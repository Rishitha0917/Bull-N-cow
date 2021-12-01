import random
list_of_number = list()

i =102
while i<987:
    z= str(i)
    if(z[0]!=z[1] and z[0]!=z[2] and z[1]!=z[2]):
        list_of_number.append(i)
        i+=1

    else:
        i+=1


randomnum = str(random.choice(list_of_number))
counter=0

while True:
    cow_count=0
    bull_count=0    
    user = input("Enter a 3 Digit Number:")

    if (len(user)!=3):
        print("ur not eligible to game go and study the rules")
        break
    if user == randomnum:
        print("YOU have guessed the number "+str(randomnum)+ " correctly")
        break
    i=0
    while i<len(randomnum):
        if(user[i] in randomnum):
            cow_count+=1
           # print(cow_count)
            if(user[i]==randomnum[i]):
                bull_count+=1
                cow_count-=1
        i+=1
    if(cow_count!=0 or bull_count!=0):
        print(str(cow_count)+" -> cows")
        print(str(bull_count)+" -> bull",)
    if(cow_count==0 and bull_count==0):
        print("shit")
    counter+=1
    print("your trial number"+": "+str(counter))