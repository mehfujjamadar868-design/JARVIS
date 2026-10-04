from commands.router import get_intent
# Imports the command router


commands = [
    "open youtube",
    "launch youtube",
    "start youtube",
    "open google",
    "launch github",
    "start calculator",
    "what is the time",
    "search Python OOP",
    "play believer",
    "hello jarvis"
]

# Tests different ways of giving commands
# Creates sample commands for testing

for command in commands:
    # Tests every command

    intent = get_intent(command)
    # Finds the intent of the command

    print(command, "→", intent)
    # Displays the detected intent