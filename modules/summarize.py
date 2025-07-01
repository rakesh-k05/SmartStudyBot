"""
summarize.py

This module provides a function to generate a text summary using the
LSA (Latent Semantic Analysis) algorithm. It utilizes the `sumy` library to identify and
extract the most relevant sentences from a given input text.
Useful for condensing long pieces of text into a few key points.
"""

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def generate_summary(text, sentence_count=3):
    """
    Generates a summary of the given text using the LSA (Latent Semantic Analysis) algorithm.

    This function parses the input text and summarizes it by extracting the most
    relevant sentences based on latent semantic analysis. It uses the `sumy` library
    for text parsing and summarization.

    Parameters:
        text (str): The input text to summarize.
        sentence_count (int, optional): The number of sentences to include in the summary.
                                        Defaults to 3.

    Returns:
        str: A summarized version of the text with the specified number of sentences.
    """

    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentence_count)
    return " ".join(str(sentence) for sentence in summary)
