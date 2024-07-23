# logic.py
import random

class GuessNumberGame:
    def __init__(self, starting_capital):
        self.min_number = 1
        self.max_number = 10
        self.max_attempts = 5
        self.starting_capital = starting_capital
        self.capital = starting_capital
        self.attempts = 0

    def start(self):
        print(f"Welcome to Guess the Number Game! You have {self.max_attempts} attempts.")

        while self.attempts < self.max_attempts:
            self.attempts += 1
            guess = self.get_player_guess()

            if guess == self.secret_number:
                self.handle_correct_guess()
                break
            else:
                self.handle_wrong_guess(guess)

        if self.attempts >= self.max_attempts:
            print(f"\nGame over! You ran out of attempts. Your final capital is {self.capital}.")
        else:
            print(f"\nCongratulations! You finished the game with {self.capital} capital.")

    def get_player_guess(self):
        while True:
            try:
                guess = int(input(f"\nAttempt {self.attempts}/{self.max_attempts}. "
                                  f"Guess a number between {self.min_number} and {self.max_number}: "))
                if self.min_number <= guess <= self.max_number:
                    return guess
                else:
                    print(f"Please enter a number between {self.min_number} and {self.max_number}.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")

    def handle_correct_guess(self):
        print(f"Congratulations! You guessed the number {self.secret_number} correctly!")
        self.capital *= 2
        print(f"You've doubled your capital. Your current capital is {self.capital}.")

    def handle_wrong_guess(self, guess):
        print(f"Oops! {guess} is not the number I'm thinking of.")
        self.capital -= 10
        print(f"You lost 10 from your capital. Your current capital is {self.capital}.")

    @property
    def secret_number(self):
        if not hasattr(self, '_secret_number'):
            self._secret_number = random.randint(self.min_number, self.max_number)
        return self._secret_number
