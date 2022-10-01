def check_perfect_cycle(array: list[int]) -> bool:
    if not array:
        return True

    # follow the path, linear time complexity
    idx = 0
    ctr = 0
    last_idx = 0
    while 0 <= idx < len(array):
        ctr += 1
        last_idx = idx
        new_idx = array[idx]
        array[idx] = -1
        idx = new_idx

    visit_all_elements = ctr-1 == len(array)  # ctr always have 1 excess, since all elements + back to position 0
    back_to_position_0 = last_idx == 0
    return visit_all_elements and back_to_position_0


def check_perfect_cycle_batch(input: dict[str, list[int]]) -> dict[str, bool]:
    output = dict()
    for k, v in input.items():
        output[k] = check_perfect_cycle(v)
    return output
