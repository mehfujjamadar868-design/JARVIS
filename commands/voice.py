import sounddevice as sd
# Used to access the microphone

import numpy as np
# Used to handle audio data

import speech_recognition as sr
# Used to convert speech into text


def listen():
    # Records the user's voice and converts it into text

    sample_rate = 16000
    # Sets the audio recording quality

    duration = 5
    # Records audio for 5 seconds

    print("Jarvis: Listening...")

    audio = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="float32"
    )
    # Records sound from the microphone

    sd.wait()
    # Waits until recording is finished

    audio = np.squeeze(audio)
    # Removes unnecessary audio dimensions

    audio_data = sr.AudioData(
        (audio * 32767).astype(np.int16).tobytes(),
        sample_rate,
        2
    )
    # Converts audio into a format SpeechRecognition understands

    recognizer = sr.Recognizer()
    # Creates the speech recognition object

    try:
        # Tries to convert speech into text

        command = recognizer.recognize_google(audio_data)

        print(f"You said: {command}")

        return command.lower()
        # Returns the command in lowercase

    except sr.UnknownValueError:
        # Runs when the speech cannot be understood

        print("Jarvis: Sorry, I didn't understand.")
        return ""

    except sr.RequestError:
        # Runs when Google's speech service cannot be reached

        print("Jarvis: Speech service is unavailable.")
        return ""
