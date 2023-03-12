#  Print all integers from 0 to 150.
def print_integers():
    for i in range(151):
        print(i)

print_integers()   
    
# Print all the multiples of 5 from 5 to 1,000
for i in range(5, 1001, 5):
    print(i)
    
# Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
def print_numbers():
    for i in range(1, 101):
        if i % 10 == 0:
            print("Coding Dojo")
        elif i % 5 == 0:
            print("Coding")
        else:
            print(i)
        
# Add odd integers from 0 to 500,000, and print the final sum.
def odd_numbers():
    total = 0
    for i in range(1, 500001, 2):
        total += i
    print("The sum of odd integers from 0 to 500,000 is:", total)
    

sum_odd_numbers()

# Print positive numbers starting at 2018, counting down by fours.
def countdown_by_four():
    for i in range(2018, 0, -4):
        print(i)


countdown_by_four()

# Flexible Counter
def flexible_counter(lowNum, highNum, mult):
    for i in range(lowNum, highNum+1):
        