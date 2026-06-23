# for loop 
print ("---- for  loop ----")
for i in range(5):  # until reach the 5 
    print(i)

    name= "Sumaira "
    for char in name:
        print (name)
        print (char)



        # start , stop , step

        # start is used to specify the starting value of the range, 
        # stop is used to specify the ending value (exclusive), 
        # and step is used to specify the increment between each value in the range.
        print ("---- start stop step----")
        for e in range (3, 15 , 3):
         print (e)



         # while loop 
 # while loop is used to execute a block of code repeatedly as long as a specified condition is true.
        print ("---- while loop ----")
        num1=2
        while num1 < 10:
                print(num1)
                num1 += 2  # incrementing the value of num1 by 2 in each iteration



# loop control statements are used to modify the behavior of loops.
# break statement is used to exit the loop prematurely when a certain condition is met.


print ("---- loop  control----")
for i in range(1, 10):
    if i == 5:
        break  # exit the loop when i is equal to 5
    print(i)
