from typer.testing import CliRunner 
from cards.cli import app
from cards import Card





def test_add_only_summary(cards_cli,cards_db):
    cards_cli('add some task')
    expected = Card('some task',owner='',state='todo')
    all_cards = cards_db.list_cards()
    assert len(all_cards) == 1
    assert all_cards[0] == expected 

def test_add_owner_and_summary(cards_cli,cards_db):
    cards_cli('add some task -o brian')
    expected = Card('some task', owner='brian',state='todo')
    all_cards = cards_db.list_cards()
    assert len(all_cards) == 1
    assert all_cards[0] == expected 

def test_add_no_summary(cards_cli,cards_db):
    output = cards_cli('add')
    assert 'Error' in output 

def test_add_duplicate_card(cards_cli,cards_db):
    '''预计可以重复添加Card 并且会得到不同的id'''
    cards_cli('add some task')
    cards_cli('add some task')
    all_cards = cards_db.list_cards()
    assert len(all_cards) == 2
    assert all_cards[0].id != all_cards[1].id 