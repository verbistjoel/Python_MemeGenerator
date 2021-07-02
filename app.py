"""Flask interface, app creator."""
import random
import os
import requests
from flask import Flask, render_template, abort, request
from pathlib import Path
from QuoteEngine import Ingestor
from QuoteEngine import QuoteModel
from MemeEngine import MemeEngine
import urllib.request
from time import sleep
import validators

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/Quotes/QuotesTXT.txt',
                   './_data/Quotes/QuotesDOCX.docx',
                   './_data/Quotes/QuotesPDF.pdf',
                   './_data/Quotes/QuotesCSV.csv']

    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/"
    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)

    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme.

    -Uses requests to save the image from the image_url
    form param to a temp local file.
    -Uses the meme object to generate a meme using this temp
    file and the body and author form parameters.
    -Removes the temporary saved image.
    """
    data = request.form
    img = str(data['image_url'])

    valid = validators.url(img)  # checks if valid url structure
    if not valid:
        print("Not a valid URL")
        return render_template('meme_form.html')

    filepath = f'./tmp/{random.randint(0, 1000000)}'
    urllib.request.urlretrieve(img, filepath)

    body = str(data['body'])
    author = str(data['author'])
    qt = random.choice(quotes)
    print(f'body: {body}, auhor: {author}')
    if img != '' or img is None:
        if (author == '' or author is None) and (body == '' or
                                                 body is None):
            author = qt.author
            quote = qt.body
        elif author != '' and (body == '' or body is None):
            author = qt.author
            quote = qt.body
        elif body != '' and (author == '' or author is None):
            author = 'Unknown'
            quote = body
        elif body != '' and author != '':
            author = author
            quote = body

    path = meme.make_meme(filepath, quote, author)

    start_removal(filepath)
    return render_template('meme.html', path=path)


def start_removal(filepath):
    """Remove temp file after slight delay."""
    sleep(1)
    os.remove(filepath)
    pass


quotes, imgs = setup()

if __name__ == "__main__":
    app.run()
