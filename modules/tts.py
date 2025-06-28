import pyttsx3

def speak(text):
    """
    Converts the given text to speech using the pyttsx3 text-to-speech engine.

    This function initializes the speech engine, speaks the provided text aloud,
    and waits for the speech to finish before returning.

    Parameters:
        text (str): The text to be spoken aloud.

    Returns:
        None
    """
        
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
