"""App entry point"""

# System imports
from tkinter import (Frame, LEFT, X)

from front import main


if __name__ == "__main__":
    window = main.MainWindow()
    root = window.create_window()
    root.configure(bg="black")

    publication_frame = Frame(root, bg="red")
    publication_frame.pack(side=LEFT)

    article_frame = Frame(root)
    article_frame.pack()

    root.mainloop()