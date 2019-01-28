"""App entry point"""

# System imports
from tkinter import (Frame, Canvas, N, E, S, W)

# front
from front.main import MainWindow
from front.publications import PublicationFrame


def run():
    """Project entry point"""

    window = MainWindow(width=800, height=600)
    root = window.create_window()

    publications_canvas = Canvas(root, scrollregion=(0, 0, 0.03*window.width, 600))
    publications_canvas.grid(column=0, row=0, sticky=N+E+S+W, in_=root, ipadx=0, pady=0)

    publication_frame = Frame(publications_canvas, bg="#333333")
    publication_frame.grid(column=0, row=0, sticky=N+E+S+W, in_=publications_canvas)
    root.rowconfigure(0, weight=1)

    # Add publication frame/section label and 'add icon'
    PublicationFrame.add_publication_label(publication_frame, window.width)
    PublicationFrame.add_publication_icon(publication_frame)

    # Publications list/menu
    PublicationFrame.create_publication_menu(publication_frame)

    # PublicationFrame.add_publications_scrollbar(publication_frame, publications_canvas)
    publications_canvas.rowconfigure(0, weight=1)

    article_frame = Frame(root, bg="#737373")
    article_frame.grid(column=1, row=0, sticky=N+E+S+W, in_=root)

    root.mainloop()


if __name__ == "__main__":
    run()