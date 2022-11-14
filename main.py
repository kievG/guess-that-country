"""
Let's play a game called Guess-that-Country.
This game makes use of web scraping from https://www.worldometers.info.
"""
# import modules
import gtcmodules
import time

def main() -> None:
    print(gtcmodules.welcome)
    time.sleep(6)
    while True:
        gtcmodules.run_guess_that_country()
    
if __name__ == '__main__':
    main()