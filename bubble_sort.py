import random


def swap_elements(ARRAY, idx1, idx2):
    tmp = ARRAY[idx1]
    ARRAY[idx1] = ARRAY[idx2]
    ARRAY[idx2] = tmp


def element_not_in_order(elm1, elm2, ascending=True):
    if ascending:
        return True if elm1 > elm2 else False
    return False if elm1 > elm2 else True


# bubble_sort1 did not consider that for every pass, the last one
# is either the largest (ascending=True), or the least (ascending=False)
def bubble_sort1(ARRAY, show_step=False, ascending=True):
    num_of_element = len(ARRAY)
    total_compared = 0
    total_swapped = 0
    if show_step:
        print("element: %s" % (ARRAY))
    for PASS in range(1, num_of_element):
        COMPARISON = num_of_element - 1
        num_exchanged = 0
        for idx1 in range(0, COMPARISON):
            total_compared += 1
            idx2 = idx1 + 1
            if element_not_in_order(ARRAY[idx1],
                                    ARRAY[idx2],
                                    ascending):
                swap_elements(ARRAY, idx1, idx2)
                num_exchanged += 1
        if show_step:
            print("PASS#%s: %s" % (PASS, ARRAY))
        total_swapped += num_exchanged
        if num_exchanged == 0:
            return (PASS, total_compared, total_swapped)
    return (PASS, total_compared, total_swapped)


def bubble_sort2(ARRAY, show_step=False, ascending=True):
    num_of_element = len(ARRAY)
    total_compared = 0
    total_swapped = 0
    if show_step:
        print("element: %s" % (ARRAY))
    for PASS in range(1, num_of_element):
        COMPARISON = num_of_element - PASS
        num_exchanged = 0
        for idx1 in range(0, COMPARISON):
            total_compared += 1
            idx2 = idx1 + 1
            if element_not_in_order(ARRAY[idx1],
                                    ARRAY[idx2],
                                    ascending):
                swap_elements(ARRAY, idx1, idx2)
                num_exchanged += 1
        if show_step:
            print("PASS#%s: %s" % (PASS, ARRAY))
        total_swapped += num_exchanged
        if num_exchanged == 0:
            return (PASS, total_compared, total_swapped)
    return (PASS, total_compared, total_swapped)


# utitlity
def gen_elements(num=10, start=1, step=1):
    stop = num + start
    _list = range(start, stop, step)
    random.shuffle(_list)
    return _list
