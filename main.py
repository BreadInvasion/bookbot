from typing import Tuple


def count_words(text:str) -> int:
    return len(text.split())

def count_characters(text:str) -> dict[str,int]:
    output = {}
    text = text.lower()
    for character in text:
        if character not in output:
            output[character] = 1
        else:
            output[character] += 1

    return output

def occurrences_sort(tuple:Tuple[str, int]) -> int:
    return tuple[1]

def main():
    filepath = input("Please provide the filepath to the text file you would like to analyze: ")
    with open(filepath) as f:
        text = f.read()

        num_words = count_words(text)
        character_dict = count_characters(text)
        occurrences = [(char, character_dict[char]) for char in character_dict if char.isalpha()]
        occurrences.sort(key=occurrences_sort, reverse=True)

        print(f"--- Begin report of {filepath} ---")
        print(f"{num_words} words found in the document\n")
        for entry in occurrences:
            print(f"The '{entry[0]}' character was found {entry[1]} times")
        print("--- End report ---")

main()