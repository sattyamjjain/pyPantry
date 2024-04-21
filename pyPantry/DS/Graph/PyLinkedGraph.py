from pyPantry.DS import PyDS


class Node:
    def __init__(self, vertex):
        self.vertex = vertex
        self.next = None


class PyLinkedGraph(PyDS):
    def __init__(self):
        super().__init__()
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = None

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self._add_edge_util(vertex1, vertex2)
            self._add_edge_util(vertex2, vertex1)

    def _add_edge_util(self, src, dest):
        new_node = Node(dest)
        new_node.next = self.vertices[src]
        self.vertices[src] = new_node

    def remove_vertex(self, vertex):
        if vertex in self.vertices:
            self.vertices.pop(vertex)
            for v in self.vertices:
                self._remove_edge_util(v, vertex)

    def _remove_edge_util(self, src, dest):
        curr = self.vertices[src]
        if curr and curr.vertex == dest:
            self.vertices[src] = curr.next
        else:
            while curr and curr.next:
                if curr.next.vertex == dest:
                    curr.next = curr.next.next
                    break
                curr = curr.next

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self._remove_edge_util(vertex1, vertex2)
            self._remove_edge_util(vertex2, vertex1)

    def get_neighbors(self, vertex):
        neighbors = []
        if vertex in self.vertices:
            curr = self.vertices[vertex]
            while curr:
                neighbors.append(curr.vertex)
                curr = curr.next
        return neighbors

    def __str__(self):
        graph_str = ""
        for vertex in self.vertices:
            graph_str += f"{vertex}: "
            neighbors = self.get_neighbors(vertex)
            graph_str += " ".join(str(neighbor) for neighbor in neighbors)
            graph_str += "\n"
        return graph_str
