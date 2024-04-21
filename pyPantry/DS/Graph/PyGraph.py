from pyPantry.DS import PyDS


class PyGraph(PyDS):
    def __init__(self):
        super().__init__()
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list:
            del self.adjacency_list[vertex]
            for v in self.adjacency_list:
                self.adjacency_list[v] = [
                    vtx for vtx in self.adjacency_list[v] if vtx != vertex
                ]

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1] = [
                vtx for vtx in self.adjacency_list[vertex1] if vtx != vertex2
            ]
            self.adjacency_list[vertex2] = [
                vtx for vtx in self.adjacency_list[vertex2] if vtx != vertex1
            ]

    def get_neighbors(self, vertex):
        if vertex in self.adjacency_list:
            return self.adjacency_list[vertex]
        else:
            return []

    def __str__(self):
        graph_str = ""
        for vertex in self.adjacency_list:
            graph_str += f"{vertex}: "
            neighbors = self.adjacency_list[vertex]
            for neighbor in neighbors:
                graph_str += f"{neighbor} "
            graph_str += "\n"
        return graph_str
