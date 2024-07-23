# main.py
from iskander_hw5.logic import GuessNumberGame

def main():
    starting_capital = int(input("Enter your starting capital: "))

    game = GuessNumberGame(starting_capital)
    game.start()

if __name__ == "__main__":
    main()
