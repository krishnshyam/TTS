cons = [
    "k",
    "c",
    "tr",
    "tB",
    "p",
    "N",
    "n~",
    "n",
    "nr",
    "nB",
    "m",
    "J",
    "j",
    "9r",
    "l",
    "v",
    "sr",
    "s",
    "hv",
    "zr",
    "rr",
    "lr"
]
vow = [
    "i",
    "u",
    "e",
    "o",
    "a",
    "aI",
    "aU"
]

long_vow = [
    "I",
    "U",
    "E",
    "O",
    "A"
]

indic_valid_symbols = cons + vow + long_vow

_ipa_to_sampa = {
    "p":"p",
    "t̪":"tB",
    "t̪":"tB",
    "ʈ":"tr",
    "k":"k",
    "tʃ":"c",
    "t͡ʃ":"c",
    "d͡ʒ":"J",
    "m":"m",
    "n":"n",
    "n̪":"nB",
    "ɳ":"nr",
    "ŋ":"N",
    "ɲ":"n~",
    "ɾ":"9r",
    "r":"rr",
    "ʋ":"v",
    "l":"l",
    "ʂ":"sr",
    "s":"s",
    "ɻ":"zr",
    "ɭ":"lr",
    "j":"j",
    "h":"hv",
    "i":"i",
    "u":"u",
    "e":"e",
    "o":"o",
    "a":"a",
    "i:":"I",
    "u:":"U",
    "e:":"E",
    "o:":"O",
    "a:":"A",
    "iː":"I",
    "uː":"U",
    "eː":"E",
    "oː":"O",
    "aː":"A",
    "aɪ":"aI",
    "aʊ":"aU",
}

_utf_to_ipa_tam = {
    "ப" : "p",
    "த" : "t̪",
    "ட" : "ʈ",
    "க" : "k",
    "ச" : "c",
    "ஜ" : "ɟ",
    "ம" : "m",
    "ன" : "n",
    "ந" : "n̪",
    "ண" : "ɳ",
    "ங" : "ŋ",
    "ஞ" : "ɲ",
    "ர" : "ɾ",
    "ற" : "r",
    "வ" : "ʋ",
    "ல" : "l",
    "ஷ" : "ʂ",
    "ஸ" : "s",
    "ழ" : "ɻ",
    "ள" : "ɭ",
    "ய" : "j",
    "ஹ" : "h",
    "இ" : "i",
    "உ" : "u",
    "எ" : "e",
    "ஒ" : "o",
    "அ" : "a",
    "ஈ" : "iː",
    "ஊ" : "uː",
    "ஏ" : "eː",
    "ஓ" : "oː",
    "ஆ" : "aː",
    "ஔ" : "aʊ",
    "ஐ" : "a j",
    "ி" : "i",
    "ு" : "u",
    "ெ" : "e",
    "ொ" : "o",
    "ீ" : "iː",
    "ூ" : "uː",
    "ே" : "eː",
    "ோ" : "oː",
    "ா" : "aː",
    "ௌ" : "aʊ",
    "ை" : "aj",
}

_DEF_TA_PUNCS = ",.[]()?!'\"\ :;"

_utf_vows_tam = ["ி", "ு", "ெ", "ொ", "ீ", "ூ", "ே", "ோ", "ா", "ௌ", "ை"]

_utf_cons_tam = [ "ப", "த", "ட", "க", "ச", "ஜ", "ம", "ன", "ந", "ண", "ங", "ஞ", "ர", "ற", "வ", "ல", "ஷ", "ஸ", "ழ", "ள", "ய", "ஹ"]

_utf_halant_tam = chr(0x0BCD)

def is_vowel(char):
    return char in _utf_vows_tam

def is_consonants(char):
    return char in _utf_cons_tam
    
def is_halant(char):
    return char == _utf_halant_tam
    
def is_tamil_utf(char):
    return char in _utf_to_ipa_tam.keys()
    
def is_punc(char):
    return char in _DEF_TA_PUNCS

from itertools import tee, islice, chain

def previous_and_next(some_iterable):
    prevs, items, nexts = tee(some_iterable, 3)
    prevs = chain([None], prevs)
    nexts = chain(islice(nexts, 1, None), [None])
    return zip(prevs, items, nexts)

def tam_g2p(text):
    phone_seq = []
    for previous, char, nxt in previous_and_next(text):
        if is_consonants(char):
            if nxt is not None:
                if is_vowel(nxt) or is_halant(nxt):
                    phone_seq.append(_utf_to_ipa_tam[char])
                    continue
                else:
                    phone_seq.append(_utf_to_ipa_tam[char])
                    phone_seq.append("a")
                    continue
            else:
                phone_seq.append(_utf_to_ipa_tam[char])
                phone_seq.append("a")
                continue
        elif is_tamil_utf(char):
            phone_seq.append(_utf_to_ipa_tam[char])
            continue
        elif is_punc(char):
            phone_seq.append(char)
        else:
            #discarding everything else
            if not is_halant(char):
                print("not tamil: ", char)
            continue
    return phone_seq

def tamil_text_to_phonemes(text, character: str = "IPA") -> str:
    """

    Tamil to IPA.

    example :

        input = 'தமிழ்' 
        output = '하늘'

    """
    
    text = tam_g2p(text)  # 'தமிழ்' --> ['ᄒ', 'ᅡ', 'ᄂ', 'ᅳ', 'ᆯ']
    return "".join(text)
