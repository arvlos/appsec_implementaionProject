# You-Crypt

**You-Crypt** is a tiny command-line application written in Python that was created as an Implementation Project for the Application Security class at NYU Tandon School of Engineering.

**You-Crypt** has the following features:
- Given a (username, password) pair in ASCII, stores the pair in a file;
- Given a (username, password) pair in ASCII, checks the db file for the username:
	* If the username is found, compares the password to the stored one;
	* If the username is not found, creates a new entry with the specified password;
- The user provides the flag for the mode of encryption to be used on his stored password:
	* The encryption is implemented with AES algorithm provided by the PyCrypto package;
	* Supported modes are CBC, ECB and CTR;

Here's the usage example for `you-crypt`:

`python you-crypt.py <username> <password> <mode_of_encryption>`

## Program operation
**You-Crypt** requires the user to provide the username, password and the encryption mode (CBC, ECB or CTR) as command-line arguments. No sophisticated error-checking is implemented besides the number of arguments and the correctness of the encryption mode. Then the app reads (or creates) the storage file to write the (login, encrypted_password) pair to; it encrypts the password using the AES algorithm in the mode specified by the user; the generated encryption key is stored in plaintext in a separate text file. A randomly generated 16-byte IV is appended to the front of the encrypted password and the result is stored alongside the plaintext login.

If the provided username already exists in the database text file, the application will perform decryption of the stored password using the mode _specified by the user_ and compare the result to the provided plaintext password.

**Attention:** if the user stores his password using one mode, and then attempts to match it using a different mode, the app will fail to recognize the provided password. Thus, only the correct login, password _and_ mode of encryption will get recognized as correct.

## Installation 
### Required packages
The following dependencies are required and must be installed separately:
- [Python 2.7](https://www.python.org/downloads/)
- [PyCrypto 2.6](https://www.dlitz.net/software/pycrypto/)

## Author
Created by Artem V Losev

May 2016