import unittest

from pyDSAlgo.DS.Graph.PyGraph import PyGraph


class PyGraphTestCase(unittest.TestCase):
    def setUp(self):
        self.graph = PyGraph()

    def test_add_vertex(self):
        self.graph.add_vertex("A")
        self.assertIn("A", self.graph.adjacency_list)

        self.graph.add_vertex("B")
        self.assertIn("B", self.graph.adjacency_list)

        self.graph.add_vertex("C")
        self.assertIn("C", self.graph.adjacency_list)

    def test_add_edge(self):
        self.graph.add_vertex("A")
        self.graph.add_vertex("B")
        self.graph.add_vertex("C")

        self.graph.add_edge("A", "B")
        self.assertEqual(self.graph.adjacency_list["A"], ["B"])
        self.assertEqual(self.graph.adjacency_list["B"], ["A"])

        self.graph.add_edge("A", "C")
        self.assertEqual(self.graph.adjacency_list["A"], ["B", "C"])
        self.assertEqual(self.graph.adjacency_list["C"], ["A"])

    def test_remove_vertex(self):
        self.graph.add_vertex("A")
        self.graph.add_vertex("B")
        self.graph.add_vertex("C")

        self.graph.add_edge("A", "B")
        self.graph.add_edge("A", "C")

        self.graph.remove_vertex("B")
        self.assertNotIn("B", self.graph.adjacency_list)
        self.assertEqual(self.graph.adjacency_list["A"], ["C"])

    def test_remove_edge(self):
        self.graph.add_vertex("A")
        self.graph.add_vertex("B")
        self.graph.add_vertex("C")

        self.graph.add_edge("A", "B")
        self.graph.add_edge("A", "C")

        self.graph.remove_edge("A", "B")
        self.assertEqual(self.graph.adjacency_list["A"], ["C"])
        self.assertEqual(self.graph.adjacency_list["B"], [])

    def test_get_neighbors(self):
        self.graph.add_vertex("A")
        self.graph.add_vertex("B")
        self.graph.add_vertex("C")

        self.graph.add_edge("A", "B")
        self.graph.add_edge("A", "C")

        neighbors = self.graph.get_neighbors("A")
        self.assertEqual(neighbors, ["B", "C"])

        neighbors = self.graph.get_neighbors("B")
        self.assertEqual(neighbors, ["A"])

        neighbors = self.graph.get_neighbors("C")
        self.assertEqual(neighbors, ["A"])

    def test_str(self):
        self.graph.add_vertex("A")
        self.graph.add_vertex("B")
        self.graph.add_vertex("C")

        self.graph.add_edge("A", "B")
        self.graph.add_edge("A", "C")

        graph_str = str(self.graph)
        expected_str = "A: B C \nB: A \nC: A \n"
        self.assertEqual(graph_str, expected_str)


if __name__ == "__main__":
    unittest.main()
