from bin_search_tree_sort.bin_search_tree import BinSearchTree
from common_sort_utils import iterables_only


@iterables_only
def bin_tree_sort(iterable):

    return BinSearchTree.build_tree_from_list(values_list=iterable).get_sorted_list()
