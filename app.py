# app.py
# Created May 1, 2016 by Artem V. Losev

# Created as a part of the "Implementation Project" assignment for
# 	Application Security class at NYU Tandon School of Engineering


import sys
from Crypto.Cipher import AES
from Crypto import Random 


# The database file name
DB_FILE_NAME = "storage.txt"

# The encryption key file name
KEY_FILE_NAME = "key.txt"

# Generates a 16-byte AES key and stores it in a file
# 	If the file exists, retrieves the stored key
def generateKey(filename):

	while True;
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


	

# Function that opens the specified file in the append mode 
# 	and writes the provided strings to it
def writeToFile(filename, login, password):
	file = open(filename, "a")
	file.write("(" + login + ", " + password + ")\n")
	file.close()


# Function that opens the specified file in the read mode 
# 	and searches for the login provided. 
# 	If the login is found, it checks the password as well.
# 	Returns True if login is found, False otherwise
def searchFile(filename, login, password):

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
	passStr = ", " + password + ")"
	for line in file:
		if loginStr in line:
			if passStr in line:
				print "Correct password."
			else:
				print "The username exists, the password is incorrect."
			file.close()
			return True

	file.close()
	return False



# The main function of the app
if __name__ == "__main__":

	if len(sys.argv) != 3:
		print "Usage: python app.py <name> <password> <encryption_mode>"
		sys.exit()

	if searchFile(DB_FILE_NAME, sys.argv[1], sys.argv[2]) == False:
		print "The username doesn't exist; a new pair will be created."
		writeToFile(DB_FILE_NAME, sys.argv[1], sys.argv[2])

