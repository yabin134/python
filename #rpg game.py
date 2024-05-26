#rpg game

import random

def generate_story():
    # Define lists of possible elements for each part of the story
    characters = ["a brave knight", "a curious explorer", "a wise wizard", "a mischievous elf", "a daring pirate"]
    settings = ["a mysterious forest", "an ancient castle", "a bustling marketplace", "a distant planet", "a hidden cavern"]
    conflicts = ["encountered a fierce dragon", "discovered a hidden treasure", "solved a perplexing riddle", "uncovered a dark secret", "escaped from a dangerous trap"]

    # Generate random elements for each part of the story
    character = random.choice(characters)
    setting = random.choice(settings)
    conflict = random.choice(conflicts)

    # Construct the story
    story = f"{character} embarked on a journey to {setting}, where they {conflict}."

    return story

def main():

    story = generate_story()

    print(story)

if __name__ == "__main__":
    main()
