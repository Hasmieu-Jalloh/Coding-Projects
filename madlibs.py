#version one
import random
import re


verbs = ["run", "jump", "touch", "drive", "cry"]
nouns = ["cow", "car", "New York", "son", "Janie"]

welcome_message = "Use this example to type in your message\nEg: The boy verb a thousands miles noun\nUse 'noun' or 'verb' to represent your missing word(s)."
print(welcome_message)

user_input = input("Enter your sentence: ")

if re.search("verb", user_input) or re.search("noun", user_input):
  user_input = user_input.replace("verb", random.choice(verbs))
  user_input = user_input.replace("noun", random.choice(nouns))
print(user_input)

#version two

noun1 = input("Enter a noun: ")
verb1 = input("Enter a verb (ending in 'ing'): ")
verb2 = input("Enter a verb: ")
noun2 = input("Enter a noun: ")

madlibs = f"Hey there, welcome to my {noun1}, today we will be {verb1}, and riding our {verb2} with the great {noun2}."

print(madlibs)
