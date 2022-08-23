import pytest 
from cards import Card, InvalidCardId 

@pytest.mark.num_cards(0)
def test_update_owner(cards_db):
    i = cards_db.add_card(Card(summary='write a book',owner='Alex'))
    cards_db.update_card(i,Card(owner='John'))
    c = cards_db.get_card(i)
    assert c.summary=='write a book' and c.owner == 'John'

@pytest.mark.num_cards(0)
def test_update_summary(cards_db):
    i = cards_db.add_card(Card(summary='write a book',owner='Alex'))
    cards_db.update_card(i,Card(summary='give a lesson'))
    c = cards_db.get_card(i)
    assert c.summary=='give a lesson' and c.owner == 'Alex'


@pytest.mark.num_cards(0)
def test_update_owner_and_summary(cards_db):
    i = cards_db.add_card(Card(summary='write a book',owner='Alex'))
    cards_db.update_card(i,Card(owner='John',summary='give a lesson'))
    c = cards_db.get_card(i)
    assert c.summary=='give a lesson' and c.owner == 'John'

@pytest.mark.num_cards(0)
def test_update_invalid_id(cards_db):
    i = 123
    with pytest.raises(InvalidCardId):
        cards_db.update_card(i,Card(owner='John'))



   
