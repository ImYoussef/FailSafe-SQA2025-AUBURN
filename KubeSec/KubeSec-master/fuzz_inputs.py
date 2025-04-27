import random
import string
import unicodedata

# List of various Unicode character ranges
UNICODE_RANGES = [
    # Basic Latin (already covered by string.ascii_letters)
    # Latin-1 Supplement
    (0x00A0, 0x00FF),  # Latin-1 Supplement
    (0x0100, 0x017F),  # Latin Extended-A
    (0x0180, 0x024F),  # Latin Extended-B
    (0x0250, 0x02AF),  # IPA Extensions
    (0x02B0, 0x02FF),  # Spacing Modifier Letters
    (0x0300, 0x036F),  # Combining Diacritical Marks
    (0x0370, 0x03FF),  # Greek and Coptic
    (0x0400, 0x04FF),  # Cyrillic
    (0x0500, 0x052F),  # Cyrillic Supplement
    (0x0530, 0x058F),  # Armenian
    (0x0590, 0x05FF),  # Hebrew
    (0x0600, 0x06FF),  # Arabic
    (0x0700, 0x074F),  # Syriac
    (0x0750, 0x077F),  # Arabic Supplement
    (0x0780, 0x07BF),  # Thaana
    (0x07C0, 0x07FF),  # NKo
    (0x0800, 0x083F),  # Samaritan
    (0x0840, 0x085F),  # Mandaic
    (0x0860, 0x086F),  # Syriac Supplement
    (0x08A0, 0x08FF),  # Arabic Extended-A
    (0x0900, 0x097F),  # Devanagari
    (0x0980, 0x09FF),  # Bengali
    (0x0A00, 0x0A7F),  # Gurmukhi
    (0x0A80, 0x0AFF),  # Gujarati
    (0x0B00, 0x0B7F),  # Oriya
    (0x0B80, 0x0BFF),  # Tamil
    (0x0C00, 0x0C7F),  # Telugu
    (0x0C80, 0x0CFF),  # Kannada
    (0x0D00, 0x0D7F),  # Malayalam
    (0x0D80, 0x0DFF),  # Sinhala
    (0x0E00, 0x0E7F),  # Thai
    (0x0E80, 0x0EFF),  # Lao
    (0x0F00, 0x0FFF),  # Tibetan
    (0x1000, 0x109F),  # Myanmar
    (0x10A0, 0x10FF),  # Georgian
    (0x1100, 0x11FF),  # Hangul Jamo
    (0x1200, 0x137F),  # Ethiopic
    (0x1380, 0x139F),  # Ethiopic Supplement
    (0x13A0, 0x13FF),  # Cherokee
    (0x1400, 0x167F),  # Unified Canadian Aboriginal Syllabics
    (0x1680, 0x169F),  # Ogham
    (0x16A0, 0x16FF),  # Runic
    (0x1700, 0x171F),  # Tagalog
    (0x1720, 0x173F),  # Hanunoo
    (0x1740, 0x175F),  # Buhid
    (0x1760, 0x177F),  # Tagbanwa
    (0x1780, 0x17FF),  # Khmer
    (0x1800, 0x18AF),  # Mongolian
    (0x18B0, 0x18FF),  # Unified Canadian Aboriginal Syllabics Extended
    (0x1900, 0x194F),  # Limbu
    (0x1950, 0x197F),  # Tai Le
    (0x1980, 0x19DF),  # New Tai Lue
    (0x19E0, 0x19FF),  # Khmer Symbols
    (0x1A00, 0x1A1F),  # Buginese
    (0x1A20, 0x1AAF),  # Tai Tham
    (0x1AB0, 0x1AFF),  # Combining Diacritical Marks Extended
    (0x1B00, 0x1B7F),  # Balinese
    (0x1B80, 0x1BBF),  # Sundanese
    (0x1BC0, 0x1BFF),  # Batak
    (0x1C00, 0x1C4F),  # Lepcha
    (0x1C50, 0x1C7F),  # Ol Chiki
    (0x1C80, 0x1C8F),  # Cyrillic Extended-C
    (0x1C90, 0x1CBF),  # Georgian Extended
    (0x1CC0, 0x1CCF),  # Sundanese Supplement
    (0x1CD0, 0x1CFF),  # Vedic Extensions
    (0x1D00, 0x1D7F),  # Phonetic Extensions
    (0x1D80, 0x1DBF),  # Phonetic Extensions Supplement
    (0x1DC0, 0x1DFF),  # Combining Diacritical Marks Supplement
    (0x1E00, 0x1EFF),  # Latin Extended Additional
    (0x1F00, 0x1FFF),  # Greek Extended
    (0x2000, 0x206F),  # General Punctuation
    (0x2070, 0x209F),  # Superscripts and Subscripts
    (0x20A0, 0x20CF),  # Currency Symbols
    (0x20D0, 0x20FF),  # Combining Diacritical Marks for Symbols
    (0x2100, 0x214F),  # Letterlike Symbols
    (0x2150, 0x218F),  # Number Forms
    (0x2190, 0x21FF),  # Arrows
    (0x2200, 0x22FF),  # Mathematical Operators
    (0x2300, 0x23FF),  # Miscellaneous Technical
    (0x2400, 0x243F),  # Control Pictures
    (0x2440, 0x245F),  # Optical Character Recognition
    (0x2460, 0x24FF),  # Enclosed Alphanumerics
    (0x2500, 0x257F),  # Box Drawing
    (0x2580, 0x259F),  # Block Elements
    (0x25A0, 0x25FF),  # Geometric Shapes
    (0x2600, 0x26FF),  # Miscellaneous Symbols
    (0x2700, 0x27BF),  # Dingbats
    (0x27C0, 0x27EF),  # Miscellaneous Mathematical Symbols-A
    (0x27F0, 0x27FF),  # Supplemental Arrows-A
    (0x2800, 0x28FF),  # Braille Patterns
    (0x2900, 0x297F),  # Supplemental Arrows-B
    (0x2980, 0x29FF),  # Miscellaneous Mathematical Symbols-B
    (0x2A00, 0x2AFF),  # Supplemental Mathematical Operators
    (0x2B00, 0x2BFF),  # Miscellaneous Symbols and Arrows
    (0x2C00, 0x2C5F),  # Glagolitic
    (0x2C60, 0x2C7F),  # Latin Extended-C
    (0x2C80, 0x2CFF),  # Coptic
    (0x2D00, 0x2D2F),  # Georgian Supplement
    (0x2D30, 0x2D7F),  # Tifinagh
    (0x2D80, 0x2DDF),  # Ethiopic Extended
    (0x2DE0, 0x2DFF),  # Cyrillic Extended-A
    (0x2E00, 0x2E7F),  # Supplemental Punctuation
    (0x2E80, 0x2EFF),  # CJK Radicals Supplement
    (0x2F00, 0x2FDF),  # Kangxi Radicals
    (0x2FF0, 0x2FFF),  # Ideographic Description Characters
    (0x3000, 0x303F),  # CJK Symbols and Punctuation
    (0x3040, 0x309F),  # Hiragana
    (0x30A0, 0x30FF),  # Katakana
    (0x3100, 0x312F),  # Bopomofo
    (0x3130, 0x318F),  # Hangul Compatibility Jamo
    (0x3190, 0x319F),  # Kanbun
    (0x31A0, 0x31BF),  # Bopomofo Extended
    (0x31C0, 0x31EF),  # CJK Strokes
    (0x31F0, 0x31FF),  # Katakana Phonetic Extensions
    (0x3200, 0x32FF),  # Enclosed CJK Letters and Months
    (0x3300, 0x33FF),  # CJK Compatibility
    (0x3400, 0x4DBF),  # CJK Unified Ideographs Extension A
    (0x4DC0, 0x4DFF),  # Yijing Hexagram Symbols
    (0x4E00, 0x9FFF),  # CJK Unified Ideographs
    (0xA000, 0xA48F),  # Yi Syllables
    (0xA490, 0xA4CF),  # Yi Radicals
    (0xA4D0, 0xA4FF),  # Lisu
    (0xA500, 0xA63F),  # Vai
    (0xA640, 0xA69F),  # Cyrillic Extended-B
    (0xA6A0, 0xA6FF),  # Bamum
    (0xA700, 0xA71F),  # Modifier Tone Letters
    (0xA720, 0xA7FF),  # Latin Extended-D
    (0xA800, 0xA82F),  # Syloti Nagri
    (0xA830, 0xA83F),  # Common Indic Number Forms
    (0xA840, 0xA87F),  # Phags-pa
    (0xA880, 0xA8DF),  # Saurashtra
    (0xA8E0, 0xA8FF),  # Devanagari Extended
    (0xA900, 0xA92F),  # Kayah Li
    (0xA930, 0xA95F),  # Rejang
    (0xA960, 0xA97F),  # Hangul Jamo Extended-A
    (0xA980, 0xA9DF),  # Javanese
    (0xA9E0, 0xA9FF),  # Myanmar Extended-B
    (0xAA00, 0xAA5F),  # Cham
    (0xAA60, 0xAA7F),  # Myanmar Extended-A
    (0xAA80, 0xAADF),  # Tai Viet
    (0xAAE0, 0xAAFF),  # Meetei Mayek Extensions
    (0xAB00, 0xAB2F),  # Ethiopic Extended-A
    (0xAB30, 0xAB6F),  # Latin Extended-E
    (0xAB70, 0xABBF),  # Cherokee Supplement
    (0xABC0, 0xABFF),  # Meetei Mayek
    (0xAC00, 0xD7AF),  # Hangul Syllables
    (0xD7B0, 0xD7FF),  # Hangul Jamo Extended-B
    (0xD800, 0xDB7F),  # High Surrogates
    (0xDB80, 0xDBFF),  # High Private Use Surrogates
    (0xDC00, 0xDFFF),  # Low Surrogates
    (0xE000, 0xF8FF),  # Private Use Area
    (0xF900, 0xFAFF),  # CJK Compatibility Ideographs
    (0xFB00, 0xFB4F),  # Alphabetic Presentation Forms
    (0xFB50, 0xFDFF),  # Arabic Presentation Forms-A
    (0xFE00, 0xFE0F),  # Variation Selectors
    (0xFE10, 0xFE1F),  # Vertical Forms
    (0xFE20, 0xFE2F),  # Combining Half Marks
    (0xFE30, 0xFE4F),  # CJK Compatibility Forms
    (0xFE50, 0xFE6F),  # Small Form Variants
    (0xFE70, 0xFEFF),  # Arabic Presentation Forms-B
    (0xFF00, 0xFFEF),  # Halfwidth and Fullwidth Forms
    (0xFFF0, 0xFFFF),  # Specials
]

# Emoji ranges
EMOJI_RANGES = [
    (0x1F300, 0x1F5FF),  # Miscellaneous Symbols and Pictographs
    (0x1F600, 0x1F64F),  # Emoticons
    (0x1F680, 0x1F6FF),  # Transport and Map Symbols
    (0x1F700, 0x1F77F),  # Alchemical Symbols
    (0x1F780, 0x1F7FF),  # Geometric Shapes Extended
    (0x1F800, 0x1F8FF),  # Supplemental Arrows-C
    (0x1F900, 0x1F9FF),  # Supplemental Symbols and Pictographs
    (0x1FA00, 0x1FA6F),  # Chess Symbols
    (0x1FA70, 0x1FAFF),  # Symbols and Pictographs Extended-A
    (0x1FB00, 0x1FBFF),  # Symbols for Legacy Computing
]

# Specific test strings with non-ASCII characters
SPECIFIC_TEST_STRINGS = [
    "usér\u0301name",  # Username with acute accent (é)
    "user\u4F60\u597D",  # Username with Chinese characters (你好)
    "user\u1F600name",  # Username with emoji (😀)
    "user\u200Bname",  # Username with zero-width space
    "user\u0300\u0301name"  # Username with combining accents
]

def get_random_unicode_char(start, end):
    """Get a random Unicode character from the given range"""
    return chr(random.randint(start, end))

def generate_random_unicode_string(length, ranges):
    """Generate a random string of Unicode characters from the given ranges"""
    chars = []
    for _ in range(length):
        # Randomly select a range
        start, end = random.choice(ranges)
        # Get a random character from that range
        char = get_random_unicode_char(start, end)
        # Skip control characters and invalid characters
        if unicodedata.category(char)[0] != 'C' and char != '\uFFFD':
            chars.append(char)
    return ''.join(chars)

def generate_test_inputs():
    """Generate a list of test inputs with non-ASCII characters"""
    test_inputs = []
    
    # Generate strings with various Unicode ranges
    for _ in range(50):
        length = random.randint(1, 20)
        test_inputs.append(generate_random_unicode_string(length, UNICODE_RANGES))
    
    # Generate strings with emojis
    for _ in range(20):
        length = random.randint(1, 5)
        test_inputs.append(generate_random_unicode_string(length, EMOJI_RANGES))
    
    # Generate mixed strings (Unicode + emojis)
    for _ in range(30):
        length = random.randint(5, 15)
        test_inputs.append(generate_random_unicode_string(length, UNICODE_RANGES + EMOJI_RANGES))
    
    # Add some specific problematic characters
    special_chars = [
        '\u0000',  # Null
        '\u2028',  # Line separator
        '\u2029',  # Paragraph separator
        '\uFEFF',  # Zero width no-break space
        '\u200B',  # Zero width space
        '\u200C',  # Zero width non-joiner
        '\u200D',  # Zero width joiner
        '\u2060',  # Word joiner
        '\uFFF9',  # Interlinear annotation anchor
        '\uFFFA',  # Interlinear annotation separator
        '\uFFFB',  # Interlinear annotation terminator
    ]
    
    # Add strings with special characters
    for char in special_chars:
        test_inputs.append(f"user{char}name")
        test_inputs.append(f"{char}username")
        test_inputs.append(f"username{char}")
    
    # Add strings with combining characters
    combining_chars = [
        '\u0300',  # Combining grave accent
        '\u0301',  # Combining acute accent
        '\u0302',  # Combining circumflex accent
        '\u0303',  # Combining tilde
        '\u0304',  # Combining macron
        '\u0305',  # Combining overline
        '\u0306',  # Combining breve
        '\u0307',  # Combining dot above
        '\u0308',  # Combining diaeresis
        '\u0309',  # Combining hook above
        '\u030A',  # Combining ring above
    ]
    
    for char in combining_chars:
        test_inputs.append(f"user{char}name")
        test_inputs.append(f"{char}username")
        test_inputs.append(f"username{char}")
    
    return test_inputs

# Generate the test inputs
FUZZ_INPUTS = generate_test_inputs()

if __name__ == "__main__":
    # Print some sample inputs
    print("Sample fuzz inputs:")
    for i, input_str in enumerate(FUZZ_INPUTS[:20]):
        print(f"{i+1}. {input_str} (length: {len(input_str)})")
    
    # Print the specific test strings
    print("\nSpecific test strings with non-ASCII characters:")
    for i, input_str in enumerate(SPECIFIC_TEST_STRINGS):
        print(f"{i+1}. {input_str} (length: {len(input_str)})")
        print(f"   Unicode points: {' '.join([f'U+{ord(c):04X}' for c in input_str])}")
        print(f"   Character categories: {' '.join([unicodedata.category(c) for c in input_str])}")
        print()
