"""
tts.py

This module handles text-to-speech functionality using the pyttsx3 library.

It exposes a simple `speak` function that converts input text into audible
speech, supporting offline TTS without external API dependencies.
"""

import logging
import pyttsx3

logger = logging.getLogger(__name__)

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

    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except (RuntimeError, Exception) as e:
        logger.error("❌ Failed to speak text: %s", e)
        return

    logger.info("🗣️ Spoke the given text successfully.")
