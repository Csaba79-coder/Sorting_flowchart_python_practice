# Sorting flowchart

## Story

Your friend Maria has found an old and dusty notebook with almost faded pages with some flowcharts on it,
and she asked you for help to write the equivalent python script based on them.
First one looks like a simple sorting algorithm that repeatedly steps through the list,
compares each pair of adjacent items and swaps them if they are in the wrong order.
Second one seems to dividing the list into smaller ones to find searched value.
Third one is looking for prime numbers.


## What are you going to learn?

You will learn and practice how to do the following things:

- write code from flowchart,
- how to sort numbers without built-in functions,
- for and while loops,
- algorithms,
- clean code refactoring (making code more easy to read and maintain
  without changing any feature).

## Tasks

1. Implement the algorithm described by [this flowchart](media/progbasics/bubble-sort-flowchart.png).
    - Running the program outputs the following numbers in a list: [1, 2, 56, 32, 51, 2, 8, 92, 15]
    - Running the program outputs the above numbers in a list in ascending order without hard coding the order (using the steps seen in the flowchart): [1, 2, 2, 8, 15, 32, 51, 56, 92]

2. Implement the algorithm described by [this flowchart](media/progbasics/binary-search-flowchart.png).
    - Running the program outputs the following numbers in a list: [1, 2, 4, 7, 11, 22, 38, 42, 43]
    - Running the program outputs an index of searched value in an list, if not present then returns -1 (i.e. for value 4 should return 2)

3. [OPTIONAL] Implement the Sieve of Eratosthenes algorithm described by [this flowchart](media/progbasics/sieve-of-eratosthenes-flowchart.png).
    - Given a number n, find all primes smaller than or equal to n. Then display them in console.

4. Refactor your solution: use functions, make it more easy to read and maintain.
    - Running the program results in the exact same behavior before and after refactoring.
    - Variable names in the program are meaningful nouns and not abbreviated
    - Function names in the program are meaningful verbs and not abbreviated
    - There are no unnecessary (dead) code or comments in the program
    - There are no duplicating code parts or code parts doing the same thing differently in the program
    - There are no function that doing more than one thing in the program
    - After each modification the changes are committed, the program is runnable and results in the exact same behavior than at the beginning
    - Commit messages are meaningful

## General requirements

None

## Hints

- Bubble sort: There are two loops and both of them can be implemented with `while` or `for`
  (but think about which is better when).
- Bubble sort: One loop is an outer loop and one is an inner loop. Do you know which one is which?
- While refactoring make sure you protect the main part of the program
  (outside of the functions) with an `if __name__ == "__main__":`
  [code snippet](https://docs.python.org/3/library/__main__.html).
- Sieve of Eratosthenes: Use an auxiliary list which stores information whether number is a prime number.


## Background materials

- <i class="far fa-exclamation"></i> [About Flowcharts](project/curriculum/materials/pages/general/flowcharts.md)
- <i class="far fa-exclamation"></i> [Basics of clean code](project/curriculum/materials/competencies/clean-code.md.html)
- <i class="far fa-exclamation"></i> [Refactoring in action](project/curriculum/materials/competencies/clean-code/refactoring.md.html)
- <i class="far fa-exclamation"></i> [About nice commit messages](https://chris.beams.io/posts/git-commit/)
- <i class="far fa-video"></i> [Bubble-sort with Hungarian ("Csángó") folk dance](https://www.youtube.com/watch?v=lyZQPjUT5B4)
- <i class="far fa-exclamation"></i> [Divide and conquer](https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm)
- <i class="far fa-exclamation"></i> [Binary search](https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search)
- <i class="far fa-exclamation"></i> [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#/media/File:Sieve_of_Eratosthenes_animation.gif)
- <i class="far fa-exclamation"></i> [What is `if __name__ == "__main__"`??](https://thepythonguru.com/what-is-if-__name__-__main__/)

