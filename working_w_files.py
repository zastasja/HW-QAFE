# open & close file without linespaces:
with open("hello_world.txt") as text:
    for line in text:
	    print(line.strip())
# "write only" = w, "read" = r, "append" = a, "read and write" = r+ 
with open("hello_world.txt", "a") as file:
    file.write("some extra text")

#removes file
import os
os.remove("hello_world.txt")

#rename file
os.rename("firstname.txt", "changed_name.txt")

# checking if file exists, return boolean
os.path.exists("changed_name.txt")

#returns file size in bites
os.path.getsize("changed_name.txt")

# last time changed
import datetime
timestamp = os.path.getmtime("changed_name.txt")
datetime.datetime.fromtimestamp(timestamp)

# gets absolute path of the file
file_path = os.path.abspath("changed_name.txt")

# get current location directory (same as pwd)
print(os.getcwd())
# make directory
os.mkdir("folder_name")
# change directory / cd
os.chdir("folder_name")
#make and remove
os.mkdir("folder_name")
os.rmdir("folder_name")

# reading csv file
import csv

file = open("csv_text.txt")
csv_f = csv.reader(file)
for row in csv_f:
  name, phone, role = row
  print(f'Name: {name}, Phone: {phone}, Role: {role}')
file.close()


