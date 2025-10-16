def add_numbers(a, b):
    """
    Problem 1:
    Write a function that takes two numbers (a and b)
    and returns their sum.

    Example:
    >>> add_numbers(2, 3)
    5
    """
    # TODO: Write your code below
    return a + b
    pass


def is_even(n):
    """
    Problem 2:
    Return True if the given number 'n' is even, otherwise return False.

    Example:
    >>> is_even(4)
    True
    >>> is_even(5)
    False
    """
    # TODO: Write your code below
    if n % 2 == 0:
        return True
    else:
        return False
    pass


def count_vowels(word):
    """
    Problem 3:
    Write a function that counts how many vowels are in a given string.

    Vowels are: a, e, i, o, u (both uppercase and lowercase).

    Example:
    >>> count_vowels("Hello")
    2
    """
    # TODO: Write your code below
    vowels = ('a','e','i','o','u','A','E','I','O','U')
    count = 0
    for i  in word:
        if i in vowels:
             count += 1
    return count
    
    
    pass


def find_max(numbers):
    """
    Problem 4:
    Given a list of numbers, return the largest number.

    Example:
    >>> find_max([1, 4, 2, 10])
    10
    """
    # TODO: Write your code below
    return max(numbers)
    pass


def reverse_string(s):
    """
    Problem 5:
    Write a function that returns the reverse of the input string.

    Example:
    >>> reverse_string("cat")
    'tac'
    """
    # TODO: Write your code below
    return s[::-1]
    pass


def average(numbers):
    """
    Problem 6:
    Given a list of numbers, return their average.
    If the list is empty, return 0.

    Example:
    >>> average([2, 4, 6])
    4.0
    >>> average([])
    0
    """
    # TODO: Write your code below
    average = 0
    sum = 0
    for i in numbers:
        if i == []:
            return 0
        else:
           sum += i
           average = sum/int(len(i))
    return average

    pass


def word_in_sentence(word, sentence):
    """
    Problem 7:
    Return True if the given word appears in the sentence, otherwise False.

    Example:
    >>> word_in_sentence("cat", "The cat is sleeping")
    True
    >>> word_in_sentence("dog", "The cat is sleeping")
    False
    """
    # TODO: Write your code below
    if word in sentence:
        return True
    else:
        return False
    pass


def factorial(n):
    """
    Problem 8:
    Write a function that returns the factorial of a non-negative integer n.
    The factorial of n (written as n!) is the product of all positive integers up to n.
    If n is 0, return 1.

    Example:
    >>> factorial(5)
    120
    >>> factorial(0)
    1
    """
    # TODO: Write your code below
    number = 1
    for i in range(1,n+1):
        if n == 0:
            return 1

        else:
            number *= i
    return number
    pass


def remove_duplicates(numbers):
    """
    Problem 9:
    Given a list of numbers, return a new list with duplicates removed.
    The order of the first occurrence of each new = vowels.split()element should be preserved.

    Example:
    >>> remove_duplicates([1, 2, 2, 3, 1])
    [1, 2, 3]
    """
    # TODO: Write your code below
    new_list = list(set(numbers))
    return new_list
    pass


def fizzbuzz(n):
    """
    Problem 10:
    Write a function that returns a list of numbers from 1 to n,
    but replace:
    - multiples of 3 with "Fizz"
    - multiples of 5 with "Buzz"
    - multiples of both 3 and 5 with "FizzBuzz"

    Example:
    >>> fizzbuzz(5)
    [1, 2, 'Fizz', 4, 'Buzz']
    """
    # TODO: Write your code below
    new_l = []
    for i in range(1,n):
        new_l.append(i)
        if 3 in new_l:
            new_l = ['Fizz']
        elif 5 in new_l:
            new_l = ['Buzz']
        
    return new_l
    pass