from typing import List
from pyfrost.network.abstract import DataManager
from sqlalchemy import create_engine, Column, String, Integer, MetaData, Table
from sqlalchemy import insert, select, update, delete
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.exc import OperationalError
import json
import time


class NodeDataManager(DataManager):
    def __init__(self, max_retries=3) -> None:
        super().__init__()
        self.__engine = create_engine(f'sqlite:///node.db')
        self.__session_factory = sessionmaker(bind=self.__engine)
        self.__Session = scoped_session(self.__session_factory)
        self.__max_retries = max_retries
        self.__tables = {}
        metadata = MetaData()
        self.__tables['dkg_list'] = Table('dkg_list', metadata,
                                          Column('key', String(80),
                                                 primary_key=True),
                                          Column('value', String(10000)))
        self.__tables['nonces'] = Table('nonces', metadata,
                                        Column('key', Integer,
                                               primary_key=True),
                                        Column('value', String(10000)))
        metadata.create_all(self.__engine)

    def __execute_command(self, exec_obj):
        retries = 0
        while retries < self.__max_retries:
            try:
                session = self.__Session()
                session.execute(exec_obj)
                session.commit()
                break
            except OperationalError as e:
                session.rollback()
                retries += 1
                time.sleep(0.1)  # A short delay between retries
            finally:
                session.close()
        if retries == self.__max_retries:
            raise Exception(f"Max retries reached for operation {exec_obj}")

    def set_nonces(self, nonces_list: List) -> None:
        self.__save_data('nonces', 1, json.dumps(nonces_list))

    def get_nonces(self):
        nonces = self.__get_data('nonces', 1)
        result = []
        for nonce in nonces:
            modified_nonce = nonce.copy()
            modified_nonce['nonce_d_pair'] = {
                int(key): value for key, value in nonce['nonce_d_pair'].items()}
            modified_nonce['nonce_e_pair'] = {
                int(key): value for key, value in nonce['nonce_e_pair'].items()}
            result.append(modified_nonce)
        return result

    def set_key(self, key, value) -> None:
        self.__save_data('dkg_list', key, json.dumps(value))

    def get_key(self, key):
        return self.__get_data('dkg_list', key)

    def __save_data(self, table_name: str, key, value) -> None:
        table = self.__tables.get(table_name)
        data = self.__get_data(table_name, key)
        exec_obj = None
        if data != []:
            exec_obj = update(table).values(value=value)\
                .where(table.c.key == key)
        else:
            exec_obj = insert(table)\
                .values(key=key, value=value)

        self.__execute_command(exec_obj)

    def __get_data(self, table_name: str, key):
        table = self.__tables.get(table_name)
        data = None
        if table is not None:
            connection = self.__engine.connect()
            select_obj = select(table)\
                .where(table.c.key == key)
            data = connection.execute(select_obj).fetchone()
            if data is not None:
                data = json.loads(data[1])  # value of the data
            else:
                data = []
            connection.close()
        return data
