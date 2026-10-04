import pyttsx3
# Used to convert text into spoken voice


def speak(text):
    # Converts the given text into speech

    engine = pyttsx3.init()
    # Creates a fresh speech engine for each response

    engine.say(text)
    # Adds the text to the speech queue

    engine.runAndWait()
    # Speaks the queued text

    engine.stop()
    # Closes the speech engine
