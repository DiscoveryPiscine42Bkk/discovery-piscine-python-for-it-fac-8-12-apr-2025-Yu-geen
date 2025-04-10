import sys

if len(sys.argv) > 1:
    for i in sys.argv:
        if not "ism" in i:
            print(i+'ism')

else:

    print('none')

sys.exit(0)