import requests
import hashlib


def request_api_data(query_char):
    password_api_url = 'https://api.pwnedpasswords.com/range/' + query_char
    password_api_response = requests.get(password_api_url)
    if password_api_response.status_code != 200:
        raise RuntimeError(f'Error Fetching: {password_api_response.status_code}, check the API and try again.')
    return password_api_response


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    return sha1password

