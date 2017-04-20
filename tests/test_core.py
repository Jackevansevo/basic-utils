import pytest

from unittest.mock import patch, MagicMock, mock_open

from basic_utils.core import (
    clear,
    getattrs,
    identity,
    map_getattr,
    recursive_default_dict,
    rgetattr,
    rsetattr,
    slurp,
    to_string,
)


def test_slurp():
    """Tests that slurp reads in contents of a file as a string"""
    data = "In the face of ambiguity, refuse the temptation to guess."
    with patch("builtins.open", mock_open(read_data=data)) as mock_file:
        file_contents = slurp('text.txt')
        mock_file.assert_called_once_with('text.txt', 'r')
        assert file_contents == data


@pytest.mark.parametrize("platform, expected", [
    ('posix', 'clear'),
    ('nt', 'cls')
])
def test_clear(platform, expected):
    """
    Tests that os.system is called with the correct string corresponding to
    the host OS name
    """
    with patch('basic_utils.core.os') as mock_os:
        mock_os.name = platform
        clear()
        mock_os.system.assert_called_once_with(expected)


def test_to_string():
    # Create two mock class instances which implement __str__
    objectX, objectY = MagicMock(), MagicMock()
    objectX.__str__.return_value = "Homer"
    objectY.__str__.return_value = "Bart"
    assert to_string([objectX, objectY]) == "Homer, Bart"
    assert to_string([1, 2, 3]) == "1, 2, 3"


def test_getattrs():
    # Create two mock class instances with a sample attribute
    mock_obj = MagicMock()
    mock_obj.name = 'Homer'
    mock_obj.age = 39
    assert getattrs(mock_obj, ('name', 'age')) == ('Homer', 39)


def test_map_getattr():
    # Create two mock class instances with a sample attribute
    objectX, objectY = MagicMock(), MagicMock()
    objectX.name = 'Homer'
    objectY.name = 'Bart'
    assert map_getattr('name', (objectX, objectY)) == ('Homer', 'Bart')


def test_recursive_default_dict():
    """
    Tests that recursive data structure points to itself
    """
    my_dict = recursive_default_dict()
    assert isinstance(my_dict['random_key'], type(my_dict))


@pytest.mark.parametrize("data", [
    (10), ((10, 20)), (("Homer", "Marge"))
])
def test_identity(data):
    """Tests that identity returns the same arguments as it was passed"""
    assert identity(data) == data


class TestRecursiveGettersAndSetters:

    @classmethod
    def setup_class(cls):
        cls.homer, cls.child = MagicMock(), MagicMock()
        cls.homer.child = cls.child
        cls.child.name = 'Bart'

    def test_rgetattr(self):
        """
        Tests that rgetattr returns returns nested values within objects
        """
        assert rgetattr(self.homer, 'child.name') == 'Bart'

    def test_rsetattr(self):
        """
        Tests that rsetattr sets the value of a nested attribute
        """
        rsetattr(self.homer, 'child.name', 'Lisa')
        assert self.child.name == 'Lisa'
