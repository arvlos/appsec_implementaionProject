# <name>

<name> is a tiny command-line application written in Python that was created as an Implementation Project for the Application Security class at NYU Tandon School of Engineering.
<name> has the following features:
- Given a (username, password) pair in ASCII, stores the pair in a file;
- Given a (username, password) pair in ASCII, checks the db file for the username:
	* If the username is found, compares the password to the stored one
	* If the username is not found, creates a new entry with the specified password
- The user provides the flag for the mode of encryption to be used on his stored password
	* The encryption is implemented with AES algorithm provided by the PyCrypto package
	* Supported modes are CBC, ECB and CTR

Here's the usage example for <name>:
`python <name>.py <username> <password> <mode_of_encryption>`


## Installation 
### Required packages
The following dependencies are required and must be installed separately:
- [Python 2.7](https://www.python.org/downloads/)
- [PyCrypto 2.6](https://www.dlitz.net/software/pycrypto/)

## Author
Created by Artem V Losev
May 2016