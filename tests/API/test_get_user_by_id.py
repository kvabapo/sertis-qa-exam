
from helper import get_user_by_id


def test_get_user_by_id():
    response = get_user_by_id()
    assert response.status_code == 200
