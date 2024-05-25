import threading
import queue
import socket
import selectors
import time

from pyPantry.DesignPatterns import PyDesignPatterns


class PyLeaderOrFollowerPattern(PyDesignPatterns):
    def __init__(self):
        self.selector = selectors.DefaultSelector()

    class Worker(threading.Thread):
        def __init__(
            self, selector, lock, condition, leader_event, followers_queue, stop_event
        ):
            super().__init__()
            self.selector = selector
            self.lock = lock
            self.condition = condition
            self.leader_event = leader_event
            self.followers_queue = followers_queue
            self.stop_event = stop_event

        def run(self):
            while not self.stop_event.is_set():
                with self.lock:
                    self.leader_event.set()
                    self.condition.notify()
                self.leader_event.wait()
                if self.stop_event.is_set():
                    break
                self.leader_event.clear()

                try:
                    events = self.selector.select(timeout=1)
                    for key, mask in events:
                        callback = key.data
                        callback(key.fileobj, mask)
                except Exception as e:
                    print(f"Error: {e}")

                with self.lock:
                    self.followers_queue.put(self)
                    self.condition.wait()

    def handle_connection(self, conn, mask):
        try:
            data = conn.recv(1024)
            if data:
                print(f"Received data: {data.decode()}")
                conn.sendall(data)
            else:
                print("Closing connection")
                self.selector.unregister(conn)
                conn.close()
        except Exception as e:
            print(f"Connection error: {e}")
            self.selector.unregister(conn)
            conn.close()

    def accept_connection(self, sock, mask):
        conn, addr = sock.accept()
        print(f"Accepted connection from {addr}")
        conn.setblocking(False)
        self.selector.register(conn, selectors.EVENT_READ, self.handle_connection)

    def example(self):
        host, port = "localhost", 65432

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((host, port))
        sock.listen()
        print(f"Listening on {(host, port)}")
        sock.setblocking(False)
        self.selector.register(sock, selectors.EVENT_READ, self.accept_connection)

        lock = threading.Lock()
        condition = threading.Condition(lock)
        leader_event = threading.Event()
        followers_queue = queue.Queue()
        stop_event = threading.Event()

        workers = [
            self.Worker(
                self.selector,
                lock,
                condition,
                leader_event,
                followers_queue,
                stop_event,
            )
            for _ in range(3)
        ]
        for worker in workers:
            followers_queue.put(worker)
            worker.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Stopping...")
            stop_event.set()
            leader_event.set()
            for worker in workers:
                worker.join()
            sock.close()
