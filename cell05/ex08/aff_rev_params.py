import sys
if len(sys.argv) > 2:
    for i in sys.argv[:0:-1]:
        print(i)
else:
    print('none')
sys.exit(0)