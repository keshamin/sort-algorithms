def bubble_sort(iterable):

    list_to_sort = list(iterable)

    for n in range(len(list_to_sort)):
        swap_made = False
        for i in range(len(list_to_sort[:-1])):
            if list_to_sort[i] > list_to_sort[i+1]:
                list_to_sort[i], list_to_sort[i+1] = list_to_sort[i+1], list_to_sort[i]
                swap_made = True
        if not swap_made:
            break

    return list_to_sort
