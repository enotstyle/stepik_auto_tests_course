def test_substring(full_string, substring):
    assert substring in full_string, f'Строка {full_string} не содержит {substring}'


def test_substring_index(full_string, substring):
    index = full_string.find(substring)
    assert index != -1, f'Строка {full_string} не содержит {substring}'


test_substring('yxxxxxxx', 'xx1')
test_substring_index('yxxxxxxx', 'xx')