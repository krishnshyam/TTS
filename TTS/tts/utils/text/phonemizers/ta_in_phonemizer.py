from typing import Dict

from TTS.tts.utils.text.indic.ta_phonemizer import tamil_text_to_phonemes
from TTS.tts.utils.text.phonemizers.base import BasePhonemizer

_DEF_TA_PUNCS = ",.[]()?!'\""


class TA_IN_Phonemizer(BasePhonemizer):
    """🐸TTS ta_in_phonemizer using functions in `TTS.tts.utils.text.indic.ta_phonemizer`

    Example:

        >>> from TTS.tts.utils.text.phonemizers import TA_IN_Phonemizer
        >>> phonemizer = TA_IN_Phonemizer()
        >>> phonemizer.phonemize("தமிழ் தமிழர்களினதும் தமிழ் பேசும் பலரின் தாய்மொழி ஆகும்.", separator="")
        't̪amiɻ t̪amiɻaɾkaɭinat̪um t̪amiɻ peːt͡ʃum palaɾin t̪aːjmoɻi aːkum.'
        """

    language = "ta-in"

    def __init__(self, punctuations=_DEF_TA_PUNCS, keep_puncs=True, **kwargs):  # pylint: disable=unused-argument
        super().__init__(self.language, punctuations=punctuations, keep_puncs=keep_puncs)

    @staticmethod
    def name():
        return "ta_in_phonemizer"

    def _phonemize(self, text: str, separator: str = "", character: str = "IPA") -> str:
        ph = tamil_text_to_phonemes(text, character=character)
        if separator is not None or separator != "":
            return separator.join(ph)
        return ph

    def phonemize(self, text: str, separator: str = "", character: str = "UTF", language=None) -> str:
        return self._phonemize(text, separator, character)

    @staticmethod
    def supported_languages() -> Dict:
        return {"ta-in": "IPA"}

    def version(self) -> str:
        return "0.0.1"

    def is_available(self) -> bool:
        return True


if __name__ == "__main__":
    texts = "தமிழ் தமிழர்களினதும் தமிழ் பேசும் பலரின் தாய்மொழி ஆகும்."
    e = TA_IN_Phonemizer()
    print(e.supported_languages())
    print(e.version())
    print(e.language)
    print(e.name())
    print(e.is_available())
    print(e.phonemize(texts))
