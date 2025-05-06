#program to print the collatz sequence


#define a function for doing the collatz calculation
def collatz(number):
#if the current number is even, do a floor division by  2, store it in another variable  and print the value
    if number%2==0:
        r_value=number//2
        print("even=",r_value)
#else , multiply the number by 3 and add 1 to it, before storing it in another variable
    else:
        r_value=3*number+1
        print("odd=",r_value)
#return the value of the modified number
    return r_value

#declare a return value variable that stores the return value
return_value=0
#declare i for counting the number of looping times
i=0

#Ask user input for the number
num=int(input("Enter a number:"))

#main program loop (exits if return value not = 1)
while return_value!=1:
#call the collatz function and pass the user input to it and assign a variable to it to store the return value
    return_value=collatz(num) 
#updates the  userinput value by changing it to the return value of the function 
    num=return_value
#print the return value of the function
    print("return_value=",return_value)
#update the loop counter
    i+=1
#print the number of times the loop has looped
    print("looping",i,"times")
#print the  exit succesfully string to make sure the program ran successfully and exited out of the loop.
print("program exited successfully!")

