"""
text_processor.py - Text Processing & Cleaning
Fake News Detector Project
"""

import re


class TextProcessor:
    """
    Handles all text cleaning, normalization, and validation
    before passing to the ML pipeline.
    """

    def preprocess_text(self, text: str) -> str:
        """
        Clean and normalize raw text for model consumption.

        Steps:
        1. Validate input
        2. Lowercase
        3. Remove URLs
        4. Remove @mentions
        5. Remove #hashtags
        6. Remove special characters
        7. Normalize whitespace
        8. Validate minimum word count

        Args:
            text: Raw news article text.

        Returns:
            Cleaned, normalized text string.

        Raises:
            ValueError: If text is None, empty, or too short after cleaning.
        """
        if not text or not isinstance(text, str):
            raise ValueError("Invalid text input: text must be a non-empty string.")

        # Lowercase
        text = text.lower()

        # Remove URLs (http, https, www)
        text = re.sub(r'http\S+|https\S+|www\S+', '', text)

        # Remove @mentions
        text = re.sub(r'@\w+', '', text)

        # Remove #hashtags
        text = re.sub(r'#\w+', '', text)

        # Remove special characters and digits (keep letters and spaces)
        text = re.sub(r'[^a-z\s]', ' ', text)

        # Normalize whitespace (collapse multiple spaces/newlines)
        text = ' '.join(text.split())

        # Validate minimum word count
        if not self.validate_text(text):
            raise ValueError("Text is too short or invalid (minimum 3 words required after cleaning).")

        return text

    def validate_text(self, text: str, min_words: int = 3) -> bool:
        """
        Check if text meets the minimum word-count requirement.

        Args:
            text: Text to validate.
            min_words: Minimum number of words required.

        Returns:
            True if valid, False otherwise.
        """
        if not text or not isinstance(text, str):
            return False
        words = text.split()
        return len(words) >= min_words

    def get_word_count(self, text: str) -> int:
        """
        Count the number of words in text.

        Args:
            text: Input text.

        Returns:
            Integer word count.
        """
        if not text or not isinstance(text, str):
            return 0
        return len(text.split())
