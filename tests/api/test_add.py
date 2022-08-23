import pytest 
from cards import Card

@pytest.mark.num_cards(0)
def test_add_only_summary_empty_database(cards_db):
    i = cards_db.add_card(Card(summary="write a book"))
    c = cards_db.get_card(i)
    assert c.summary == 'write a book'

@pytest.mark.num_cards(3)
def test_add_only_summary_non_empty_database(cards_db):
    i = cards_db.add_card(Card(summary="write a book"))
    c = cards_db.get_card(i)
    assert c.summary == 'write a book'

@pytest.mark.num_cards(0)
def test_add_owner_and_summary(cards_db):
    i = cards_db.add_card(Card(summary="write a book",owner='Alex'))
    c = cards_db.get_card(i)
    assert c.summary == 'write a book' and c.owner == 'Alex'

@pytest.mark.num_cards(0)
def test_add_no_summary(cards_db):
    with pytest.raises(Exception):
        cards_db.add_card(Card())

@pytest.mark.num_cards(0)
def test_add_duplicate_card(cards_db):
    '''预计可以重复添加Card 并且会得到不同的id'''
    c = Card(summary="write a book")
    i1 = cards_db.add_card(c)
    i2 = cards_db.add_card(c)
    assert len(cards_db.list_cards()) == 2
    assert i1 != i2




    

