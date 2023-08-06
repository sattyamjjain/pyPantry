import unittest

from pyDSAlgo.DS.Graph.PyLinkedGraph import PyLinkedGraph


class TestPyLinkedGraph(unittest.TestCase):
    def setUp(self):
        self.graph = PyLinkedGraph()

    def test_add_vertex(self):
        self.graph.add_vertex("A")
        self.assertIn("A", self.graph.vertices)

        self.graph.add_vertex("B")
        self.assertIn("B", self.graph.vertices)

        self.graph.add_vertex("C")
        self.assertIn("C", self.graph.vertices)

    def test_add_edge(self):
        self.graph.add_vertex("A")
        self.graph.add_vertex("B")
        self.graph.add_vertex("C")

        self.graph.add_edge("A", "B")
        self.assertEqual(set(self.graph.get_neighbors("A")), {"B"})
        self.assertEqual(set(self.graph.get_neighbors("B")), {"A"})

        self.graph.add_edge("A", "C")
        self.assertEqual(set(self.graph.get_neighbors("A")), {"B", "C"})
        self.assertEqual(set(self.graph.get_neighbors("C")), {"A"})

    def test_remove_vertex(self):
        self.graph.add_vertex("A")
        self.graph.add_vertex("B")
        self.graph.add_vertex("C")

        self.graph.add_edge("A", "B")
        self.graph.add_edge("A", "C")

        self.graph.remove_vertex("B")
        self.assertNotIn("B", self.graph.vertices)
        self.assertEqual(self.graph.get_neighbors("A"), ["C"])

    def test_remove_edge(self):
        self.graph.add_vertex("A")
        self.graph.add_vertex("B")
        self.graph.add_vertex("C")

        self.graph.add_edge("A", "B")
        self.graph.add_edge("A", "C")

        self.graph.remove_edge("A", "B")
        self.assertEqual(self.graph.get_neighbors("A"), ["C"])
        self.assertEqual(self.graph.get_neighbors("B"), [])

    def test_get_neighbors(self):
        self.graph.add_vertex("A")
        self.graph.add_vertex("B")
        self.graph.add_vertex("C")

        self.graph.add_edge("A", "B")
        self.graph.add_edge("A", "C")

        neighbors = self.graph.get_neighbors("A")
        self.assertEqual(set(neighbors), {"B", "C"})

        neighbors = self.graph.get_neighbors("B")
        self.assertEqual(set(neighbors), {"A"})

        neighbors = self.graph.get_neighbors("C")
        self.assertEqual(set(neighbors), {"A"})

    def test_str(self):
        self.graph.add_vertex("A")
        self.graph.add_vertex("B")
        self.graph.add_vertex("C")

        self.graph.add_edge("A", "B")
        self.graph.add_edge("A", "C")

        graph_str = str(self.graph)
        expected_str = "A: B C \nB: A \nC: A \n"
        self.assertEqual(set(graph_str.split()), set(expected_str.split()))


if __name__ == "__main__":
    unittest.main()
