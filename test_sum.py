import pytest

# define fixture for test sum function
@pytest.fixture
def sum_fixture():
    """
    Fixture for sum function
    """
    x = 5
    y = 10
    sum = x + y  # calculate sum using fixture values
    yield sum  # yield the sum to the test function

def test_sum(sum_fixture):
    """
    Test file that prints sum
    """
    sum = sum_fixture  # get the sum from the fixture

    assert sum == 15, f"Expected {15}, got {sum}"
