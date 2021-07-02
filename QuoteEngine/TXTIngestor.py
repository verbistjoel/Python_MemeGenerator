"""txt file reader, importer, or ingestor."""
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TXTIngestor(IngestorInterface):
    """Ingest the quotes and authors from a txt document.

    Opens a txt file and parses it line by line into quote and
    author.
    """

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse txt file in quotes and authors.

        :param path: path to txt file
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        with open(path, 'r', encoding='utf-8') as infile:
            contents = infile.read()
        lines = contents.split('\n')

        for line in lines:
            if line != "":
                parse = line.split('-')
                new_quote = QuoteModel(parse[0].strip(),
                                       parse[1].strip())
                quotes.append(new_quote)

        return quotes
