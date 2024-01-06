def factorial(n):
    """Calculate the factorial of a number."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n in [0, 1]:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    numbers = [5, 3, 0, -1]
    for num in numbers:
        try:
            print(f"Factorial of {num}: {factorial(num)}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
