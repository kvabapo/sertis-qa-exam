
from helper import *


def test_get_list_of_users():
    response = get_list_of_users()
    assert response.status_code == 200
