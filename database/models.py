from peewee import *
from config import DB_NAME, DB_USER, DB_HOST, DB_PASSWORD, DB_PORT

# db = PostgresqlDatabase(DB_NAME, user=DB_USER, host=DB_HOST, password=DB_PASSWORD, port=DB_PORT)
db = SqliteDatabase("users.db")


class BaseModel(Model):
    class Meta:
        database = db


class Users(BaseModel):
    user_id = BigIntegerField(primary_key=True)
    username = CharField(max_length=200, null=True)
    full_name = CharField(max_length=200, null=True)
    score = IntegerField(default=0)
    procent = FloatField(default=0)

    class Meta:
        db_name = 'users'


class Tests(BaseModel):
    test_name = CharField(max_length=200)
    test_code = CharField(max_length=200, null=True)
    tests = TextField()

    class Meta:
        db_name = 'tests'



