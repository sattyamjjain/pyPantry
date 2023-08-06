class Node:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.child = []


class PyBTree:
    def __init__(self, t):
        self.root = Node(True)
        self.t = t

    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            temp = Node()
            self.root = temp
            temp.child.insert(0, root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)

    def insert_non_full(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append((k, None))
            x.keys.sort(key=lambda x: x[0])
        else:
            while i >= 0 and k < x.keys[i][0]:
                i -= 1
            i += 1
            if len(x.child[i].keys) == (2 * self.t) - 1:
                self.split_child(x, i)
                if k > x.keys[i][0]:
                    i += 1
            self.insert_non_full(x.child[i], k)

    def split_child(self, i, x):
        t = self.t
        y = i.child[x]
        z = Node(y.leaf)
        i.child.insert(x + 1, z)
        i.keys.insert(x, y.keys[t - 1])
        z.keys = y.keys[t : (2 * t - 1)]
        y.keys = y.keys[0 : (t - 1)]
        if not y.leaf:
            z.child = y.child[t : (2 * t)]
            y.child = y.child[0 : (t - 1)]

    def print_tree(self, x, l=0):
        print("Level ", l, " ", len(x.keys), end=":")
        for i in x.keys:
            print(i, end=" ")
        print()
        l += 1
        if len(x.child) > 0:
            for i in x.child:
                self.print_tree(i, l)

    def search(self, k, x=None):
        if x is not None:
            i = 0
            while i < len(x.keys) and k > x.keys[i][0]:
                i += 1
            if i < len(x.keys) and k == x.keys[i][0]:
                return x
            elif len(x.child) > 0:
                return self.search(k, x.child[i])
            else:
                return None
        else:
            return self.search(k, self.root)

    def inorder_traversal(self, x=None):
        """
        Inorder traversal of the B-Tree.
        """
        if x is None:
            x = self.root
        keys = []
        for i, key in enumerate(x.keys):
            if len(x.child) > i:
                keys.extend(self.inorder_traversal(x.child[i]))
            keys.append(key[0])
        if len(x.child) > len(x.keys):
            keys.extend(self.inorder_traversal(x.child[-1]))
        return keys

    def delete(self, k, x=None):
        if x is None:
            x = self.root
        t = self.t
        i = 0
        while i < len(x.keys) and k > x.keys[i][0]:
            i += 1
        if x.leaf:
            if i < len(x.keys) and x.keys[i][0] == k:
                x.keys.pop(i)
                return
            return

        if i < len(x.keys) and x.keys[i][0] == k:
            return self.delete_internal_node(x, i, k)
        elif len(x.child[i].keys) >= t:
            self.delete(k, x.child[i])
        else:
            if i != 0 and i + 2 < len(x.child):
                if len(x.child[i - 1].keys) >= t:
                    self.delete_sibling(x, i, i - 1)
                elif len(x.child[i + 1].keys) >= t:
                    self.delete_sibling(x, i, i + 1)
                else:
                    self.delete_merge(x, i, i + 1)
            elif i == 0:
                if len(x.child[i + 1].keys) >= t:
                    self.delete_sibling(x, i, i + 1)
                else:
                    self.delete_merge(x, i, i + 1)
            elif i + 1 == len(x.child):
                if len(x.child[i - 1].keys) >= t:
                    self.delete_sibling(x, i, i - 1)
                else:
                    self.delete_merge(x, i, i - 1)
        self.delete(k, x.child[i])

    def delete_merge(self, x, i, j):
        c_node = x.child[i]

        if j > i:
            rs_node = x.child[j]
            c_node.keys.append(x.keys[i])
            for k, item in enumerate(rs_node.keys):
                c_node.keys.append(item)
                if len(rs_node.child) > 0:
                    c_node.child.append(rs_node.child[k])
            if len(rs_node.child) > 0:
                c_node.child.append(rs_node.child.pop())
            new = c_node
            x.keys.pop(i)
            x.child.pop(j)
        else:
            ls_node = x.child[j]
            ls_node.keys.append(x.keys[j])
            for i, item in reversed(list(enumerate(c_node.keys))):
                ls_node.keys.append(item)
                if len(c_node.child) > 0:
                    ls_node.child.append(c_node.child[i])
            if len(c_node.child) > 0:
                ls_node.child.append(c_node.child.pop())
            new = ls_node
            x.keys.pop(j)
            x.child.pop(i)

        if x == self.root and len(x.keys) == 0:
            self.root = new

    def delete_sibling(self, x, i, j):
        c_node = x.child[i]
        if i < j:
            rs_node = x.child[j]
            c_node.keys.append(x.keys[i])
            x.keys[i] = rs_node.keys[0]
            if len(rs_node.child) > 0:
                c_node.child.append(rs_node.child.pop(0))
            rs_node.keys.pop(0)
        else:
            ls_node = x.child[j]
            c_node.keys.insert(0, x.keys[i - 1])
            x.keys[i - 1] = ls_node.keys.pop()
            if len(ls_node.child) > 0:
                c_node.child.insert(0, ls_node.child.pop())

    def delete_internal_node(self, x, i, k):
        t = self.t
        if x.leaf:
            if x.keys[i][0] == k:
                x.keys.pop(i)
                return
            else:
                return

        child = x.child[i]
        if len(child.keys) >= t:
            x.keys[i] = self.delete_predecessor(child)
            return
        elif len(x.child[i + 1].keys) >= t:
            x.keys[i] = self.delete_successor(x.child[i + 1])
            return
        else:
            self.delete_merge(x, i, i + 1)
            self.delete_internal_node(x.child[i], len(x.child[i].keys) - 1, k)

    def delete_predecessor(self, x):
        if x.leaf:
            return x.keys.pop()

        if len(x.child[-1].keys) >= self.t:
            return self.delete_max(x.child[-1])

        if len(x.child[-1].keys) == self.t - 1:
            c = x.child[-1]
            sibling = x.child[-2]

            if len(sibling.keys) >= self.t:
                c.keys.insert(0, x.keys[-1])
                x.keys[-1] = sibling.keys.pop()
                if len(sibling.child) > 0:
                    c.child.insert(0, sibling.child.pop())
                return self.delete_predecessor(c)

            sibling.keys.append(x.keys.pop())
            sibling.keys += c.keys
            sibling.child += c.child
            x.child.pop()
            return self.delete_predecessor(sibling)

    def delete_max(self, x):
        if x.leaf:
            return x.keys.pop()

        if len(x.child[-1].keys) >= self.t:
            return self.delete_max(x.child[-1])

        if len(x.child[-1].keys) == self.t - 1:
            c = x.child[-1]
            sibling = x.child[-2]

            if len(sibling.keys) >= self.t:
                c.keys.insert(0, x.keys.pop())
                x.keys.append(sibling.keys.pop())
                if len(sibling.child) > 0:
                    c.child.insert(0, sibling.child.pop())
                return self.delete_max(c)

            sibling.keys.append(x.keys.pop())
            sibling.keys += c.keys
            sibling.child += c.child
            x.child.pop()
            return self.delete_max(sibling)

    def delete_successor(self, x):
        if x.leaf:
            return x.keys.pop(0)
        if len(x.child[1].keys) >= self.t:
            self.delete_sibling(x, 0, 1)
        else:
            self.delete_merge(x, 0, 1)
        self.delete_successor(x)
