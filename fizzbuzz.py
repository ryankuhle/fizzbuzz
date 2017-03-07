def fizzbuzz(n):
    print("Fizz buzz is counting up to", n)
    
    i = 0 # counter
    while i < n:
        i += 1
        if (i % 3 == 0 and i % 5 == 0):
            print("FizzBuzz")
        elif (i % 3 == 0):
            print("Fizz")
        elif (i % 5 == 0):
            print("Buzz")
        else:
            print(i)
            
    print("Done!")
        
r = int(input("How high should we count? "))
fizzbuzz(r)