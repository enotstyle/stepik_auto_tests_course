def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, f'Ожидаемый результат {expected_result} не соответствует фактическому {actual_result}'


test_input_text(1, 2)