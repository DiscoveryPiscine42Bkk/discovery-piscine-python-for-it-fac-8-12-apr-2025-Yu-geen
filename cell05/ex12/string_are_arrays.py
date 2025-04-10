import sys

if len(sys.argv) > 1 and 'z' in sys.argv[1] :
    z = sys.argv[1].count('z')
    print('z' *z)

else:

    print('none')

sys.exit(0)