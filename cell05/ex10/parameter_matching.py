import sys

if len(sys.argv) > 0:
    word = input('What was the parameter? ')
    if word == sys.argv[1]:
        print('Good job!')
    else:
        print('Nope, sorry...')

else:

    print('none')

sys.exit(0)
