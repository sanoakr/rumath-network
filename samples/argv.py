# argv.py
import sys

args = sys.argv

argc = len(args)
print('args =',args)
print('len(args) =', argc)

for i in range(argc):
    print('args[{0}] = {1}'.format(i, args[i]))
