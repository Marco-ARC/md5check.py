import argparse
import hashlib

# part of this ccode is from https://linuxhint.com/add_command_line_arguments_to_a_python_script/
parser = argparse.ArgumentParser(description='A python MD5 checker and verifier')

#add -f and -v as command line arguments to supply file location and md5 to verify against
parser.add_argument("-f", "--file_location", help="specifies location of the file to check.")
parser.add_argument("-v", "--varify", help="verifies the file's md5 is the same as the one provided.")

args = parser.parse_args()


file = args.file_location
md5_check = args.varify

# this folowing block of code is from user HAL9000 on https://stackoverflow.com/questions/16874598/how-do-i-calculate-the-md5-checksum-of-a-file-in-python
# Open,close, read file and calculate MD5 on its contents 
with open(file, 'rb') as file_to_check:
    # read contents of the file
    data = file_to_check.read()    
    # pipe contents of the file through
    md5_returned = hashlib.md5(data).hexdigest()


if md5_check != None:               # check that the user provided an MD5 hash to check ahgainst
    if md5_check == md5_returned:   # if so, check that the MD5 is correct
        print("MD5 verified.")
    else:
        print("MD5 verification failed!.")
else:                               # if not, print the md5 hash of the file
    print(md5_returned)