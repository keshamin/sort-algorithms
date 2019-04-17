from bin_tree_sort.bintree import BinTree


def bin_tree_sort(list_to_sort):
    if not isinstance(list_to_sort, list):
        raise ValueError('This function takes only lists to sort!')

    return BinTree.build_tree_from_list(values_list=list_to_sort).get_sorted_list()