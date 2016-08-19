from bubble_sort import swap_elements


# Arrange the ARRAY into two segements:
# anything < PIVOT is at left, and anthing > PIVOT is at right.
# no order considered inside the segment.
def partition(ARRAY, start, end, show_step=True):
    if show_step:
        print("parition enter(%d,%d): %s" % (start, end,
                                             ARRAY[start:end+1]))
    PIVOT = ARRAY[int((start+end)/2)]
    left = start
    right = end
    while left <= right:
        while ARRAY[left] < PIVOT:
            left += 1
        while ARRAY[right] > PIVOT:
            right -= 1
        if left <= right:
            swap_elements(ARRAY, left, right)
            left += 1
            right -= 1
    if show_step:
        print("parition exit(%d,%d, %d): %s" % (start, end, PIVOT,
                                                ARRAY[start:end+1]))
    return (right, left)


def quick_sort(ARRAY, start, end):
    if (start < end):
        left_most, right_most = partition(ARRAY, start, end)
        quick_sort(ARRAY, start, left_most)
        quick_sort(ARRAY, right_most, end)
