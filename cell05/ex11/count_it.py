import sys

if len(sys.argv) > 0:
    print(f'parameters: {len(sys.argv)-1}')
    for i in sys.argv[1::]:
        print(f'{i}: {len(i)}')
else:

    print('none')

sys.exit(0)
