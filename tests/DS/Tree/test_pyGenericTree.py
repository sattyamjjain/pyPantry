import unittest

from pyDSAlgo.DS.Tree.PyGenericTree import PyGenericTree


class GenericTreeTestCase(unittest.TestCase):
    def test_add_root(self):
        tree = PyGenericTree()
        tree.add_root("A")
        self.assertEqual(tree.get_root().data, "A")
        self.assertRaises(ValueError, tree.add_root, "B")

    def test_add_child(self):
        tree = PyGenericTree()
        tree.add_root("A")
        tree.add_child(tree.get_root(), "B")
        tree.add_child(tree.get_root(), "C")
        tree.add_child(tree.get_root().children[0], "D")
        self.assertEqual(len(tree.get_root().children), 2)
        self.assertEqual(tree.get_root().children[0].data, "B")
        self.assertEqual(tree.get_root().children[1].data, "C")
        self.assertEqual(tree.get_root().children[0].children[0].data, "D")
        self.assertRaises(ValueError, tree.add_child, None, "E")

    def test_traverse_preorder(self):
        tree = PyGenericTree()
        tree.add_root("A")
        tree.add_child(tree.get_root(), "B")
        tree.add_child(tree.get_root(), "C")
        tree.add_child(tree.get_root().children[0], "D")
        tree.add_child(tree.get_root().children[0], "E")
        tree.add_child(tree.get_root().children[1], "F")
        expected_output = ["A", "B", "D", "E", "C", "F"]

        captured_output = tree.traverse_pre_order(tree.get_root())

        self.assertEqual(captured_output, expected_output)

    def test_traverse_postorder(self):
        tree = PyGenericTree()
        tree.add_root("A")
        tree.add_child(tree.get_root(), "B")
        tree.add_child(tree.get_root(), "C")
        tree.add_child(tree.get_root().children[0], "D")
        tree.add_child(tree.get_root().children[0], "E")
        tree.add_child(tree.get_root().children[1], "F")
        expected_output = ["D", "E", "B", "F", "C", "A"]

        captured_output = tree.traverse_post_order(tree.get_root())

        self.assertEqual(captured_output, expected_output)

    def test_traverse_level_order(self):
        tree = PyGenericTree()
        tree.add_root("A")
        tree.add_child(tree.get_root(), "B")
        tree.add_child(tree.get_root(), "C")
        tree.add_child(tree.get_root().children[0], "D")
        tree.add_child(tree.get_root().children[0], "E")
        tree.add_child(tree.get_root().children[1], "F")
        expected_output = ["A", "B", "C", "D", "E", "F"]

        captured_output = tree.traverse_level_order()

        self.assertEqual(captured_output, expected_output)


if __name__ == "__main__":
    unittest.main()
