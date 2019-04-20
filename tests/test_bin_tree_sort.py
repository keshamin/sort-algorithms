from bin_search_tree_sort import *
import random
import pytest

from tests.common_tests_class import CommonTestsClass


class TestBinTreeSort(CommonTestsClass):
    """Tests bin_search_tree_sort function.
    """

    sort_function = staticmethod(bin_tree_sort)


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
