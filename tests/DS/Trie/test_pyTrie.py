import unittest

from pyPantry.DS.Trie.PyTrie import PyTrie


class PyTrieTestCase(unittest.TestCase):
    def setUp(self):
        self.trie = PyTrie()

    def test_insert(self):
        self.trie.insert("apple")
        self.assertTrue(self.trie.search("apple"))
        self.assertFalse(self.trie.search("app"))
        self.assertFalse(self.trie.search("orange"))

        self.trie.insert("app")
        self.assertTrue(self.trie.search("app"))

        self.trie.insert("banana")
        self.assertTrue(self.trie.search("banana"))
        self.assertFalse(self.trie.search("ban"))

    def test_starts_with(self):
        self.trie.insert("apple")
        self.trie.insert("app")
        self.trie.insert("banana")

        self.assertTrue(self.trie.starts_with("app"))
        self.assertTrue(self.trie.starts_with("apple"))
        self.assertTrue(self.trie.starts_with("banana"))
        self.assertTrue(self.trie.starts_with("ban"))

        self.assertFalse(self.trie.starts_with("orange"))


if __name__ == "__main__":
    unittest.main()
