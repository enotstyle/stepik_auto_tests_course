def test_substring(full_string, substring):
    assert substring in full_string, f'Строка {full_string} не содержит {substring}'


def test_substring_index(full_string, substring):
    index = full_string.find(substring)
    assert index != -1, f'Строка {full_string} не содержит {substring}'


if __name__ == '__main__':
    test_substring('yxxxxxxx', 'xx')
    test_substring_index('yxxxxxxx', 'xx')
    print("All tests passed!")
