#!/usr/bin/env python
# Parse earthquake data files and output an HTML file.
# Requires PANDAS library, which is part of iPython distribution.
#
# Primary Author: Ben Pharr <bnpharr@olemiss.edu>
# Secondary Author: Hunter Gabbard <hunter.gabbard@ligo.org>
# Time-stamp: <2015-03-25 15:14:08 bnp>
#
# ./earthquakes2html.py 1109300301-1110423501

import sys
import os
import os.path
import pandas as pd

# Column names to use in HTML table
col_names = ['GPS Time', 'Magnitude', 'P-phase Arrival', 'S-phase Arrival',
             'R- 2 km/s', 'R 3.5 km/s', 'R 5 km/s', 'R-wave amplitude in m/s',
             'Arrival floor', 'Departure ceil', 'EQ lat', 'EQ lon', 'EQ distance',
             'ifo']

# Function to open HTML file and output beginning of HTML file
def start_html_file(title, filename):
    file = open(filename, 'w')
    file.write('<html>')
    file.write('<head><title>Earthquake data: %s</title></head>' % title)
    file.write('<body>')
    file.write('<h1>Earthquake data: %s</h1>' % title)
    return file

# Function to write end of HTML file and close file
def end_html_file(file):
    file.write('</body>')
    file.write('</html>')
    file.close()

def process_sub_dir(dir, file):
    # Attempt to open earthquakes.txt in dir
    efilename = os.path.join(dir, 'earthquakes.txt')
    try:
        input = open(efilename)
    except:
        print dir, 'does not contain an earthquakes.txt file!'
    else:
        # Get name of directory for table header
        local_title = os.path.basename(dir)

        # Read earthquakes.txt
        table = pd.read_table(efilename, sep=' ', names=col_names)

        # Write subtitle for table
        file.write('<h2>%s</h2>' % local_title)

        # Write actual table to HTML file
        file.write(table.to_html(index=False))


# Main function
def main():
    # Get directory to process from user via command line argument
    if len(sys.argv) < 2:
        print 'Please provide a directory to process as a command line argument.'
        print 'Example: ./earthquakes2html.py 1109300301-1110423501'
        exit(1)
    main_dir = sys.argv[1] + '/earthquakes'

    # Get list of subdirectories in earthquakes directory
    # (using a list comprehension)
    sub_dirs = [ f for f in os.listdir(main_dir)
                 if os.path.isdir(os.path.join(main_dir, f)) ]

    # Start HTML file
    file = start_html_file(sys.argv[1], main_dir + "/earthquakes.html")

    # Iterate through subdirectories
    for dir in sub_dirs:
        # Process each subdirectory, looking for earthquakes.txt
        process_sub_dir(os.path.join(main_dir, dir), file)

    # End HTML file
    end_html_file(file)


if __name__ == "__main__":
   main() 
