import os
import sys

from sqlalchemy import Column, Integer, String

try:
    from compare_project.settings import Engine, Base
except ImportError:
    sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
    from compare_project.settings import Engine, Base


class UsdJpy(Base):
    __tablename__ = 'sqlalchemy_model_usdjpy'
    id = Column(Integer, primary_key=True, autoincrement=True)
    time_stamp = Column('time_stamp', String(128))
    usd_jpy = Column('usd_jpy', String(128))


def main():
    Base.metadata.create_all(bind=Engine)


if __name__ == '__main__':
    main()
