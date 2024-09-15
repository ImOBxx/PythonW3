# r = read mode
# w : write mode
# a : append mode

fileObj = open("Stuname.txt","r")
fileObj.seek(2)

data = fileObj.read()

print(data)