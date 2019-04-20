from bin_search_tree_sort.bin_search_tree import BinSearchTree


def bin_tree_sort(list_to_sort):
    if not isinstance(list_to_sort, list):
        raise ValueError('This function takes only lists to sort!')

    return BinSearchTree.build_tree_from_list(values_list=list_to_sort).get_sorted_list()
