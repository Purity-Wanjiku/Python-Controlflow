#Write a function that uses while, if and continue statements to
# print all the even numbers between 0 and 50. 
def even_numbers():
    z = 0
    while z < 50:
        z += 1
        if z%2 != 0:
            continue
        print (z)
       
#Write a function that takes an integer argument and 
# prints "Prime" if the number is prime, and "Not prime" if the number is not prime.
def prime_numbers(integer):
      if integer < 2:
        print("Not Prime")
      i = 2
      while i <= integer / 2:
       if integer % i == 0:
        print("Not Prime") 
        i += 1
        print("Prime")
                 
#Write a function that takes a list of integers as input 
# and prints the sum of all the even numbers in the list.

def even_integers(*ints):
   ints=0
   for i in ints:
      if i %2==0:
         ints+=i
         print(ints)

#Write a function that takes any two integers as input,
# and prints the sum of all the numbers between the two integers (inclusive) 
# that are divisible by 3.                 
def two_intergers():
     start=0
     for i in range(6,10):
      if i %3==0:
        
       
       
        
