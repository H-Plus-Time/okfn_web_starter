from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:////tmp/test.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def safe_add(args):
    try:
        db_session.add(args)
        db_session.commit()
    except:
        db_session.rollback()

def safe_val(attr_dict, key):
    if key in attr_dict.keys():
        return attr_dict[key]
    else:
        return None

def result_to_json(query_result):
    return map(lambda x : x.to_json(), query_result)

def init_db():
    import models
    Base.metadata.create_all(bind=engine)