import pytest 
from cards import Card

@pytest.mark.parametrize(
    'start_state',
    ['todo', 'in prog', 'done']
)
def test_finish(cards_cli,cards_db,start_state):
    i = cards_db.add_card(Card('some task',state=start_state))
    cards_cli(f'finish {i}')
    card = cards_db.get_card(i)
    assert card.state == 'done'

def test_finish_with_invalid_id(cards_cli,cards_db):
    i = 123
    output = cards_cli(f'finish {i}')
    assert 'Error' in output