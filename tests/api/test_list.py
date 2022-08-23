import pytest 
from cards import Card

@pytest.mark.num_cards(0)
def test_list_empty(cards_db):
    lst = cards_db.list_cards()
    assert len(lst) == 0



@pytest.mark.num_cards(3)
def test_list_non_empty(cards_db):
    lst = cards_db.list_cards()
    assert len(lst) == 3


@pytest.mark.num_cards(0)
def test_list_owner(cards_db):
    cards = [
        Card(summary='foo',owner='Alex'),
        Card(summary='foo',owner='Julie'),
        Card(summary='foo',owner='Rex'),
    ]
    for c in cards:
        cards_db.add_card(c)
    lst = cards_db.list_cards(owner='Alex')
    assert len(lst) == 1 and lst[0].owner == 'Alex'


@pytest.mark.num_cards(0)
def test_list_state(cards_db):
    cards = [
        Card(summary='foo',state='todo'),
        Card(summary='foo',state='in prog'),
        Card(summary='foo',state='done'),
    ]
    for c in cards:
        cards_db.add_card(c)
    lst = cards_db.list_cards(state='in prog')
    assert len(lst) == 1 and lst[0].state == 'in prog'


@pytest.mark.num_cards(0)
def test_list_owner_and_state(cards_db):
    cards = [
        Card(summary='foo',owner='Alex',state='todo'),
        Card(summary='foo',owner='Alex',state='done'),
        Card(summary='foo',owner='Rex',state='done'),
    ]
    for c in cards:
        cards_db.add_card(c)
    lst = cards_db.list_cards(owner='Alex',state='done')
    assert len(lst) == 1 and lst[0].owner == 'Alex' and lst[0].state=='done'