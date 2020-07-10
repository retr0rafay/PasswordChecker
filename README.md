# PasswordChecker Overview

Are you curious to know whether your passwords have been compromised? If you are, then this Password Checker program will check how many times your password has been leaked.
If your passwords haven't been leaked, then good job! It is always best to have strong passwords that way no one can try to guess them. Just so you know, when you run the program,
you actually won't be sending your passwords over the web. Instead, a hashed version (sha1) password will be sent and it's only the first 5 characters of the sha1 password that will
be sent over the web for security reasons. Companies like Google, Salesforce and Netflix use hashing to store hashed passwords in databases, that way no one is able to see someone's real
password. Now that I've given you a little background over hashing, let's go over how to run this program.

## Instructions
- Download this program on your computer
- Open up your terminal, go to the program's location and run `python3 passwordchecker.py`
- Enter the passwords you would like to check and make sure that if you are entering multiple passwords, they are divided by a space
  - For example, if you wanted to check for three passwords, you can write something like `abcde 12345 iAmAwesome!`
- Press the Enter or return key on your keyboard and see the magic happen!
