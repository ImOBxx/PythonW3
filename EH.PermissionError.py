import os

# Step 1: Create a text file
file_path = 'test.txt'
with open(file_path, 'w') as f:
    f.write('This is a test file.')

# Step 2: Change the file permissions to deny access
# Remove read and write permissions for the owner (user)
os.chmod(file_path, 0o000)

# Verify the permission change
try:
    f = open(file_path)
except PermissionError as e:
    print(e)
finally:
    print("The Code Is Executed.")
