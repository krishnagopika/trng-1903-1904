import os

if os.path.exists("week-1\sample file.txt"):
    os.remove("week-1\sample file.txt")

try:
    os.remove("week-1\sample file.txt")
except Exception as e:
    print("File not found")



# returns a file object
f = open("week-1\sample file.txt", "r+", encoding="utf-8")


f.write("Hello")

# return a string till the /n
f.readline()


# returns the list of lines in the file
for i in f.readlines():
    print(i, end=" ")


with open("week-1\SampleText.txt", "r+", encoding="utf-8") as f:
    for i in f.read():
        print(i, end="")

print(f.closed)



print(f.seek(4))






    

