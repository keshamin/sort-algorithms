from bubble_sort import bubble_sort
from tests.utils import int_lists_gen


class TestBubbleSort(object):

    def test_random_int_list(self):
        to_sort = [1, -5, 32, 100055, 285, -9285, 205, 526, 94]
        assert  bubble_sort(to_sort) == sorted(to_sort)

    def test_100_int_lists(self):
        for test_list in int_lists_gen(n=100):
            assert bubble_sort(test_list) == sorted(test_list)
