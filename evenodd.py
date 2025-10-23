

def count_even_odd(numbers):
    even_count = sum(1 for num in numbers if num % 2 == 0)
    odd_count = len(numbers) - even_count
    return even_count, odd_count

def main():
    numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]  
    even, odd = count_even_odd(numbers)
    print(f"Even numbers: {even}")
    print(f"Odd numbers: {odd}")

if __name__ == "__main__":
    main()
