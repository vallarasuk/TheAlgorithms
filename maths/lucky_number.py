'''
>>> File :- lucky_number.py
>>> brief :- Program return in boolean (True/False) whether a number is lucky 
number or not
>>> link :- (https://en.wikipedia.org/wiki/Lucky_number)
>>> details :- 
A lucky number is a natural number in a set which is generated by a
certain "sieve". This sieve is similar to Sieve of Eratosthenes that 
generate the primes, but it eliminates number on their position in the 
remaining set, instead of their value.

>>> Example :- 
Take the set of integer 
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, .....
 
First delete every second number, we get following reduced set
1, _, 3, _, 5, _, 7, _, 9, __, 11, __, 13, __, 15, __, 17, __, 19, .....

Now delete every third number, we get
1, _, 3, _, _, _, 7, _, 9, __, __, __, 13, __, 15, __, __, __, 19, .....

Continue this process indefinitely......
'''
# TODO: coding logic behind lucky number
def isLuckyNumber(num):
    for i in range(2,num+1):
        if num%i==0: 
            return False
        num -= num//i
    return True
# TODO: self-test implementation
def test():
    assert(isLuckyNumber(5)==False)
    assert(isLuckyNumber(19)==True)
    assert(isLuckyNumber(13)==True)
    assert(isLuckyNumber(200)==False)
    print("All test cases have successfully passed\n")
# TODO: User defined test-cases
def user_test():
    num = int(input())
    if isLuckyNumber(num):
        print("Yes, it is a lucky number\n")
    else:
        print("No, it is not a lucky number\n")
# TODO: Main function
if __name__=='__main__':
    test() # rin the self-test implementation
    # user_test() # uncomment to get the user input'''