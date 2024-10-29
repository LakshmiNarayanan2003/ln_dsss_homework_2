import random


def get_random_integer(min, max):
    """
    Google docstring:
    Generates a random integer between a minimum and maximum value.

    Args:
        min (int): The minimum value (inclusive).
        max (int): The maximum value (inclusive).

    Returns:
        int: A random integer between min and max.
    """
    return random.randint(min, max)


def get_random_operator():
    """
    Google docstring:
    Selects a random mathematical operator from addition, subtraction, and multiplication.

    Returns:
        str: A randomly chosen operator ('+', '-', or '*').
    """
    return random.choice(['+', '-', '*'])


def perform_operation(n1, n2, o):
    """
    Google docstring:
    Performs a mathematical operation on two numbers based on the given operator.

    Args:
        n1 (int): The first number.
        n2 (int): The second number.
        o (str): The operator ('+', '-', or '*').

    Returns:
        tuple: A tuple with the problem statement (str) and the answer (int).
    """
    p = f"{n1} {o} {n2}"  # Problem string
    # Determine the answer
    if o == '+':
        a = n1 + n2
    elif o == '-':
        a = n1 - n2
    else:
        a = n1 * n2
    return p, a


def math_quiz():
    """
    Initiates a simple math quiz with random arithmetic questions. The user scores points
    by providing correct answers. At the end, the total score is displayed.
    """
    s = 0  # initialize score
    t_q = 3  # total number of questions

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    # Loop to ask the specified number of questions
    for _ in range(t_q):
        # Generate two random numbers and a random operator
        n1 = get_random_integer(1, 10)
        n2 = get_random_integer(1, 10)  # Generate a second random integer for calculation
        o = get_random_operator()

        # Generate the problem and correct answer
        PROBLEM, ANSWER = perform_operation(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")

        # Get user answer and handle non-integer inputs
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue  # Move to the next question without penalty

        # Check if the user's answer is correct
        if user_answer == ANSWER:
            print("Correct! You earned a point.")
            s += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    # Display final score
    print(f"\nGame over! Your score is: {s}/{t_q}")


if __name__ == "__main__":
    math_quiz()
