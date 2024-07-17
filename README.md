# py_password
Generates a strong password

## Usage
$ python main.py [--length # | -l #]

Use the --length or -l to define the password legnth.  If unset the length will be 8 characters.  The minimum the tool allows is 4 characters.

The password is guarenteed to have at least 1 of the following characters:

* lower case alpha (a-z)
* upper case alpha (A-Z)
* numeric (0-9)
* special character (!@#$%^&*{}[],.?:;)

The password will be printed to stdout.
