word = input()

for i in word:
    if i.islower():
        print(i.upper(),end='')
    elif i.isupper():
        print(i.lower(),end='')
    else:
        print(i,end='')