import domain.commands.add_item as add_item
from unittest.mock import patch, call

@patch('infrastructure.storage.addJoker')
def test_add_one(mock_storage_add_joker):
    add_item.execute('foo')

    mock_storage_add_joker.assert_called_once_with('foo')

@patch('infrastructure.storage.addJoker')
def test_add_multi(mock_storage_add_joker):
    add_item.execute('foo, bar')

    mock_storage_add_joker.assert_has_calls([call('foo'), call('bar')])
