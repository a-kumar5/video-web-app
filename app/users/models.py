import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
import validators
from app.config import settings
from passlib.context import CryptContext

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return bcrypt_context.hash(password)


def verify_password(plain_password: str, hashed_password) -> True | Exception:
    return bcrypt_context.verify(plain_password, hashed_password)


class User(Model):
    __keyspace__ = settings.ASTRADB_KEYSPACE
    email: str = columns.Text(primary_key=True)
    user_id = columns.UUID(primary_key=True, default=uuid.uuid1)
    password: str = columns.Text()

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f"User(email={self.email}, user_id={self.user_id}"

    @staticmethod
    def create_user(email, password=None):
        query = User.objects.filter(email=email)
        if query.count() != 0:
            raise Exception("User already has account.")
        valid, msg, email = validators._validate_email(email=email)
        if not valid:
            raise Exception(f"Invalid email: {msg}")
        obj = User(email=email)
        obj.password = get_password_hash(password=password)
        obj.save()
        return obj
