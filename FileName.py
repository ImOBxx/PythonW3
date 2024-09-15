filename = input ("Input The File Name: ")
f_extns = filename.split(".")
print ("The extension of the files is: " + repr(f_extns[-1]))