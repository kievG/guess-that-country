"""
These modules are used for the game Guess-that-Country.
"""
import random
from  dataclasses import dataclass
import webbrowser
import time


welcome:str = """
Welcome to GUESS-THAT-COUNTRY!
You have 7 chances to guess the correct answer.
Select your clues and play away!
"""

def load_country_dataset(file_name: str, mode: str = 'r') -> None:
    """
    This function loads a csv file and return a list of countries.
    
    :param file_name: This is the file name saved in CSV format.
    :param mode: This is set to read.
    :return: A list of countries.
    """
    with open(file_name, mode) as countries:
        # create a countries list
        countries_list: list[str] = []
        # append enries to countries_list
        for country in countries:
            if country != '\n':
                countries_list.append(country)
        return countries_list


def choose_random_country(number_of_countries: int, countries_list: list[str]) -> list[str]:
    """
    This function randomly returns a country from takes a list of countries. 

    :param number_of_countries: This is the number of countries based on the countries_list.
    :param countries_list: This is the output of function load_country_dataset.
    :return: This is a country/string/row randomly selected from the countries_list.
    """
    # randomly choose an index
    country_index = random.randint(0, number_of_countries -1)
    return countries_list[country_index]


@dataclass
class Country:
    """
    This class identifies the atrributes of a country.

    :attribute name: Country's name.
    :attribute name_length: The length of the country's name.
    :attribute aka: For countries with a former name. Not available to all.
    :attribute population: The country's population.
    :attribute land_area: The country's land area.
    :attribute density: The country's density.
    :attribute first_letter: First character of the country's name.
    :attribute last_letter: Last character of the country's name.
    """
    name : str
    name_length : int
    aka : str
    population : int
    land_area : int
    density : int
    first_letter: str
    last_letter: str
    

def country_instance(country: list[str]) -> Country:
    """
    This function creates an instance of a country.

    :param country: A list containing identified attributes about the country.
    :return: A instance of the class Country.
    """
    country = country.split(",")
    name = country[0].replace("_", " ")
    if "(" in name:
        name = name.split("(")
        aka = name[1].strip().replace(")", "")
        name = name[0].strip()
        population = country[1]
        land_area = country[2]
        density = country[3].replace("\n", "")
        first_letter = name[0]
        last_letter = name[-1]
        name_length = len(name) 
        country_instance = Country(name, name_length, aka, population, land_area, density, first_letter, last_letter)
        return country_instance
    if "(" not in name:
        aka = None
        population = country[1]
        land_area = country[2]
        density = country[3].replace("\n", "")
        first_letter = name[0]
        last_letter = name[-1]
        name_length = len(name)
        country_instance = Country(name, name_length, aka, population, land_area, density, first_letter, last_letter)
        return country_instance


def available_clues(clues_list: list, used_clues: list) -> None:
    """
    This function displays available clues to the player.

    :param clues_list: This is a list that contains clues.
    :param used_clues: This is a list of clues availed by the player.
    """
    for idx, clue in enumerate(clues_list):
        if str(idx + 1) not in used_clues:
            print(f" {idx + 1} {clue}")


def tracker(guesses_made: int, answers_given: list[str], clues_enabled: list[str]) -> None:
    """
    This function displays/tracks the user's activities including guesses made, 
    answers given, and clues made available.

    :param guesses_made: A count of guesses that the player made.
    :param answers_given: A list of answers given by the player.
    :param clues_enabled: A list of clues made available to the player.
    """
    
    print(f"""MATCH HISTORY:
    Guesses made: {guesses_made}
    Answers given: {answers_given}
    Clues available: {clues_enabled}""")


def clue_master(country: Country, clue_selected: str) -> str:
    """
    This function matches the user input, in string, with correspinding clues 
    and returns the clue as selected by the player.

    :param country: An instance of the class Country.
    :param clue_selected: The clue that the player wants to see.
    :return: A variable/string representing the clue that the player wants to see.
    """
    match clue_selected:
        case '1':
            clue = f"Number of characters: {country.name_length}"
            return clue
        case '2':
            clue = f"Population: {country.population} (yr 2020)"
            return clue
        case '3':
            clue = f"Land area: {country.land_area} (sq.km)"
            return clue
        case '4':
            clue = f"Density: {country.density} (P/sq.km)"
            return clue
        case '5':
            clue = f"First letter: {country.first_letter}"
            return clue
        case '6':
            clue = f"Last letter: {country.last_letter}"
            return clue
        case '7':
            if country.aka != None:
                clue = f"Also known as...: {country.population}"
                return clue
            else:
                clue = f"No other names known."
                return clue


def ampire(guess: str, country: Country) -> bool:
    """
    This function determine whether the answer given by the player is true or not 
    by comparing the guess with the country name.

    :param guess: The guess given by the player.
    :param country: An instance of the class Country.
    :return: A boolean value indicating if the answer is correct or not.
    """
    if guess.lower() == country.name.lower():
        return True
    else:
        return False


def show_flag(country: Country) -> None:
    """
    This function opens a new browser to show the country's flag in the event the player wins/loses.
    This uses the webbrowser package.

    :param country: An instance of the class Country.
    """
    country_name = country.name
    url = f"https://google.com/search?q={country_name}+flag"
    webbrowser.open_new(url)

     
def run_guess_that_country() -> None:
    """
    This function details the game mechanics.
    """
    # load and read the CSV file
    countries_list = load_country_dataset('scraped_countries.csv', 'r')
    # get the number of countries in the file
    number_of_countries = (len(countries_list))
    # choose a random country from the list
    random_country = choose_random_country(number_of_countries, countries_list)
    # instantiate a randon country
    country = country_instance(random_country)
    # create a list of clues
    clues_list: list(str) = ["Number of characters", "Population", "Land area", "Density", "First letter", "Last letter", "Also known as..."]
    # create a list of used clues
    used_clues : list(str) = [] 
    # create a list of valid clues
    valid_clues: list(str) = ['1', '2', '3', '4', '5', '6', '7']
    # create a list of guesses made
    guesses_made: int = 0
    # create a list of answers given by the user
    answers_given: list[str] = []
    # create a list of clues enabled by the user
    clues_enabled: list[str] = []
    # while (guesses_made < len(clues_list)) & (winner == False):
    while guesses_made < len(clues_list):
        # display game history
        tracker(guesses_made, answers_given, clues_enabled)
        print()
        # display available clues
        available_clues(clues_list, used_clues)
        print()
        try:
            # player selects clue
            clue_selected : str = input("> Select clue: ")
            print()
            if (clue_selected in valid_clues) & (clue_selected not in used_clues):
                used_clues.append(clue_selected)
                clue = clue_master(country, clue_selected)
                clues_enabled.append(clue)
                print(clue)
                print()
                try:
                    # player provides guess 
                    guess: str = input(" > Guess: ")
                    if guess not in answers_given:
                        # append answer given to list
                        answers_given.append(guess)
                        # add 1 to guesses made
                        guesses_made += 1
                        # determine if the answer given by the user is correct or incorrect
                        decision = ampire(guess, country)
                        if decision:
                            # player gave the correct answer
                            print(f"You guessed it RIGHT! The country we are looking for is >>> {country.name} <<<")
                            time.sleep(5)
                            show_flag(country)
                            print()
                            break
                            
                        else:
                            # player gave an incorrect answer
                            print(f"The country we are looking for is NOT {guess}. >>>")
                            print()
                            time.sleep(4)        
                except:
                    pass
        
        except:
            pass
    # player lost
    if guesses_made == len(clues_list):
        print(f"You are out of guesses. The country we are looking for is ... >>>")
        print()
        time.sleep(4)
        show_flag(country)
#END