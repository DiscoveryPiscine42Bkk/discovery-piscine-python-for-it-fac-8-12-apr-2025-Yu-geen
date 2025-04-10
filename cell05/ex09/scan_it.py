import sys

if len(sys.argv) > 1:

    keyword = sys.argv[1]
    string = sys.argv[2]
    print(string.count(keyword))

else:

    print('none')

sys.exit(0)
