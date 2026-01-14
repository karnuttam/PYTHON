#File I/O in Python
#Python can be used to perform operations on a file.(read and write data)
#Types of all files
#1.Text Files: .txt, .docx, .log etc.
#2.Binary Files: .mp4,.mov,.png, .jpeg etc.

f = open("file_1.txt", "r");#open in read line
#data = f.read();
#print(data);
#print(type(data));
char = f.read(5);
print(char);
line_1 = f.readline();
print(line_1);
f.close();

'''
Character            Meaning
'r'                  Open for reading (default)
'w'                  Open for writing, truncating the file first
'x'                  Create an new file and open it for writing
'a'                  Open for writing, appending to the end of the file if it exists
'b'                  Binary mode
't'                  text mode (default)
'+'                  Open a disk file for updating (reading and writing)
'r+'                 read + overwrite (pointer at starting) - no truncate
'w+'                 read + overwrite - truncate
'a+'                 read + append (pointer at end) - no truncate
'''
f = open("file_1.txt", "a");
f.write("This is the best language for beginners.");
f.close();

#with Syntax
with open("file_2.txt", "r") as f:
    data = f.read();
    print(data);
f.close();

def check_for_line():
    word = "Python";
    data = True;
    line_no = 1;
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline();
            if(word in data):
                print(line_no);
            return;
        line_no = line_no + 1;

check_for_line();