COLORS = {
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "gray": "\033[90m",
    "crimson": "\033[31m",
    "darkred": "\033[31m",
    "lime": "\033[92m",
    "gold": "\033[33m",
    "brown": "\033[33m",
    "maroon": "\033[31m",
    "orange": "\033[33m",
    "purple": "\033[35m",
    "violet": "\033[35m",
    "rainbow": "\033[38;5;51m", 
}

RESET = "\033[0m"
BOLD = "\033[1m"

def get_color(color_name: str | None) -> str:
    """
    Returns the ANSI color code for a given color name.
    If the color is not found or is None, returns an empty string.
    """
    if not color_name:
        return ""
    return COLORS.get(color_name.lower(), "")