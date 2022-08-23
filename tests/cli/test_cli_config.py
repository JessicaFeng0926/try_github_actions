def test_config_path(cards_db,cards_cli,db_path):
    result = cards_cli('config')
    assert result == str(db_path)