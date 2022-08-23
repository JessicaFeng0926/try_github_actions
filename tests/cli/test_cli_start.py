import pytest 
from cards import Card

@pytest.mark.parametrize(
    'start_state',
    ['todo', 'in prog', 'done']
)
def test_start(cards_cli,cards_db,start_state):
    i = cards_db.add_card(Card('some task',state=start_state))
    cards_cli(f'start {i}')
    assert cards_db.get_card(i).state == 'in prog'

def test_start_with_invalid_id(cards_cli,cards_db):
    i = 123
    output = cards_cli(f'start {i}')
    assert 'Error' in output 

    
