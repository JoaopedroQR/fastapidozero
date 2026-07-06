from dataclasses import asdict
from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    new_user = User(username='test', email='test@test.com', password='secret')

    session.add(new_user)
    session.commit()

    user = session.scalar(
        select(User).where(User.username == 'test')
    )

    # assert user.password == 'secret'
    assert asdict(user) == {
        id: 1,
        'username': 'test',
        'email': 'test@test.com',
        'password': 'secret',
        'created_at': ...
    }
