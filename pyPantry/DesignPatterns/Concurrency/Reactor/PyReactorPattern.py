import selectors
import socket
import types

from pyPantry.DesignPatterns import PyDesignPatterns


class PyReactorPattern(PyDesignPatterns):
    # Event Handler Interface
    class EventHandler:
        def handle_event(self, key, mask) -> None:
            pass

    # Concrete Event Handlers
    class AcceptEventHandler(EventHandler):
        def __init__(self, sock, selector):
            self.sock = sock
            self.selector = selector

        def handle_event(self, key, mask) -> None:
            conn, addr = self.sock.accept()  # Should be ready to read
            print(f"Accepted connection from {addr}")
            conn.setblocking(False)
            data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
            events = selectors.EVENT_READ | selectors.EVENT_WRITE
            self.selector.register(conn, events, data=data)

    class ReadEventHandler(EventHandler):
        def __init__(self, selector):
            self.selector = selector

        def handle_event(self, key, mask) -> None:
            sock = key.fileobj
            data = key.data
            if mask & selectors.EVENT_READ:
                recv_data = sock.recv(1024)  # Should be ready to read
                if recv_data:
                    data.outb += recv_data
                else:
                    print(f"Closing connection to {data.addr}")
                    self.selector.unregister(sock)
                    sock.close()

            if mask & selectors.EVENT_WRITE:
                if data.outb:
                    print(f"Echoing data to {data.addr}")
                    sent = sock.send(data.outb)  # Should be ready to write
                    data.outb = data.outb[sent:]

    # Reactor
    class Reactor:
        def __init__(self):
            self.selector = selectors.DefaultSelector()

        def register_handler(self, sock, handler, events) -> None:
            self.selector.register(sock, events, data=handler)

        def unregister_handler(self, sock) -> None:
            self.selector.unregister(sock)

        def run(self) -> None:
            while True:
                events = self.selector.select(timeout=None)
                for key, mask in events:
                    handler = key.data
                    handler.handle_event(key, mask)

    def example(self):
        host, port = "localhost", 65432

        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((host, port))
        sock.listen()
        print(f"Listening on {(host, port)}")
        sock.setblocking(False)

        reactor = PyReactorPattern.Reactor()

        # Register the accept handler
        accept_handler = PyReactorPattern.AcceptEventHandler(sock, reactor.selector)
        reactor.register_handler(sock, accept_handler, selectors.EVENT_READ)

        # Run the reactor
        reactor.run()
