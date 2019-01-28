"""Main aotd module."""

# System imports
from tkinter import Tk


class MainWindow:
    """Main window class."""

    def __init__(self, **kwargs):
        self.width = kwargs.get('width', 400)
        self.height = kwargs.get('height', 400)
        self.root = None

    def create_window(self):
        """Create the  main window"""

        root = Tk()
        root.title('AOTD!')

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        x = int(screen_width/2 - self.width/2)
        y = int(screen_height/2 - self.height/2)

        root.geometry(f'{self.width}x{self.height}+{x}+{y}')

        self.root = root

        return root
