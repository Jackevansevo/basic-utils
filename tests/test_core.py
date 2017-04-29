from unittest.mock import MagicMock, Mock, mock_open, patch

import pytest  # type: ignore

from basic_utils.core import (
    clear,
    getattrs,
    map_getattr,
    recursive_default_dict,
    rgetattr,
    rsetattr,
    slurp,
    to_string
)


def test_slurp() -> None:
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
def test_clear(platform: str, expected: str) -> None:
    """
    Tests that os.system is called with the correct string corresponding to
    the host OS name
    """
    with patch('basic_utils.core.os') as mock_os:
        mock_os.name = platform
        clear()
        mock_os.system.assert_called_once_with(expected)


def test_to_string() -> None:
    # Create two mock class instances which implement __str__
    objectX, objectY = Mock(), Mock()
    objectX.__str__ = Mock(return_value='Homer')  # type: ignore
    objectY.__str__ = Mock(return_value='Bart')  # type: ignore
    assert to_string([objectX, objectY]) == "Homer, Bart"
    assert to_string([1, 2, 3]) == "1, 2, 3"


def test_getattrs() -> None:
    # Create a single mock class instance with two sample attributes
    mock_obj = Mock(forename='Homer', age=39)  # type: ignore
    assert getattrs(mock_obj, ('forename', 'age')) == ('Homer', 39)


def test_map_getattr() -> None:
    # Create two mock class instances with a sample attribute
    objectX = Mock(forename='Homer')  # type: ignore
    objectY = Mock(forename='Bart')  # type: ignore
    assert map_getattr('forename', (objectX, objectY)) == ('Homer', 'Bart')


def test_recursive_default_dict() -> None:
    """
    Tests that recursive data structure points to itself
    """
    my_dict = recursive_default_dict()
    assert isinstance(my_dict['random_key'], type(my_dict))


class TestRecursiveGettersAndSetters:

    @classmethod
    def setup_class(cls) -> None:
        cls.child = MagicMock(forename='Bart')  # type: ignore
        cls.homer = MagicMock(child=cls.child)  # type: ignore

    def test_rgetattr(self) -> None:
        """
        Tests that rgetattr returns returns nested values within objects
        """
        assert rgetattr(self.homer, 'child.forename') == 'Bart'  # type: ignore

    def test_rsetattr(self) -> None:
        """
        Tests that rsetattr sets the value of a nested attribute
        """
        rsetattr(self.homer, 'child.name', 'Lisa')  # type: ignore
        assert self.child.name == 'Lisa'  # type: ignore
