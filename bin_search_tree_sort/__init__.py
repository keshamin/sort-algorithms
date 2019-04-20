from bin_search_tree_sort.bin_search_tree import BinSearchTree
from collections import Iterable


def bin_tree_sort(iterable):
    if not isinstance(iterable, Iterable):
        raise ValueError('Cannot sort non-iterable object!')

    return BinSearchTree.build_tree_from_list(values_list=iterable).get_sorted_list()
