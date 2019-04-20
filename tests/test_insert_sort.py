from insert_sort import insert_sort
from tests.common_tests_class import CommonTestsClass


class TestBubbleSort(CommonTestsClass):

    sort_function = staticmethod(insert_sort)
