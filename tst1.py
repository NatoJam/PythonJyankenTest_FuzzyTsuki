import random
def print_halo():
    name = input("Please input your name:\n")
    print("Hello~, "+name+".\n")
    sum = 0
    for i in name:
        sum += ord(i)
    print("Your identification number is: "+str(sum)+".\n")
print_halo()