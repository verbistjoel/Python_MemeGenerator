"""DOCX reader, importer, or ingestor."""
from typing import List
import docx
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DOCXIngestor(IngestorInterface):
    """Ingest the quotes and authors from a Word document.

    Opens a Word doc and parses it line by line into quote and
    author.
    """

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse word doc in quotes and authors.

        :param path: path to word file
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split('-')
                new_quote = QuoteModel(parse[0].replace('"', ''),
                                       parse[1].strip())
                quotes.append(new_quote)

        return quotes
