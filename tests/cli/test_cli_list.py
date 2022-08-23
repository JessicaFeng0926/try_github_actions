from cards import Card

def test_list_from_empty(cards_cli,cards_db):
    # 即使没有记录 也会打印一个空行、表头和一条线
    output = cards_cli('list')
    lst = output.split('\n')
    assert len(lst) == 3

def test_list_from_non_empty(cards_cli,cards_db):
    cards_db.add_card(Card('task 1'))
    cards_db.add_card(Card('task 2'))
    cards_db.add_card(Card('task 3'))
    output = cards_cli('list')
    lst = output.split('\n')
    assert len(lst) == 6
    assert 'task 1' in lst[3]
    assert 'task 2' in lst[4]
    assert 'task 3' in lst[5] 

def test_list_with_owner(cards_cli,cards_db):
    cards = [
        Card(summary='foo',owner='Alex'),
        Card(summary='foo',owner='Julie'),
        Card(summary='foo',owner='Rex'),
    ]
    for c in cards:
        cards_db.add_card(c)
    output = cards_cli('list -o Julie')
    lst = output.split('\n')
    assert len(lst) == 4
    assert 'Julie' in lst[-1]

