import pytest 
from cards import Card, InvalidCardId

@pytest.mark.num_cards(3)
def test_delete_from_many_items(cards_db):
    i = cards_db.add_card(Card(summary="write a book"))
    cards_db.delete_card(i)
    with pytest.raises(InvalidCardId):
        c = cards_db.get_card(i)


@pytest.mark.num_cards(0)
def test_delete_from_one_item(cards_db):
    i = cards_db.add_card(Card(summary="write a book"))
    cards_db.delete_card(i)
    assert cards_db.count() == 0

@pytest.mark.num_cards(0)
def test_delete_with_invalid_id(cards_db):
    i = 123
    with pytest.raises(InvalidCardId):
        cards_db.delete_card(i)
