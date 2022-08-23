def test_count_from_empty(cards_cli,cards_db):
    assert cards_cli('count') == '0'

def test_count_from_one_item(cards_cli,cards_db):
    cards_cli('add some task')
    assert cards_cli('count') == '1' 

def test_count_from_many_items(cards_cli,cards_db):
    cards_cli('add one item')
    cards_cli('add two item')
    cards_cli('add three item')
    assert cards_cli('count') == '3'

