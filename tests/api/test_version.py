import cards 


def test_version_case(capsys):
    cards.cli.version()
    assert capsys.readouterr().out.rstrip() == cards.__version__