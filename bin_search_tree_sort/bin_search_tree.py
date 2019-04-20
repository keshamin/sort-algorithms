class BinSearchTree(object):

    def __init__(self, value):
        self.value = value
        self.left = self.right = None

    def __repr__(self):
        left_value = None if self.left is None else self.left.value
        right_value = None if self.right is None else self.right.value
        return '<Binary Tree, value: {}, left: {}, right: {}>'.format(self.value, left_value, right_value)

    @classmethod
    def build_tree_from_list(cls, values_list):
        if not isinstance(values_list, list) or len(values_list) < 1:
            raise ValueError('To build a binary tree pass non-empty list!')

        tree = BinSearchTree(values_list[0])
        if len(values_list) > 1:
            tree.add_children(*values_list[1:])

        return tree

    def add_child(self, child_value):
        if self.value > child_value:
            if self.left is None:
                self.left = BinSearchTree(child_value)
            elif isinstance(self.left, BinSearchTree):
                self.left.add_child(child_value)
            else:
                raise ValueError
        else:
            if self.right is None:
                self.right = BinSearchTree(child_value)
            elif isinstance(self.right, BinSearchTree):
                self.right.add_child(child_value)
            else:
                raise ValueError

    def add_children(self, *children_values):
        for child_value in children_values:
            self.add_child(child_value)

    def get_sorted_list(self):
        result = [self.value]
        if self.left is None:
            pass
        elif isinstance(self.left, BinSearchTree):
            result = self.left.get_sorted_list() + result
        else:
            raise ValueError

        if self.right is None:
            pass
        elif isinstance(self.right, BinSearchTree):
            result += self.right.get_sorted_list()
        else:
            raise ValueError

        return result
