import random
import time


def int_lists_gen(n=100, len_min=1, len_max=1000, value_min=-10 ** 6, value_max= 10 ** 6):
    """
    Generates lists of random ints (values thresholds can be specified)
    with random length (length thresholds can be specified.

    :param int n: number of lists to generate
    :param len_min: Lower threshold of length of generated lists
    :param len_max: Upper threshold of length of generated lists
    :param value_min: Lower threshold of values in generated lists
    :param value_max: Upper threshold of values in generated lists

    :return: list of ints
    """
    for i in range(n):
        random.seed(time.time())
        list_len = random.randint(len_min, len_max)
        yield [random.randint(value_min, value_max) for _ in range(list_len)]