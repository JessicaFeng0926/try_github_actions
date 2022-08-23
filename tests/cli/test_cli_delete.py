from cards import Card, InvalidCardId
import pytest 

def test_delete_from_many_items(cards_db,cards_cli):
    i = cards_db.add_card(Card('task 1'))
    cards_db.add_card(Card('task 2'))
    cards_db.add_card(Card('task 3'))
    cards_cli(f'delete {i}')
    with pytest.raises(InvalidCardId):
        cards_db.get_card(i)

def test_delete_from_one_item(cards_db,cards_cli):
    i = cards_db.add_card(Card('task 1'))
    cards_cli(f'delete {i}')
    assert len(cards_db.list_cards()) == 0
    with pytest.raises(InvalidCardId):
        cards_db.get_card(i)

def test_delete_with_invalid_id(cards_db,cards_cli):
    i = 123
    output = cards_cli(f'delete {i}')
    assert 'Error' in output 

