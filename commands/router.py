def get_intent(command):
    # Finds what the user wants to do

    command = command.lower().strip()
    # Converts the command to lowercase and removes extra spaces


    if any(word in command for word in ["open", "launch", "start"]) and "youtube" in command:
        # Detects different ways of asking to open YouTube
        return "open_youtube"


    if any(word in command for word in ["open", "launch", "start"]) and "google" in command:
        # Detects different ways of asking to open Google
        return "open_google"


    if any(word in command for word in ["open", "launch", "start"]) and "github" in command:
        # Detects different ways of asking to open GitHub
        return "open_github"


    if any(word in command for word in ["open", "launch", "start"]) and "chatgpt" in command:
        # Detects different ways of asking to open ChatGPT
        return "open_chatgpt"


    if any(word in command for word in ["open", "launch", "start"]) and "notepad" in command:
        # Detects different ways of asking to open Notepad
        return "open_notepad"


    if any(word in command for word in ["open", "launch", "start"]) and "calculator" in command:
        # Detects different ways of asking to open Calculator
        return "open_calculator"


    if "what is the time" in command or "what's the time" in command:
        # Detects the time command
        return "get_time"


    if "what is the date" in command or "today's date" in command:
        # Detects the date command
        return "get_date"


    if command.startswith("search "):
        # Detects a Google search command
        return "google_search"


    if command.startswith("play "):
        # Detects a YouTube search command
        return "youtube_search"


    if command == "exit":
        # Detects the exit command
        return "exit"


    return "unknown"
    # Returns unknown when no command matches
