from enum import Enum
from abc import ABC, abstractmethod

class Databases(Enum):
    REDIS = 'REDIS'
    MYSQL = 'MYSQL'
    SQLITE = 'SQLITE'
    MONGO = 'MONGO'
    DYNAMO = 'DYNAMO'

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class Redis(Database):
    def connect(self):
        print('Connecting into Redis database')

class MySQL(Database):
    def connect(self):
        print('Connecting into MySQL database')


class SQLite(Database):
    def connect(self):
        print('Connecting into SQLite database')

class Mongo(Database):
    def connect(self):
        print('Connecting into Mongo database')

class Dynamo(Database):
    def connect(self):
        print('Connecting into Dynamo database')


class DatabaseFactory(ABC):
    @abstractmethod
    def get_client(self, engine: Databases):
        pass

class SQLFactory(DatabaseFactory):
    def get_client(self, engine: Databases):
        if engine == Databases.MYSQL:
            return MySQL()
        elif engine == Databases.SQLITE:
            return SQLite()
        else:
            raise Exception(f'SQLFactory do not interface with {engine}')

class NoSQLFactory(DatabaseFactory):
    def get_client(self, engine: Databases):
        if engine == Databases.MONGO:
            return Mongo()
        elif engine == Databases.DYNAMO:
            return Dynamo()
        else:
            raise Exception(f'NoSQLFactory do not interface with {engine}')

class CacheDBFactory(DatabaseFactory):
    def get_client(self, engine: Databases):
        if engine == Databases.REDIS:
            return Redis()
        else:
            raise Exception(f'CacheDBFactory do not interface with {engine}')
        
client = CacheDBFactory().get_client(Databases.REDIS)
client.connect()

client = SQLFactory().get_client(Databases.MYSQL)
client.connect()

client = SQLFactory().get_client(Databases.SQLITE)
client.connect()

client = NoSQLFactory().get_client(Databases.MONGO)
client.connect()

client = NoSQLFactory().get_client(Databases.DYNAMO)
client.connect()