import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','%','$','^','&','*','(',')']


print("welcome to password generator")

nr_num=int(input("How many numbers do you want:"))
nr_letter=int(input("How many letters do you want:"))
nr_symbol=int(input("How many symbol do you want:"))

password_list = []

for num in range(1,nr_num+1):
    password_list += random.choice(numbers)

for char in range(1,nr_letter+1):
    password_list += random.choice(letters)

for symbol in range(1,nr_symbol+1):
    password_list += random.choice(symbols)


password = ""
random.shuffle(password_list)


for i in password_list:
    password += i

print("Your password is " + password + " enjoy")