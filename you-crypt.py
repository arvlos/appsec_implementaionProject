# you-crypt.py
# Created May 1, 2016 by Artem V. Losev

# Created as a part of the Implementation Project assignment for
# 	Application Security class at NYU Tandon School of Engineering

import sys
from Crypto.Cipher import AES
from Crypto import Random 
from Crypto.Util import Counter

# The database file name
DB_FILE_NAME = "storage.txt"

# The encryption key file name
KEY_FILE_NAME = "key.txt"

# The counter for the CTR mode
COUNTER = Counter.new(128)

# Generates a 16-byte AES key and stores it in a @filename
# 	If the file exists, retrieves the stored key
def generateKey(filename):

	# Check if the file exists, if not - create it
	while True:
		try:
			file = open(filename, "r")
			break
		except IOError:
			file = open(filename, "w")
			key = Random.new().read(AES.block_size)
			file.write(key + "\n")
			file.close()
			return key

	key = file.read(AES.block_size)
	file.close()
	return key



# Encrypts the provided @string using the encryption @mode specified
def encryptStr(string, mode):

	# Standartize string for 16-byte block size for AES
	spaces = 16 - (len(string) % 16)
	if spaces != 16:
		while spaces != 0:
			string += " "
			spaces = spaces-1

	# Generate key and store it in a file
	key = generateKey(KEY_FILE_NAME)

	# Generate the iv for AES
	iv = Random.new().read(AES.block_size)

	# Create the appropriate cipher object
	if mode.upper() == "CBC":
		cipher = AES.new(key, AES.MODE_CBC, iv)
	elif mode.upper() == "ECB":
		cipher = AES.new(key, AES.MODE_ECB)
	elif mode.upper() == "CTR":
		cipher = AES.new(key, AES.MODE_CTR, counter=COUNTER)
	else:
		print "Error, the specified mode is invalid."
		sys.exit()

	# Encrypt the string
	passEncr = iv + cipher.encrypt(string)
	return passEncr

# Decrypts the provided @string using the decryption @mode specified
def decryptStr(string, mode):

	# Retrieve the appended iv
	iv = string[:16]

	# Get the generated key from a file
	key = generateKey(KEY_FILE_NAME)

	# Create the appropriate cipher object
	if mode.upper() == "CBC":
		cipher = AES.new(key, AES.MODE_CBC, iv)
	elif mode.upper() == "ECB":
		cipher = AES.new(key, AES.MODE_ECB)
	elif mode.upper() == "CTR":
		cipher = AES.new(key, AES.MODE_CTR, counter=COUNTER)
	else:
		print "Error, the specified mode is invalid."
		sys.exit()

	# Decrypt the string
	plainText = cipher.decrypt(string[16:])
	return plainText


		
# Opens the @filename and writes (@login, @password) to it
def writeToFile(filename, login, password):
	file = open(filename, "a")	# Open in append mode
	file.write("(" + login + ", " + password + ")\n")
	file.close()


# Search the @filename for @login, then compare its @password
def searchFile(filename, login, password, mode):
	# Equalizes the password to 16-block dividable string for comparison
	spaces = 16 - (len(password) % 16)
	if spaces != 16:
		while spaces != 0:
			password += " "
			spaces = spaces-1

	# Check if the file exists, if not - create it
	while True:
		try:
			file = open(filename, "r")
			break
		except IOError:
			file = open(filename, "w")
			file.close()
			return False

	loginStr = "(" + login + ", "
	
	# Search
	for line in file:
		# Login found
		if loginStr in line:

			passEncr = line[line.find(", ")+2:line.find(")")]
			passStr = decryptStr(passEncr, mode)
			if passStr == password:
				print "Correct password."
			else:
				print "The username exists, the password is incorrect."
			file.close()
			return True

	file.close()
	return False



# The main function of the app
if __name__ == "__main__":

	if len(sys.argv) != 4:
		print "Usage: python you-crypt.py <name> <password> <encryption_mode (ECB, CTR or CBC)>"
		sys.exit()

	# If the file is found, the app gets terminated, else writes the new pair to the file
	if searchFile(DB_FILE_NAME, sys.argv[1], sys.argv[2], sys.argv[3]) == False:
		print "The username doesn't exist; a new pair will be created."
		encryptedPassword = encryptStr(sys.argv[2], sys.argv[3])
		writeToFile(DB_FILE_NAME, sys.argv[1], encryptedPassword)

