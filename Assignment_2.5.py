def calculate_even_odd_sums(numbers):
    even_sum =sum(n for n in numbers if n % 2 == 0 )
    odd_sum = sum(n for n in numbers if n % 2 != 0 )
    return even_sum, odd_sum
nums=[10, 21, 32, 43, 54, 65]
even_sum, odd_sum = calculate_even_odd_sums(nums)
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)