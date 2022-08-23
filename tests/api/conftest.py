import pytest
import cards 


@pytest.fixture(scope='session')
def db(tmp_path_factory):
    db_ = cards.CardsDB(tmp_path_factory.mktemp("sub"))
    yield db_ 
    db_.close()

@pytest.fixture(scope='function')
def cards_db(db,request,faker):
    # 先清空
    db.delete_all()
    # 根据用户使用marker传入的数字往数据库添加Card对象
    marker = request.node.get_closest_marker("num_cards")
    if marker and len(marker.args)>0:
        for _ in range(marker.args[0]):
            db.add_card(cards.Card(summary=faker.sentence(),owner=faker.first_name()))
        
    return db 