def get_intent(command):
    # Converts the command to lowercase and removes extra spaces
    command = command.lower().strip()

    # Personal links
    if "linkedin" in command:
        return "open_linkedin"

    if "portfolio" in command:
        return "open_my_portfolio"

    if "my website" in command or "personal website" in command:
        return "open_my_website"

    if "my github" in command or "my git hub" in command:
        return "open_my_github"

    # Regular websites
    if any(word in command for word in ["open", "launch", "start"]) and "youtube" in command:
        return "open_youtube"

    if any(word in command for word in ["open", "launch", "start"]) and "google" in command:
        return "open_google"

    if any(word in command for word in ["open", "launch", "start"]) and "github" in command:
        return "open_github"

    if any(word in command for word in ["open", "launch", "start"]) and "chatgpt" in command:
        return "open_chatgpt"

    if any(word in command for word in ["open", "launch", "start"]) and "notepad" in command:
        return "open_notepad"

    if any(word in command for word in ["open", "launch", "start"]) and "calculator" in command:
        return "open_calculator"

    # Time
    if "what is the time" in command or "what's the time" in command:
        return "get_time"

    # Date
    if "what is the date" in command or "today's date" in command:
        return "get_date"

    # Google search
    if command.startswith("search "):
        return "google_search"

    # YouTube search
    if command.startswith("play "):
        return "youtube_search"

    # Exit
    if command == "exit":
        return "exit"

    # Unknown command
    return "unknown"