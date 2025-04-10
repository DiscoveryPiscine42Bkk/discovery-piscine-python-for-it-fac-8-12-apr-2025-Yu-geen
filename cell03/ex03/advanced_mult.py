num1 = 0
num2 = 0

while num1 <= 10:
    print(f'Table de {num1}:',end='')

    while num2 <= 10:
        print(f' {num1 * num2}',end='')
        num2 += 1

    num2 = 0
    num1 += 1
    print()
