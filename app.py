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
	storage = open(filename, "a")
	storage.write("(" + login + ", " + password + ")\n")
	storage.close()


# The main function of the app
if __name__ == "__main__":

	if len(sys.argv) != 4:
		print "Usage: python app.py <name> <password> <encryption_mode>"


	writeToFile(FILE_NAME, sys.argv[1], sys.argv[2])

