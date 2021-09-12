travelling = input("Yes or No :")
while travelling == "Yes" :
    num = int(input("Number of people travelling : "))
    for num in range(1, num + 1) :
        name = input("Name :")
        age = input("Age :")
        sex = input("Male Or Female :")
        print(name)
        print(age)
        print(sex)
    travelling = input("Oops ! , Missing some one ")
else :
    print("Not Intersted to traveler have a beer ")
