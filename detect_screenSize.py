from screeninfo import get_monitors


def calculate_screen_size_screeninfo():
    """Uses screeninfo library to get a list of screens. Returns list and prints dimensions for all screens"""
    screens = get_monitors()
    for idx, screen in enumerate(screens):
        if screen.is_primary:
            print(f"Primary screen: {screen.width}x{screen.height}")
        else:
            print(f"Secondary screen: {screen.width}x{screen.height}")
    return screens


calculate_screen_size_screeninfo()
