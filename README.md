
OVERVIEW

This project is a "meme generator" – a multimedia application to dynamically generate memes, 
including an image with an overlaid quote. It will either create a randomly generated meme (choose a picture
and a quote at random) from within a default selection of images and quotes to be found in the _data folder. 
One can also supply a path to an image of choice and / or both a quote and author to generate a meme of 
choice. If a quote is supplied then an author is also required.

If no path to an image is supplied, a random default selection will be made from the pictures
in the _data/Photos folder. if no quote and author are supplied then a random selection will be made from
one of the quotes (and authors) available in one of the files within the _data/Quotes folder.

In addition, a flask application is built that allows direct output to a webpage (if so desired). For 
instructions and description of the flask app see end of this file. 

INSTRUCTIONS

Simply run 'main.py' from the command line  (ex. $python3 main.py)
Make sure all folders (with all files) are available and copied in same relative folder structure as:

- main.py  (python file)
- QuotesEngine (folder containing quote engine files)
- MemeEgnine (folder containing meme generator files)
- _data (folder containing folders with quote and photo data files)
- tmp (folder that is originall empty but will contain meme output picture)

Command line arguments can be passed to customize the meme.  One can provide a path to the picture to
be used and/or a quote with author.  NOTE: when a quote is passed as a command line argument then an 
author is also required. 
Options:  
- --path PATH
- --body QUOTE
- --author AUTHOR

ex.  $python3 main.py --path ./_data/Otherpics   OR   $python3 main.py --body Life is good --author J. Smith

Note that if --body is passed then --author is required.

DESCRIPTION

The meme generator can interact with a variety of complex filetypes. 
- It can load quotes from a variety of filetypes (PDF, Word Documents, CSVs, Text files). 
- Load, manipulate, and save images
- Accept dynamic user input through a command-line tool and a web service. 

Let's look at these in more detail.

1. Default data for both the pictures and quotes can be found in the _data folder.  Quotes are found in 
the quotes folder. Note quotes are found in Txt, Word (docx), csv, and pdf format.  Pictures can be found in the Photos folder. 
   

2. The QuoteEngine folder contains all the files necessary to ingest the quotes found in the Quotes folder (or passed via command line).
The Quote Engine module is responsible for ingesting many types of files that contain quotes. For our purposes, a quote contains a body and an author.
  
Ingestor Interface:
  
   An abstract base class, IngestorInterface defines two methods with the following class method signatures
    -  can_ingest: check to see if the file type (ext) is a valid type 
    -  parse: which just passes through since the actual will happen in the file type ingestor files

Ingestor:

Inherets from the abstract IngestorInterface class and set up the ingestor class object. 
Method Parse selects the correct file type ingestor from one of the available importers and parse the quote 
file

CSVIngestor, DOCXIngestor, TXTIngestor, PDFIngestor:

Methods Parse parses the relevant file type into individual quotes and authors and creates a list of QuoteModel 
objects containing the Quote and the author (as .body and .author in QuoteModel class)

QuoteModel:

sets up the QuoteModel class. this instantiates a QuoteModel object containing the quote (body) and author.

Method __repr__ allows us to print a readable formatted form of the object

3. MemeEngine folder contains the MemeEngine which grabs the picture, manipulates it to a width fo 500px, 
adds a provided quote and author and places it on the picture. Then the picture is saved to the ./tmp directory
   and the file name path of the picture is returned and printed.
   
At initialization of the MemeEngine class only the output path of the meme picture is instantiated. 

The make_meme method will open the picture to be used as the meme, manipulates is to a max 500px width
(holding all aspects constant), overlays the provided quote and author, and save the file in the output 
path.

4. main.py in the root directory contains the generate_meme method which will either use default path to an 
image directory and quotes or the provided arguments passed via the command line. It will take one random
   image and one random quote and create the meme, all using the classes and method provided in QuoteEngine
   and MemeEngine folders.
   Meme picture File will be saved in the ./tmp folder as a jpg

The requirements.txt file contains versions of all libraries used

FLASK APP

The app.py application in the root directory is the flask application that takes the meme generator and wraps
it in a web application. To run it just run at the command line. Then click on the generated url to open the
web page and engage with it.

As you will see a random meme is generated. You can then generate other random memes by clicking the 'Random'
button or create your own custom one by clicking the 'Creator' button and filling out the form.

All images created from within the app will be saved in the ./static folder as jpgs

The app uses the following files and folders. In addition to all the files and folders for the
Meme generator (see above), make sure that the following files and folders are also included: 

- app.py  (python file which generates the flask app)
- templates folder (contains the necessary html files to create the webpages)
- static folder (originally empty folder which will hold the generated memes)

Method setup loads all necessary resources (both images and quotes)

Method meme_random generates a random meme to be displayed on the webpage

Method meme_post grabs the entries from the form (url path, quote, and author) to be used to generate a meme

Method meme_form renders the form in which the user can input the url path (to the image), and type in the 
quote and author for the meme to be generated

