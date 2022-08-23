import pytest 
from cards import Card, InvalidCardId


@pytest.mark.num_cards(0)
def test_start_from_todo(cards_db):
    i = cards_db.add_card(Card(summary='write a book',state='todo'))
    cards_db.start(i)
    c = cards_db.get_card(i)
    assert c.state == 'in prog'

@pytest.mark.num_cards(0)
def test_start_from_in_prog(cards_db):
    i = cards_db.add_card(Card(summary='write a book',state='in prog'))
    cards_db.start(i)
    c = cards_db.get_card(i)
    assert c.state == 'in prog'


@pytest.mark.num_cards(0)
def test_start_from_done(cards_db):
    i = cards_db.add_card(Card(summary='write a book',state='done'))
    cards_db.start(i)
    c = cards_db.get_card(i)
    assert c.state == 'in prog'


@pytest.mark.num_cards(0)
def test_start_with_invalid_id(cards_db):
    i = 123
    with pytest.raises(InvalidCardId):
        cards_db.start(i)
    
