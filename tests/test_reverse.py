from pathlib import Path
from hexlet_pytest.example import reverse

def get_test_data_path(filename):
    return Path(__file__).parent / 'test_data' / filename 


def read_file(filename):
    return get_test_data_path(filename).read_text()


def test_reverse():
    original_text = read_file('original.txt')
    expected = read_file('expected.txt')
    actual = reverse(original_text)
    
    assert actual == expected