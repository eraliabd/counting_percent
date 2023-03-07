# import uuid
# print(str(uuid.uuid4()).split('-')[-1])

# import random
# guess_number = random.randint(1, 100)
# print("The number you guessed: ", guess_number)
# # bool_number = True
# while True:
#     n = int(input("Taxmin qilgan sonningizni kiriting: "))
#     if n > guess_number:
#         print("Juda baland!")
#     elif n < guess_number:
#         print("Juda past!")
#     else:
#         # bool_number = False
#         print("Taxmin qilgan soningiz to'g'ri!")
#         break

n = int(input("Enter a number: "))
i = 1
while i <= n:
    j = 1
    while j <= i:
        print(i, end='')
        j += 1
    i += 1
    print()

s = int()
while n:
    val = n % 10
    s += val

    n //= 10
print("Sum: ", s)
