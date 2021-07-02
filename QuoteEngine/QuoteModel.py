"""Quote Model Class."""


class QuoteModel():
    """Master Quote Model Class."""

    def __init__(self, body, author):
        """Initialize class.

        :param body: quote text
        :param author: author
        """
        self.body = body
        self.author = author

    def __repr__(self):
        """Print object in meaningful manner."""
        return f'<{self.body} --{self.author}>'
