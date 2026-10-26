# ----------------------------------------------------------------------
# This is the file mad_libs.py
#
# The intent is to give you practice writing a complete, interactive
# Python program using a lot of Python data types, especially lists,
# sets, and dictionaries.
#
# Remove ALL of the existing comments in this file prior to submission.
# You can, and should, add your own comments, but please remove all the
# comments that are here now.
#
# Things to do:
#
# Define a bunch of templates in which some of the words begin with a colon (:).
# The words that begin with a colon are the words that you will ask the user
# to fill in. An example of a template is:
#
#     "The :color :animal :action over the :adjective :plant."
#
# You should define a list of at least 10 templates. Be creative!
#
# Your app should begin by selecting a random template. Then, for each word
# that begins with a colon in the template, prompt the user for a word
# that fits the description. Make sure that their input is between 1 and 30
# characters long, to prevent them from making too much of a mess of things.
#
# After the user has filled in all of the words, print the completed
# template with the user's words filled in. Then after a blank line, print
# a line crediting the author of the template. Then, print a couple of blank
# lines and ask them if they want to play again. If they say "yes" (or "sí"
# or "oui") or any acceptable version of an affirmative answer, start over
# with a new random template. Otherwise, say "no", print "Thanks for playing!"
# and exit the program.
#
# Here are some constraints:
#
#   1. The templates should be a list of dictionaries, in which each entry
#      has a "text" fields and an "author" field. The "text" field should
#      contain the template string, and the "author" field should contain
#      the name of the person who wrote the template.
#
#   2. The possible "yes" answers should be stored in a set.
# ----------------------------------------------------------------------
import random

templates = [
    {
        "text": "The :color :animal :action over the :adjective :plant.",
        "author": "Anonymous"
    },
    {
        "text": "Once upon a time, a :adjective :animal lived in a :place.",
        "author": "Anonymous"
    },
    {
        "text": "In the :adjective :place, a :animal decided to :action.",
        "author": "Anonymous"
    },
    {
        "text": "The :adjective :animal was very :emotion when it saw the :adjective :object.",
        "author": "Anonymous"
    },
    {
        "text": "A :adjective :animal and a :adjective :animal went on a :adjective :adventure to find the :adjective :object.",
        "author": "Anonymous"
    },
    {
        "text": "The :adjective :animal was very :emotion when it saw the :adjective :object.",
        "author": "Anonymous"
    },
    {
        "text": "A :adjective :animal and a :adjective :animal went on a :adjective :adventure to find the :adjective :object.",
        "author": "Anonymous"
    },
    {
        "text": "The :adjective :animal was very :emotion when it saw the :adjective :object.",
        "author": "Anonymous"
    },
    {
        "text": "A :adjective :animal and a :adjective :animal went on a :adjective :adventure to find the :adjective :object.",
        "author": "Anonymous"
    },
    {
        "text": "The :adjective :animal was very :emotion when it saw the :adjective :object.",
        "author": "Anonymous"
    }
]
yes_answers = {"yes", "y", "sí", "si", "oui", "ja", "hai", "da"}


def get_user_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if 1 <= len(user_input) <= 30:
            return user_input
        else:
            print("Input must be between 1 and 30 characters long. Please try again.")
def fill_in_template(template):
    filled_template = template["text"]
    placeholders = [word for word in filled_template.split() if word.startswith(":")]
    user_inputs = {}
    for placeholder in placeholders:
        prompt = f"Please enter a {placeholder[1:]}: "
        user_input = get_user_input(prompt)
        user_inputs[placeholder] = user_input
    for placeholder, user_input in user_inputs.items():
        filled_template = filled_template.replace(placeholder, user_input)
    return filled_template
def main():
    while True:
        template = random.choice(templates)
        filled_template = fill_in_template(template)
        print("\n" + filled_template)
        print(f"\nTemplate by: {template['author']}\n")
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again not in yes_answers:
            print("Thanks for playing!")
            break
def play_once():
    template = random.choice(templates)
    filled_template = fill_in_template(template)
    print("\n" + filled_template)
    print(f"\nTemplate by: {template['author']}\n")
def main():
    while True:
        play_once()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again not in yes_answers:
            print("Thanks for playing!")
            break
if __name__ == "__main__":
    main()