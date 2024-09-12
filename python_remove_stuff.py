import os

try_create_file = os.system('echo hello > test.txt') 

if try_create_file == 0:
    res = os.system('del test.txt')

print(res)