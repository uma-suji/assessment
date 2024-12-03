def process_numbers():
    user_input=input("Enter the numbers:")
    numbers=list(map(int,user_input.split()))
    odd_numbers=list(filter(lambda x: x % 2!=0,numbers))
    even_numbers=list(filter(lambda x: x %2==0,numbers))
    sum_odd=reduce(lambda acc,x:acc+x,odd_numbers,0)
    sum_even=reduce(lambda acc,x:acc+x,even_numbers,0)
    result=[sum_odd,sum_even]
    print("Odd numbers:",odd_numbers)
    print("Even_numbers:",even_numbers)
    print("Sum of odd numbers:",sum_odd)
    print("Sum of even numbers:",sum_even)
    print("Result list(sum of odd,sum of even):",result)
process_numbers