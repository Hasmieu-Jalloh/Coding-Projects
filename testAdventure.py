#Text adventure game

over_message = "Game over!"


def start():
    message = input("You wake up in the morning, do you go to school or stay home? (home or school) ").lower()
    match message:
        case "home":
            outcome = "You stayed home and never got educated. Which is not so good."
            print(outcome)
            print(over_message)
            quit()
        case "school":
            second()

def second():
    message2 = input("You are now in school, do you go to class or play truant? (class or truant) ").lower()
    match message2:
        case "truant":
            outcome2 = "You got expelled the next day for playing truant"
            print(outcome2)
            print(over_message)
        case "class":
            third()

def third():
    message3 = input("You are now in class, do you do your work and graduate or do no work and not graduate? (work or no work) ").lower()
    match message3:
        case "no work":
            outcome2 = "You wasted all your time going to school just to get nothing done, you didn't make it to graduation"
            print(outcome2)
            print(over_message)
        case "work":
            fourth()

def fourth():
    congrats = "Yay, congrats!!! You made it to graduations and graduated with flying colors. Good job!"
    print(congrats)
    final_score = "you final score is 10"

start()

