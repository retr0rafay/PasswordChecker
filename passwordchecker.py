import requests
import hashlib
import sys


def request_api_data(query_char):
    password_api_url = 'https://api.pwnedpasswords.com/range/' + query_char
    password_api_response = requests.get(password_api_url)
    if password_api_response.status_code != 200:
        raise RuntimeError(f'Error Fetching: {password_api_response.status_code}, check the API and try again.')
    return password_api_response


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if hash_to_check == h:
            return int(count)
    return 0


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_five_chars, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first_five_chars)
    return get_password_leaks_count(response, tail)


def main(args):
    passwords = input('Enter some passwords to check if they have been leaked. Make sure to separate each password '
                      'with a space.\n').split()
    for pw in passwords:
        number_of_leaks = pwned_api_check(pw)
        if number_of_leaks == 0:
            print(f'Password {pw} is good!')
        else:
            print(f'Oh no! Your password {pw} has been leaked {number_of_leaks} times! Please change it ASAP!')


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
