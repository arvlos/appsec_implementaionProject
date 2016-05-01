# app.py
# Created May 1, 2016 by Artem V. Losev
# Created as a part of the "Implementation Project" assignment for
# 	Application Security class at NYU Tandon School of Engineering


import sys

# The storage file filename
FILE_NAME = "storage.txt"

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
	file = open(filename, "r")
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

	if searchFile(FILE_NAME, sys.argv[1], sys.argv[2]) == False:
		print "The username doesn't exist, so a new one will be created."
		writeToFile(FILE_NAME, sys.argv[1], sys.argv[2])

