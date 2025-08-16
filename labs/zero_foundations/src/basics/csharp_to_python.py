"""
C# → Python quick bridge. | C# → Python brzi most.

- No braces; use colon + indentation. | Nema zagrada; koristi dvotačku i uvlaku.
- elif instead of 'else if'. | elif umesto 'else if'.
- None instead of null; True/False case-sensitive. | None umesto null; True/False su case-sensitive.
"""
# ENG/SR comments are kept concise. | Komentari ENG/SR su sažeti.
def is_falsy(value) -> bool:
    """Return True if value is falsy in Python. | Vrati True ako je vrednost 'falsy' u Pythonu."""
    return not bool(value)
