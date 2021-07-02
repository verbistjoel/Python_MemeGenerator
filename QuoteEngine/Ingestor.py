"""Ingestor of quotes from possible file types."""
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .DOCXIngestor import DOCXIngestor
from .CSVIngestor import CSVIngestor
from .TXTIngestor import TXTIngestor
from .PDFIngestor import PDFIngestor


class Ingestor(IngestorInterface):
    """Inherets abstract class IngestorInterface.

    chooses correct file type ingestor to ingest quotes
    """

    importers = [CSVIngestor, DOCXIngestor, TXTIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse quote file using correct ingestor.

        :param path: path to quote file
        """
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)
        return 'Not a valid file extension. please use txt, pdf, ' \
               'docx, or csv files'
