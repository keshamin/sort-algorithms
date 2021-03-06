from common_sort_utils import iterables_only


@iterables_only
def insert_sort(iterable):

    list_to_sort = list(iterable)

    sorted_list = list_to_sort[:1]
    for elem in list_to_sort[1:]:
        sorted_list.append(elem)
        for i in range(len(sorted_list) - 1, 0, -1):
            if sorted_list[i] < sorted_list[i - 1]:
                sorted_list[i], sorted_list[i - 1] = sorted_list[i - 1], sorted_list[i]
            else:
                break

    return sorted_list
