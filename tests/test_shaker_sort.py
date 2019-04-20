from tests.common_tests_class import CommonTestsClass
from shaker_sort import shaker_sort


class TestShakerSort(CommonTestsClass):
    sort_function = staticmethod(shaker_sort)
