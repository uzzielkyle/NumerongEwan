NumerongEwan
====================

A simple command-line number guessing game implemented in Python. The program generates a random number within a specified range, and the player tries to guess it in as few attempts as possible. Feedback is given for each guess to indicate whether the guess is too high, too low, or correct.

Table of Contents
-----------------

- [NumerongEwan](#numerongewan)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Usage](#usage)
  - [Gameplay Instructions](#gameplay-instructions)
  - [Customization](#customization)
  - [Example](#example)
  - [License](#license)

Features
--------

- Randomly generates a target number within a given range.
- Provides hints if the guessed number is too high or too low.
- Tracks the number of attempts taken to guess correctly.
- Allows the player to set custom number ranges.

Requirements
------------

- Python 3.x

Usage
-----

1. Clone the repository:

    ```bash
    git clone https://github.com/username/NumerongEwan.git
    cd NumerongEwan
    ```

2. Run the game:

    ```bash
    python numerong_ewan
    ```

Gameplay Instructions
---------------------

1. The game will prompt you to guess a number within a specified range (default is 1 to 100).
2. Enter your guess, and the program will tell you if your guess is too high, too low, or correct.
3. If your guess is correct, the program will congratulate you and display the total number of attempts taken.
4. You can play again by following the prompt after winning or exiting by typing `exit`.

Customization
-------------

You can modify the range of numbers by editing the `min_number` and `max_number` variables in `numerong_ewan.py`. By default, the range is set from 1 to 100.

Example
-------

```plaintext
Welcome to the Number Guessing Game!
Try to guess the number between 1 and 100.

Enter your guess: 50
Too low, try again!
Enter your guess: 75
Too high, try again!
...
Congratulations! You've guessed the number in 5 attempts.
```

License
-------

This project is licensed under the MIT License. See the LICENSE file for details.
