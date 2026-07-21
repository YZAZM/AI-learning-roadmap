from services.score_service import calculate_average, get_grade


def test_calculate_average():
    result = calculate_average([80, 90, 100])
    assert result == 90


def test_get_grade():
    assert get_grade(95) == "A"
    assert get_grade(85) == "B"
    assert get_grade(75) == "C"
    assert get_grade(65) == "D"
    assert get_grade(50) == "F"