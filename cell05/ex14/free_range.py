import sys

if len(sys.argv) > 2:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2] )
    print([ i for i in range(num1,num2+1)])

else:

    print('none')

sys.exit(0)