from queue import Queue
from threading import Lock

from pyPantry.DesignPatterns import PyDesignPatterns


class PyObjectPoolPattern(PyDesignPatterns):
    class DatabaseConnection:
        def __init__(self, connection_id: int):
            self.connection_id = connection_id
            self.in_use = False

        def connect(self):
            print(f"Connection {self.connection_id} is now in use.")
            self.in_use = True

        def disconnect(self):
            print(f"Connection {self.connection_id} is now released.")
            self.in_use = False

        def __str__(self):
            return f"DatabaseConnection(id={self.connection_id}, in_use={self.in_use})"

    class ConnectionPool:
        def __init__(self, size: int):
            self.pool = Queue(maxsize=size)
            self.lock = Lock()
            for i in range(size):
                self.pool.put(PyObjectPoolPattern.DatabaseConnection(connection_id=i))

        def acquire_connection(self):
            with self.lock:
                if not self.pool.empty():
                    connection = self.pool.get()
                    connection.connect()
                    return connection
                else:
                    print("No available connections.")
                    return None

        def release_connection(self, connection):
            with self.lock:
                connection.disconnect()
                self.pool.put(connection)

    def example(self):
        pool = PyObjectPoolPattern.ConnectionPool(size=2)

        # Acquire and use a connection
        conn1 = pool.acquire_connection()
        conn2 = pool.acquire_connection()
        conn3 = pool.acquire_connection()  # Should print "No available connections."

        # Release connections
        if conn1:
            pool.release_connection(conn1)
        if conn2:
            pool.release_connection(conn2)

        # Try acquiring again
        conn4 = pool.acquire_connection()
        conn5 = pool.acquire_connection()
        conn6 = pool.acquire_connection()  # Should print "No available connections."
