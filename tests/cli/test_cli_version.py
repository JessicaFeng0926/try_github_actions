import cards 


def test_version1(cards_cli):
    output = cards_cli('version')
    assert output == cards.__version__