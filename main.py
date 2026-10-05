from commands.browser import open_website, google_search, youtube_search
# Imports website, Google search and YouTube search functions
from commands.voice import listen
# Imports the microphone listening function
from commands.speech import speak
# Imports text-to-speech
from commands.datetime_utils import get_time, get_date
# Imports the time and date functions
from commands.apps import open_notepad, open_calculator
# Imports Windows application functions
from commands.router import get_intent
# Imports the command router


def main():
    # Main function of JARVIS
    speak("Hello! I am Jarvis. How can I help you?")
    # Speaks the greeting
    print("Hello! I am Jarvis. How can I help you?")

    speak("what are we doing today? sir ")
    print("what are we doing today? sir ")

    while True:
        command = listen()
        # Gets the command from the microphone

        if command == "":
            # Skips the loop if no command was understood
            continue

        intent = get_intent(command)
        # Finds what the user wants to do

        if intent == "exit":
        # Checks if the user wants to stop JARVIS
            speak("Goodbye, sir.")
            # Speaks the response
            print("Jarvis: Goodbye, sir.")
            # Displays the response
            break
            # Stops JARVIS


        elif intent == "open_youtube":
            # Checks if the user wants to open YouTube
            speak("Opening YouTube.")
            # Speaks the response
            print("Jarvis: Opening YouTube.")
            # Displays the response
            open_website("https://www.youtube.com")
            # Opens YouTube

        elif intent == "open_my_portfolio":
            # Checks if the user wants to open your personal website
            speak("Opening your portfolio.")
            # Speaks the response
            print("Jarvis: Opening your portfolio.")
            # Displays the response
            open_website("https://mehfujjamadar.wordpress.com/")
            # Opens your personal website


        elif intent == "open_linkedin":
            # Checks if the user wants to open LinkedIn
            speak("Opening LinkedIn.")
            # Speaks the response
            print("Jarvis: Opening LinkedIn.")
            # Displays the response
            open_website("https://www.linkedin.com/in/mehfuj-jamadar-0a1b4b1a6/")
            # Opens LinkedIn


        elif intent == "open_my_website":
            # Checks if the user wants to open your personal website
            speak("Opening your personal website.")
            # Speaks the response
            print("Jarvis: Opening your personal website.")
            # Displays the response
            open_website("https://mehfujjamadar-ms-r3435.netlify.app/")
            # Opens your personal website


        elif intent == "open_my_github":
            # Checks if the user wants to open your GitHub
            speak("Opening your GitHub.")
            # Speaks the response
            print("Jarvis: Opening your GitHub.")
            # Displays the response
            open_website("https://github.com/mehfujjamadar868-design")

        elif intent == "open_my_instagram":
            # Checks if the user wants to open your Instagram
            speak("Opening your Instagram.")
            # Speaks the response
            print("Jarvis: Opening your Instagram.")
            # Displays the response
            open_website("https://www.instagram.com/mehfuj_707?stkn=b3BvbTdreGQ3YTVy")
            # Opens your Instagram

        elif intent == "open_google":
            # Checks if the user wants to open Google
            speak("Opening Google.")
            # Speaks the response
            print("Jarvis: Opening Google.")
            # Displays the response
            open_website("https://www.google.com")
            # Opens Google


        elif intent == "open_github":
            # Checks if the user wants to open GitHub
            speak("Opening GitHub.")
            # Speaks the response
            print("Jarvis: Opening GitHub.")
            # Displays the response
            open_website("https://github.com")
            # Opens GitHub


        elif intent == "open_chatgpt":
            # Checks if the user wants to open ChatGPT
            speak("Opening ChatGPT.")
            # Speaks the response
            print("Jarvis: Opening ChatGPT.")
            # Displays the response
            open_website("https://chatgpt.com")
            # Opens ChatGPT     


        elif intent == "open_notepad":
            # Checks if the user wants to open Notepad
            speak("Opening Notepad.")
            # Speaks the response
            print("Jarvis: Opening Notepad.")
            # Displays the response
            open_notepad()
            # Opens Notepad


        elif intent == "open_calculator":
            # Checks if the user wants to open Calculator
            speak("Opening Calculator.")
            # Speaks the response
            print("Jarvis: Opening Calculator.")
            # Displays the response
            open_calculator()
            # Opens Calculator


        elif intent == "get_time":
            # Checks if the user wants the current time
            current_time = get_time()
            # Gets the current time
            speak(f"The time is {current_time}.")
            # Speaks the time
            print(f"Jarvis: The time is {current_time}.")
            # Displays the time


        elif intent == "get_date":
            # Checks if the user wants today's date
            current_date = get_date()
            # Gets today's date
            speak(f"Today's date is {current_date}.")
            # Speaks the date
            print(f"Jarvis: Today's date is {current_date}.")
            # Displays the date

        elif intent == "google_search":
            # Checks if the user wants a Google search
            query = command[7:]
            # Removes "search " and keeps the search text
            speak(f"Searching Google for {query}.")
            # Speaks the response
            print(f"Jarvis: Searching Google for {query}.")
            # Displays the response
            google_search(query)
            # Opens Google with the search query


        elif intent == "youtube_search":
            # Checks if the user wants to search YouTube
            query = command[5:]
            # Removes "play " and keeps the song name
            speak(f"Searching YouTube for {query}.")
            # Speaks the response
            print(f"Jarvis: Searching YouTube for {query}.")
            # Displays the response
            youtube_search(query)
            # Opens YouTube with the search query

        else:
            # Runs when JARVIS does not understand the command
            speak("Sorry, I don't know that command yet.")
            # Speaks the response
            print("Jarvis: Sorry, I don't know that command yet.")
            # Displays the response


if __name__ == "__main__":
    # Starts JARVIS when this file is executed
    main()