"""
Translation between English and French.
"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """Translate English text to French."""
    if english_text == "":
        return ""
    return MyMemoryTranslator(source='en-US', target='fr-FR').translate(text=english_text)

def french_to_english(french_text):
    """Translate French text to English."""
    if french_text == "":
        return ""
    return MyMemoryTranslator(source='fr-FR', target='en-US').translate(text=french_text)
    