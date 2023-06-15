# Using os to do things

import os

# Echo to the terminal
# os.system('echo "Hello World!')
#
# # make and change directories
#
# #create a directory

#directory name
directory = "test_dir"
#parent directory name
parent_dir = "C:/Users/krzyd"
#path
path = os.path.join(parent_dir, directory)

# #create directory
# os.mkdir(path)

# Putting a new file in the new dir

filename = "testfile.txt"
filepath = os.path.join(path, filename)

# putting content in the file
with open(filepath, "w") as file1:
    toFile = "Contents of file is written here"
    file1.write(toFile)


