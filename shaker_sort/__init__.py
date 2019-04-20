from common_sort_utils import iterables_only


@iterables_only
def shaker_sort(iterable):

    list_to_sort = list(iterable)

    left_finger = 0
    right_finger = len(list_to_sort) - 1

    while left_finger != right_finger:
        for i in range(left_finger, right_finger):
            if list_to_sort[i] > list_to_sort[i + 1]:
                list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
        right_finger -= 1

        if left_finger == right_finger:
            break

        for i in range(right_finger, left_finger, -1):
            if list_to_sort[i] < list_to_sort[i - 1]:
                list_to_sort[i], list_to_sort[i - 1] = list_to_sort[i - 1], list_to_sort[i]
        left_finger += 1

    return list_to_sort
