def add_numbers(num1: int, num2: int) -> int:
    """
    Adds two numbers together.

    Args:
        num1 (int): The first number.
        num2 (int): The second number.

    Returns:
        int: The sum of num1 and num2.
    """
    print(f"add_numbers called with num1={num1}, num2={num2}")
    return num1 + num2

if __name__ == "__main__":
    # Example usage
    result = add_numbers(5, 10)
    print(f"The sum of 5 and 10 is: {result}")