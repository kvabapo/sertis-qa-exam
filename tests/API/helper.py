import requests
import json

BASE_URL = "https://sertis-qa.glitch.me"


def get_list_of_users():

    url = BASE_URL + "/user/ids"
    response = requests.get(url)
    return response


def get_user_by_id():
    id = get_list_of_users().json()
    url = BASE_URL + "/user/" + id[0]  # 001
    response = requests.get(url)
    return response


def sign_in_user(phone=get_user_by_id().json()["phone_no"],
                 otp=get_user_by_id().json()["otp"]):

    url = BASE_URL + "/signin"
    headers = {"accept": "application/json",
               "Content-Type": "application/json"}
    payload = {"phone_no": phone, "otp": otp}
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response
