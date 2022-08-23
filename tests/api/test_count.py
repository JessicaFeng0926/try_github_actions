import pytest 


@pytest.mark.num_cards(0)
def test_count_from_empty(cards_db):
    assert cards_db.count() == 0


@pytest.mark.num_cards(1)
def test_count_from_one_item(cards_db):
    assert cards_db.count() == 1

@pytest.mark.num_cards(3)
def test_count_from_three_items(cards_db):
    assert cards_db.count() == 3