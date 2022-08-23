import cards 


def test_config_path(monkeypatch,capsys,tmp_path):
    def fake_get_path():
        return tmp_path 
    
    monkeypatch.setattr(cards.cli,'get_path',fake_get_path)
    cards.cli.config()
    output = capsys.readouterr().out.rstrip()
    assert output == str(tmp_path)



