"""Publications frontend main module"""

from tkinter import (Label, Scrollbar,  N, W, S, E)


class PublicationFrame:
    """Publications class"""

    publications = {'TechNews': 'url', 'Recode': 'url', 'TechCrunch': 'url'}
    row = 1

    @classmethod
    def pub_entry(cls, widget, publication):
        """Creates a publication entry.

        Args:
            cls (class): PublicationFrame class.
            widget (object): Tkinter master object.
            publication (str): Title of publication/site.

        Returns:
            None
        """

        entry = Label(
            widget,
            text=publication,
            anchor=W,
            bg='#333333',
            fg='#e6e6e6',
            font='LucidaConsole 13 bold',
            borderwidth=0.5,
            relief='solid',
            highlightcolor='#737373',
            padx=10
        )
        entry.grid(column=0, row=cls.row, columnspan=2, sticky=N+E+S+W, ipadx=15, ipady=15)

        entry.bind('<Button-1>', lambda event, pub=publication: cls.get_articles(event, pub))
        cls.row += 1

    @classmethod
    def create_publication_menu(cls, widget):
        """Create list of publication entries.

        Args:
            cls (class): PublicationFrame class.
            widget (object): Tkinter master object.

        Returns:
            None
        """

        for pub in cls.get_all_publications():
            cls.pub_entry(widget, pub)

    @classmethod
    def get_all_publications(cls):
        """Get list of all publications.

        Args:
            cls (class): PublicationFrame class.

        Returns:
            list : Publication titles
        """

        return [title for title in cls.publications]

    @classmethod
    def add_publication_label(cls, widget, window_width):
        """Create label for publications section

        Args:
             cls (class): PublicationFrame class.
             widget (object): publication_frame object.
             window_width (int): width of GUI window.

        Returns:
            None
        """

        publication_width = int(0.03 * window_width)

        publication_label = Label(
            widget,
            text='publications',
            bg='#333333',
            fg='#bfbfbf',
            font='LucidaConsole 11',
            width=publication_width
        )
        publication_label.grid(column=0, row=0, padx=(10, 0), ipadx=10, ipady=7)

    @classmethod
    def add_publication_icon(cls, widget):
        """Create '+' for adding a publication to list of publications.

        Args:
             cls (class): PublicationFrame class.
             widget (object): publication_frame object.

        Returns:
            None
        """

        add_pub_icon = Label(
            widget, text='+',
            font='LucidaConsole 15 bold',
            bg='#333333',
            fg='#e6e6e6'
        )
        add_pub_icon.grid(column=1, row=0, sticky=E, padx=(0, 5))

    @classmethod
    def add_publications_scrollbar(cls, widget, publication_canvas):
        """Add scrollbar to publications section.

        Args:
             cls (class): PublicationFrame class.
             widget (object): publication_frame object.
             publication_canvas (object): Canvas object allowing for scrollable publications list
        """
        publications_scrollbar = Scrollbar(widget, orient='vertical', troughcolor='black')
        publications_scrollbar.config(command=publication_canvas.yview)
        publication_canvas.config(yscrollcommand=publications_scrollbar.set)
        publications_scrollbar.grid(row=0, column=3)

    @classmethod
    def get_articles(cls, event, publication):
        """Get articles from a publication. Temporary func."""
        print(event.widget.__dict__)

        print("TEST POINT: Get article from: ", publication)
