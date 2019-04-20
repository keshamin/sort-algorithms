from bin_search_tree_sort import *
import random
import time
import pytest


class TestBinTreeSort(object):
    """Tests bin_search_tree_sort function.
    """
    @staticmethod
    def int_lists_gen(n=100):
        """
        Generates lists of random ints with length up to 1000
        :param int n: number of lists to generate
        :return: list of ints
        """
        for i in range(n):
            random.seed(time.time())
            list_len = random.randint(0, 1000)
            yield [random.randint(-10 ** 6, 10 ** 6) for _ in range(list_len)]

    def test_sort_100_random_int_lists(self):
        for test_list in self.int_lists_gen(n=100):
            assert bin_tree_sort(test_list) == sorted(test_list)

    def test_pass_not_list(self):
        with pytest.raises(ValueError):
            bin_tree_sort((1, 5, 2))

    def test_float_list(self):
        list_to_sort = [3.14, 521.245, 9.32, 1234532.234, 32.532, 543.1234]
        assert bin_tree_sort(list_to_sort) == sorted(list_to_sort)


class TestBinTree(object):
    """Tests BinTree.
    """
    @pytest.mark.parametrize('root_value, child_value, expected_side', [(1, 10, 'right'),
                                                                        (5, 2, 'left'),
                                                                        (100, 100, 'right')])
    def test_add_child(self, root_value, child_value, expected_side):
        bt = BinSearchTree(value=root_value)
        bt.add_child(child_value)
        assert isinstance(getattr(bt, expected_side), BinSearchTree)
        assert getattr(bt, expected_side).value == child_value

    def test_add_children(self):
        bt = BinSearchTree(value=10)
        bt.add_children(*(100, 53, 2, 87, 65, 39, 1))
        assert bt.left.left.value == 1
        assert bt.left.value == 2
        assert bt.right.left.left.value == 39
        assert bt.right.left.value == 53
        assert bt.right.left.right.left.value == 65
        assert bt.right.left.right.value == 87
        assert bt.right.value == 100

    def test_build_tree_from_list(self):
        bt = BinSearchTree.build_tree_from_list([66, 34, 55, 76, 67, 26, 11, 7, 88, 94])
        assert bt.left.value == 34
        assert bt.left.left.left.left.value == 7
        assert bt.right.right.right.value == 94

    def test_get_sorted_list(self):
        int_list = [random.randint(1, 100) for _ in range(20)]
        bt = BinSearchTree.build_tree_from_list(values_list=int_list)
        assert sorted(int_list) == bt.get_sorted_list()
