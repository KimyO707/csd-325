#Kimberly Orozco, Module 6.2 Assignment, April 18th, 2025
#Purpose:Create a tuple of car types and prints them in different ways.

def show_all(states):
    print("States:")
    print(", ".join(states))



def show_sentences(states):
    print("\nPlaces I have researched:")
    for state in states:
        print(f"I know a lot about {state}.")



def show_sentences_reverse(states):
    print("\nPlaces I would like to visit:")
    for state in reversed(states):
        print(f"{state} would be awesome to visit!")



def main():
    states = (
        'California', 'Texas', 'Florida', 'New York', 'Illinois',
        'Pennsylvania', 'Ohio', 'Georgia', 'North Carolina', 'Michigan',
        'New Jersey', 'Virginia', 'Washington', 'Arizona', 'Massachusetts'
    )

    show_all(states)
    show_sentences(states)
    show_sentences_reverse(states)



if __name__ == "__main__":
    main()