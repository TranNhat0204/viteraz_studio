"""
Vietnamese Text Normalizer for TTS — Simple find-and-replace from voice_dict.json

When Smooth is ON:
  → Replace words using "Phát âm tùy chỉnh" table (custom_pronunciation)
  → Case-insensitive, whole-word matching
"""
import re
import json
from pathlib import Path as _Path

# Backward compat
IPA_OK = True

# ── User dictionary (loaded from voice_dict.json) ──
_DICT_PATH = _Path(__file__).resolve().parent / "voice_dict.json"
_user_pronunciation: dict = {}   # {"big": "bíc", "computer": "com-piu-tơ", ...}


def _load_user_dict():
    """Load user dictionary from voice_dict.json."""
    global _user_pronunciation
    try:
        if _DICT_PATH.exists():
            data = json.loads(_DICT_PATH.read_text("utf-8"))
            _user_pronunciation = data.get("custom_pronunciation", {})
    except Exception:
        pass


def reload_user_dict():
    """Reload user dictionary (called from config panel after save)."""
    _load_user_dict()


_load_user_dict()  # Load on import


def _build_pattern(word: str) -> str:
    """Build regex pattern for a word.

    - Normal words: use \\b for whole-word matching
    - Units with non-word chars (km/h, m/s): use lookaround so they
      match even when attached to digits like '120km/h'
    - Short units (kg, km, GB, dB...): also use lookaround for digit-attach
    """
    escaped = re.escape(word)
    has_special = not word.isalnum()

    # Known unit patterns (entries that should match when attached to digits)
    _UNIT_WORDS = {
        'km', 'cm', 'mm', 'kg', 'mg', 'ml', 'ha', 'm2', 'm3', 'km2',
        'GB', 'MB', 'KB', 'TB', 'GHz', 'MHz', 'kW', 'MW', 'kWh', 'Hz',
        'dB', 'pH', 'rpm', 'psi', 'fps', 'bps', 'Mbps',
    }

    if has_special or word in _UNIT_WORDS:
        # Units: match after digit/space, add space if after digit
        return r'(?<=[\d\s])' + escaped + r'(?=\s|$|[,.\!\?;\)\]])'
    else:
        return r'\b' + escaped + r'\b'


def convert_english_in_text(text: str) -> str:
    """
    Normalize text for TTS using custom pronunciation table.
    Simple find-and-replace: case-insensitive.

    - Longest match first (so 'km/h' matches before 'km')
    - Units with / or special chars match even next to digits
    """
    if not text or not _user_pronunciation:
        return text or ""

    # Sort by length descending → longest match wins
    sorted_entries = sorted(_user_pronunciation.items(),
                            key=lambda x: len(x[0]), reverse=True)

    for orig, pron in sorted_entries:
        pattern = _build_pattern(orig)
        try:
            text = re.sub(pattern, pron, text, flags=re.IGNORECASE)
        except re.error:
            # Fallback: simple word boundary
            text = re.sub(r'\b' + re.escape(orig) + r'\b',
                          pron, text, flags=re.IGNORECASE)
    # Normalize decimal numbers: "3.5" → "3 chấm 5"
    text = re.sub(r'(\d+)\.(\d+)', r'\1 chấm \2', text)

    # Ensure space between digit and Vietnamese text (e.g. "300ki lô" → "300 ki lô")
    text = re.sub(r'(\d)([a-zA-ZÀ-ỹ])', r'\1 \2', text)

    return text


def convert_with_details(text: str):
    """Same as convert_english_in_text but also returns conversion details."""
    original = text
    result = convert_english_in_text(text)

    details = []
    if original != result:
        details.append((original, "", result))

    return result, details


# ── Quick test ──
if __name__ == "__main__":
    tests = [
        "Hello world, đây là bài test",
        "big bang vũ trụ",
        "Alex dùng iPhone và Google",
        "download software từ website",
        "check email và marketing online",
    ]
    for t in tests:
        result = convert_english_in_text(t)
        print(f"IN:  {t}")
        print(f"OUT: {result}")
        print()
    print(f"Total entries: {len(_user_pronunciation)}")
