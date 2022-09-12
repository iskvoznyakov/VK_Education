import pytest

# Задание первой функции


def is_sum_even(a, b):
    if (a + b) % 2 == 0:
        return True
    else:
        return False

# Параметризация первого теста


@pytest.mark.parametrize('a, b, expected_result', [(-46.5, -53.5, True),
                                                   (-15.3, 14.3, False),
                                                   (23.45, -23.45, True),
                                                   (34.345, -33.345, False),
                                                   (89.2, 10.8, True)])
# Первый тест


def test_1_is_sum_of_floats_even(a, b, expected_result):
    assert is_sum_even(a, b) == expected_result


# Задание второй функции


def division(a, b):
    return a / b

# Второй тест


def test_2_division_with_error():
    with pytest.raises(TypeError):
        assert division(25.34, '11.67')

# Задание третьей функции


def multiplication(a, b):
    return a*b

# Третий тест


def test_3_list_multiplication_by_number():
    assert multiplication([1, 2, 3], 3) == [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Задание четвертой функции


def smallest_digit(a):
    return min(a)

# Четвертый тест


def test_4_smallest_digit_of_list():
    assert smallest_digit([5, 45, 3, 657, 7, 1, 345, 54]) == 1

# Задание пятой функции


def length_of_tuple(a):
    return len(a)

# Пятый тест


def test_5_length_of_tuple():
    assert length_of_tuple(('a', 2, 52, 'cat', 78)) == 5

# Задание шестой функции


def slices_of_tuple(a):
    return a[::2]

# Шестой тест


def test_6_slices_of_tuple():
    assert slices_of_tuple((1, -1, 2, -2, 3, -3, 4, -4)) == (1, 2, 3, 4)




