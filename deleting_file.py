f = open("file_3.txt","w");
f.write("This file is created for deletion purpose");
f.close();

#Deleting a File
#Module (like a code library) is a file written by another programmer that generally has a functions we can use.

import os;
os.remove("file_3.txt");