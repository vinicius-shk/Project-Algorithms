def is_anagram(first_string, second_string):
    first_list, second_list = [*first_string.lower()], [*second_string.lower()]
    merge_sort(first_list)
    merge_sort(second_list)
    first_sorted, second_sorted = ''.join(first_list), ''.join(second_list)
    if not len(first_string) or not len(second_string):
        return (first_sorted, second_sorted, False)
    return (first_sorted, second_sorted, first_sorted == second_sorted)


def merge_sort(char_list, start=0, end=None):
    if end is None:
        end = len(char_list)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(char_list, start, mid)
        merge_sort(char_list, mid, end)
        merge(char_list, start, mid, end)


def merge(char_list, start, mid, end):
    left = char_list[start:mid]
    right = char_list[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            char_list[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            char_list[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            char_list[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            char_list[general_index] = right[right_index]
            right_index = right_index + 1
