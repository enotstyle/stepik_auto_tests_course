import pytest


class TestCaseAbc:

    def test_positive_1(self):
        assert abs(-42) == 42, f'Fail, test {__class__.__name__}'

    def test_positive_2(self):
        assert abs(-42) == -42, f'Fail, test {__name__}'


if __name__ == '__main__':
    pytest.main()
