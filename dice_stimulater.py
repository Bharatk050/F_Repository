name = input("Enter your name: ")
print(f"Hello {name}")

import random
ranNo = random.randint(1,6)
for i in range(1,7):
    if ranNo == i:
        print("*" * i)
# print(ranNo)
