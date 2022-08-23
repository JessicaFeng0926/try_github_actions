from cards import Card, InvalidCardId

def test_update_owner(cards_cli,cards_db):
    i = cards_db.add_card(Card('some task',owner='Brian'))
    cards_cli(f'update {i} -o Alex')
    card = cards_db.get_card(i)
    assert card.summary == 'some task'
    assert card.owner == 'Alex'

def test_update_summary(cards_cli,cards_db):
    i = cards_db.add_card(Card('some task',owner='Brian'))
    cards_cli(f'update {i} -s new_task')
    card = cards_db.get_card(i)
    assert card.summary == 'new_task'
    assert card.owner == 'Brian'

def test_update_owner_and_summary(cards_cli,cards_db):
    i = cards_db.add_card(Card('some task',owner='Brian'))
    cards_cli(f'update {i} -s new_task -o Alex')
    card = cards_db.get_card(i)
    assert card.summary == 'new_task'
    assert card.owner == 'Alex'

def test_update_with_invalid_id(cards_cli,cards_db):
    i = 123
    output = cards_cli(f'update {i} -o alex')
    assert 'Error' in output 


