import pytest 
import cards 
from cards.cli import app
from typer.testing import CliRunner

@pytest.fixture(scope='session')
def db_path(tmp_path_factory):
    return tmp_path_factory.mktemp('sub')

@pytest.fixture(scope='session')
def db(db_path):
    db_ = cards.CardsDB(db_path)
    yield db_ 
    db_.close()

@pytest.fixture()
def cards_db(db,monkeypatch,db_path):
    # 一定要把原来的数据库路径覆盖一下 
    # 不然通过命令行添加Card对象就不是添加到同一个数据库里
    monkeypatch.setenv('CARDS_DB_DIR',str(db_path))
    db.delete_all()
    return db 

runner = CliRunner()

@pytest.fixture()
def cards_cli():
    def inside(command_string):
        command_list = command_string.split()
        result = runner.invoke(app,command_list)
        return result.stdout.rstrip()
    return inside

