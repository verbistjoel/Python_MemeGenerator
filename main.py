"""Meme master file."""
import os
import random
import argparse
from pathlib import Path
from QuoteEngine import Ingestor
from QuoteEngine import QuoteModel
from MemeEngine import MemeEngine


def generate_meme(pth=None, bdy=None, auth=None):
    """Generate a meme given an path and a quote.

    takes random image from the image folder, a
    random quote from the quote folder and creates a meme
    object using the image, quote and author of quote.

    if args are passed via the command line then it will use those
    args to generate the meme.
    Options are to pass --path PATH, --body QUOTE, --author AUTHOR
    if --body is passed then --author is required.

    if no args are passed via command line then defaults are used

    :param pth: path to image folder
    :param bdy: quote folder
    :param auth: author name
    """
    if pth is None:
        images = "./_data/photos/"
    else:
        if os.path.isdir(pth):
            images = pth
        else:
            raise Exception('Not a valid Image directory')

    imgs = []
    for root, dirs, files in os.walk(images):
        imgs = [os.path.join(root, name) for name in files]
    img = random.choice(imgs)

    if bdy is None:
        quote_files = ['./_data/Quotes/QuotesTXT.txt',
                       './_data/Quotes/QuotesDOCX.docx',
                       './_data/Quotes/QuotesPDF.pdf',
                       './_data/Quotes/QuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))
        quote = random.choice(quotes)
    else:
        if auth is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(bdy, auth)

    meme = MemeEngine('./tmp')
    pth = meme.make_meme(img, quote.body, quote.author)
    return pth


if __name__ == "__main__":
    """Command line argparser if args are passed."""
    parser = argparse.ArgumentParser(description='Create a meme')
    parser.add_argument('--path', type=Path, default=None,
                        help='path to pic')
    parser.add_argument('--body', nargs='+', type=str, default=None,
                        help='text quote')
    parser.add_argument('--author', nargs='+', type=str, default=None,
                        help='author of quote')
    args = parser.parse_args()

    path = args.path
    body = args.body
    author = args.author

    if path is not None:
        path = str(path)

    if body is not None:
        bd = ''
        for word in body:
            bd += word + ' '
        body = bd.strip().strip("'")

    if author is not None:
        at = ''
        for athr in author:
            at += athr + ' '
        author = at.strip().strip("'")

    print(generate_meme(path, body, author))
else:
    print(generate_meme())
