from perfect_cycle.lib import check_perfect_cycle


def test_perfect_cycle():
    assert check_perfect_cycle([3, 0, 1, 2]) is True
    assert check_perfect_cycle([]) is True

    assert check_perfect_cycle([1, 2, 3]) is False
    assert check_perfect_cycle([0, 2, 5]) is False
    assert check_perfect_cycle([3, 0, 1, 2, -1]) is False
    assert check_perfect_cycle([3, 0, -1, 2]) is False
    assert check_perfect_cycle([100, 0, -1, 2]) is False
    assert check_perfect_cycle([-100, 0, -1, 2]) is False
