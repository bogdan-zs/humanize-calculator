import py.test as pytest
from main import (humanize_calculator,
                  INVALID_MESSAGE,
                  all,
                  humanize_number,
                  is_digit)


@pytest.mark.parametrize('exp,out', [
    ('3 + 6 = 9', 'three plus six equals nine'),
    ('3 + 6 * 11 /   - 10 -     12 = 18', 'three plus six multiply eleven divided by minus ten minus twelve equals eighteen'),
    ('154 + 3568 = 7879', 'one hundred fifty-four plus three thousand five hundred sixty-eight equals seven thousand eight hundred seventy-nine')
])
def test_humanize_calculator(exp, out):
    assert humanize_calculator(exp) == out

@pytest.mark.parametrize('number,out', [
    ('0445945896', 'four hundred forty-five million nine hundred forty-five thousand eight hundred ninety-six'),
    ('5445945896', 'five billion four hundred forty-five million nine hundred forty-five thousand eight hundred ninety-six'),
    ('5405045006', 'five billion four hundred five million forty-five thousand six'),
    ('000000000', 'zero'),
    ('5000000000', 'five billion'),
    ('455445945896', 'four hundred fifty-five billion four hundred forty-five million nine hundred forty-five thousand eight hundred ninety-six'),
    ('45445945896', 'forty-five billion four hundred forty-five million nine hundred forty-five thousand eight hundred ninety-six'),
])
def test_humanize_number(number, out):
    assert humanize_number(number) == out

def test_invalid():
    assert humanize_calculator(' 123 eqw qwe') == INVALID_MESSAGE


@pytest.mark.parametrize('arr,res', [
    ([], True),
    ([1, 2, 3], True),
    ([1, 0, 5], False),
])
def test_all(arr, res):
    assert all(arr) == res


@pytest.mark.parametrize('el,res', [
    ('qwe', False),
    ('1548544525', True),
    ('', False),
    ('5', True)
])
def test_is_digit(el, res):
    assert is_digit(el) == res
