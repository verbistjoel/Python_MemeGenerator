"""Meme Engine."""
from PIL import Image, ImageDraw, ImageFont
import random


class MemeEngine():
    """Generates the Meme - pic and quote.

    The MemeEngine generates the picture and overlay quote.
    Grabs the picture from the provided path and resizes it,
    if necessary, to max width of 500px. Then it takes the provided
    text (body) quote and author and overlays it on the pic.
    Finally the picture gets saved as jpg in the tmp folder and the
    path the the picture is provided.
    """

    def __init__(self, out_path):
        """Initialize MemeEngine class."""
        self.out_path = out_path

    def make_meme(self, img_path, text, author, width=500):
        """Make meme method - will generate meme, pic and quote.

        The MemeEngine generates the picture and overlay quote.
        Grabs the picture from the provided path and resizes it,
        if necessary, to max width of 500px. Then it takes the provided
        text (body) quote and author and overlays it on the pic.
        Finally the picture gets saved as jpg in the tmp folder and the
        path the the picture is provided.

        :param img_path: path to the image
        :param text: the quote to be overlay (body)
        :param author: the auhor of the quote
        :param width: this is optional and max of 500
        """
        with Image.open(img_path) as im:
            # Provide the target width and height of the image
            new_width = int(width)
            new_height = int(new_width * im.height / im.width)
            (width, height) = (new_width, new_height)
            im_resized = im.resize((width, height))
            im = im_resized

            # get a font
            fnt = ImageFont.truetype("Pillow/Tests/fonts/arial.ttf",
                                     24)
            # get a drawing context
            d = ImageDraw.Draw(im)

            # draw text
            msg = f'{text} --{author}'
            if len(msg) > 35:
                left, right = msg[:35], msg[35:]
                r = right.split(" ", 1)
                try:
                    msg = f'{left}{r[0]} \n{r[1]}'
                except IndexError:
                    msg = f'{msg}'
            d.text((10, 100), msg, font=fnt, color='White')

            tmp = f'{self.out_path}/{random.randint(0, 1000000)}.jpg'
            im.save(tmp)
            return tmp
