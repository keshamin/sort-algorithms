import pytest
from tests.utils import int_lists_gen


class CommonTestsClass(object):

    sort_function = sorted

    @pytest.mark.parametrize('int_list', list(int_lists_gen(n=100)))
    def test_int_list(self, int_list):
        assert self.sort_function(int_list) == sorted(int_list)

    def test_pass_not_list(self):
        with pytest.raises(ValueError):
            self.sort_function(None)

    def test_float_list(self):
        list_to_sort = [3.14, 521.245, 9.32, 1234532.234, 32.532, 543.1234]
        assert self.sort_function(list_to_sort) == sorted(list_to_sort)
