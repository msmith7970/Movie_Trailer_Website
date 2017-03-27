# Project Movie Trailer website

Project Movie Trailer website utilizes server side code (fresh_tomatoes.py)
to display six of my favorite movies on a dynamically generated website
where the data for these movies are stored using Classes.  The data for the
movies is contained in the entertainment_center.py file and the "Movie" Class
in contained in the media.py file.

## Instructions

1) Install Python 2.7.x. Instructions for installing Python can be found
  [here](https://www.python.org/downloads/).  
2) Download and install these three files to a PC that has Python installed
  to the same directory.  These three files are:

    1) fresh_tomatores.py
    2) entertainment_center.py
    3) media.py

Unzip the zip file titled "media" in the same folder on your PC.
Once these three files are installed and to see the results, follow pythons
normal practice to run the file called 'entertainment.py'.

## Usage
The file entertainment.py contains the information to define the instance of
six movie titles.  

The six pieces of information for each movie instance are:

    1) Movie Title
    2) Storyline
    3) The movies poster image
    4) the Youtube URL of the movie trailer
    5) the index to the global variable called VALID_RATINGS that contains
       the rating of the movie (where 0 = 'G', 1 = 'PG', 2 = 'PG-13 and 3 = 'R'
    6) the ratings given to a movie from the Rotten Tomatoes website as defined
       as the Tomatometer.

The file fresh_tomatoes.py is file that displays all the instance of a movie as
defined from the enterainment.py file into a format that is easily viewed
as a HTML file in a web browser.

The media.py file defines the Movie class and initializes the data
associated with the instance.

## License

The content of this repository is licensed under MIT License.

Copyright (c) 2017 Mitchell Smith

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
