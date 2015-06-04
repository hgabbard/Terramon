#!/usr/bin/env python
# Parse earthquake data files and output an HTML file.
# Requires PANDAS library, which is part of iPython distribution.
#
# Author: Hunter Gabbard <hunter.gabbard@ligo.org>
# Time-stamp: <2015-03-25 15:14:08 bnp>
#
# ./earthquakes2html.py 1109300301-1110423501

import sys
import os
import os.path
import pandas as pd
from time import gmtime, strftime
import commands
import string
import csv


#Current time calculation
time = strftime("%Y-%m-%d %H:%M:%S")

# Column names to use in HTML table
col_names = ['GPS Time', 'Magnitude', 'P-phase Arrival', 'S-phase Arrival',
             'R- 2 km/s', 'R 3.5 km/s', 'R 5 km/s', 'R-wave amplitude in m/s',
             'Arrival floor', 'Departure ceil', 'EQ lat', 'EQ lon', 'EQ distance',
             'ifo']

# Function to open HTML file and output beginning of HTML file
def start_html_file(title, filename):
    file = open(filename, 'w')
    file.write('<html>')
    file.write('<head><title>Earthquake data: </title></head>')
    file.write('<body>')
    file.write('<h1>Earthquake data: </h1>')
    #file.write('<table border="5">')
    #file.write('<th> GPS time </th>')
    #file.write('<th> MAGNITUDE </th> <th> P-phase Arrival </th> <th> S-phase Arrival </th> <th> R 3.5 km/s </th> <th> R-wave amplitude in m/s </th> <th> EQ lat </th> <th> EQ lon </th> <th> EQ distance </th> <th> ifo </th>')
    return file
   
    
# Function to write end of HTML file and close file
def end_html_file(file):
    file.write('</body>')
    file.write('</html>')
    file.close()

def process_sub_dir(dir, file):
    # Attempt to open earthquakes.txt in dir
    efilename = os.path.join(dir, 'earthquakes.txt')
    #store values
    a = open(efilename,"r")
    global b
    b = a.readlines()
    global c1
    global c2
    global c3
    global c4
    c1 = b[0].split(" ")
    
    c2 = b[1].split(" ")
    c3 = b[2].split(" ")
    c4 = b[3].split(" ")
    print c1
    global latitude
    global longitude
    global GPS
    global Mag
    global P_phas
    global s_phas
    global R3
    global Ramp
    global EQ_dis
    global ifo 
    latitude = c1[10]
    longitude = c1[11]
    GPS = c1[0]
    Mag = c1[1]
    P_phas = c1[2]
    s_phas = c1[3]
    R3 = c1[5]
    Ramp = c1[7]
    EQ_dis = c1[12]
    ifo = c1[13]
    #file_n = open(main_dir + '/crazy.html', 'w')
    #file.write('Hello World')

    
    try:
        input = open(efilename)
    except:
        print dir, 'does not contain an earthquakes.txt file!'
    else:
        # Get name of directory for table header
        local_title = os.path.basename(dir)
	conv_title = local_title.replace(local_title[:4], '')
	integer_title = int(conv_title)
	#print integer_title
	New_title = commands.getstatusoutput("lalapps_tconvert --local --zone=UTC %d" % (integer_title))
	#link_time = commands.getstatusoutput("tconvert -f %m" integer_title) 
	link_time = commands.getstatusoutput("lalapps_tconvert --local --zone=UTC -f%%Y-%%m-%%d-%%H-%%M-%%S %d" % (integer_title))
	#print link_time
	link_time = str(link_time)
	link_time = link_time.replace(link_time[:5], '')
	link_time = link_time.replace(link_time[19:], '')
	link_time = link_time.split("-")
	link_year = link_time[0]
	link_month = link_time[1]
	link_day = link_time[2]
	link_hour = link_time[3]
	link_minute = link_time[4]
	link_sec = link_time[5]
	link_sec_min1 = int(link_sec) - 5
	link_sec_plus1 = int(link_sec) + 5
	if link_sec_plus1 > 60:
		link_sec_plus1 = link_sec_plus1 - 60
		link_minute_plus1 = int(link_minute) + 1
		web_link = "http://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&starttime=%s-%s-%s%%20%s%%3A%s%%3A%s&minmagnitude=3&endtime=%s-%s-%s%%20%s%%3A%s%%3A%s" % (link_year, link_month, link_day, link_hour, link_minute, link_sec_min1, link_year, link_month, link_day, link_hour, link_minute_plus1, link_sec_plus1)
	elif link_sec_min1 < 0:
		link_sec_min1 = link_sec_min1 + 60
		link_minute_min1 = int(link_minute) - 1	
		web_link = "http://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&starttime=%s-%s-%s%%20%s%%3A%s%%3A%s&minmagnitude=3&endtime=%s-%s-%s%%20%s%%3A%s%%3A%s" % (link_year, link_month, link_day, link_hour, link_minute_min1, link_sec_min1, link_year, link_month, link_day, link_hour, link_minute, link_sec_plus1)
	elif link_sec_plus1 > 60 and link_sec_min1 < 0:
		link_sec_plus1 = link_sec_plus1 - 60
		link_minute_plus1 = int(link_minute) + 1
		link_minute_min1 = int(link_minute) -1
		web_link = "http://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&starttime=%s-%s-%s%%20%s%%3A%s%%3A%s&minmagnitude=3&endtime=%s-%s-%s%%20%s%%3A%s%%3A%s" % (link_year, link_month, link_day, link_hour, link_minute_min1, link_sec_min1, link_year, link_month, link_day, link_hour, link_minute_plus1, link_sec_plus1)
	  
	else:
		web_link = "http://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&starttime=%s-%s-%s%%20%s%%3A%s%%3A%s&minmagnitude=3&endtime=%s-%s-%s%%20%s%%3A%s%%3A%s" % (link_year, link_month, link_day, link_hour, link_minute, link_sec_min1, link_year, link_month, link_day, link_hour, link_minute, link_sec_plus1)
	#print web_link

	#Getting csv files for human readable location
	os.system("rm /home/hunter.gabbard/public_html/earthquake_mon/event_csvs/event.csv")
	os.system("wget '%s' -O /home/hunter.gabbard/public_html/earthquake_mon/event_csvs/event.csv" % web_link)
	#crs = open("/home/hunter.gabbard/public_html/earthquake_mon/event_csvs/event.txt", "r")
	try:
		with open('/home/hunter.gabbard/public_html/earthquake_mon/event_csvs/event.csv', 'rb') as csvfile:
        		reader = csv.reader(csvfile)
			reader = list(reader)
			id = reader[1][11]
			place = reader[1][13]
			USGSmap_link = "http://earthquake.usgs.gov/earthquakes/eventpage/%s#general_map" % id
	except:
		place = ""
		USGSmap_link = ""
		pass
			
	#print id
	new_title = str(New_title)
	blah = new_title.replace(new_title[:5], '')
	event_title = blah.replace(blah[28:], '')

	#Get human readble location 
	#latf=float(c1[10])
	#lonf=float(c1[11])
	#destination = Geocoder.reverse_geocode(latf, lonf)
	#print destination[0]
        # Read earthquakes.txt
        table = pd.read_table(efilename, sep=' ', names=col_names)
	
        # Write subtitle for table
        file.write('<h2>%s</h2>' % event_title)
	file.write('<h2>%s</h2>' % place)
	file.write('<a href="%s">USGS event link</a>' % USGSmap_link)
	
        # Write actual table to HTML file
        #file.write(table.to_html(index=False, columns=[0,1,2,3,5,7,10,11,12,13], col_space=80))
        file.write('<table border="5">')
        file.write('<th> GPS time </th> <th> MAGNITUDE </th> <th> P-phase Arrival </th> <th> S-phase Arrival </th> <th> R 3.5 km/s </th> <th> R-wave amplitude in m/s </th> <th> EQ lat </th> <th> EQ lon </th> <th> EQ distance </th> <th> ifo </th>')
        file.write('<tr>')
        for i in range(len(c1)):
            if i == 0 or i == 1 or i == 2 or i == 3 or i == 5 or i == 10 or i == 11 or i == 13:
                file.write('<td>' + c1[i] + '</td>')
            elif i == 7:
                x7=float(c1[i]) * (10**6)
                c1[i]=str(x7)
		if x7 < 0.5:
		    file.write('<td bgcolor="#00FF00">' + c1[i] + '</td>')
		elif x7 >= 0.5:
		    file.write('<td bgcolor="#FF0000">' + c1[i] + '</td>')
	    elif i == 12:
		x12=float(c1[i]) * (10**-3)
		c1[i]=str(x12)
		file.write('<td>' + c1[i] + '</td>')
        file.write('</tr>')
        file.write('<tr>')
        for i in range(len(c2)):
            if i == 0 or i == 1 or i == 2 or i == 3 or i == 5 or i == 10 or i == 11 or i == 12 or i == 13:
                file.write('<td>' + c2[i] + '</td>')
	    elif i == 7:
		y7=float(c2[i]) * (10**6)
		c2[i]=str(y7)
		file.write('<td>' + c2[i] + '</td>')
        file.write('</tr>')
        file.write('<tr>')
        for i in range(len(c3)):
            if i == 0 or i == 1 or i == 2 or i == 3 or i == 5 or i == 7 or i == 10 or i == 11 or i == 12 or i == 13:
                file.write('<td>' + c3[i] + '</td>')
        file.write('</tr>')
        file.write('<tr>')
        for i in range(len(c4)):
            if i == 0 or i == 1 or i == 2 or i == 3 or i == 5 or i == 7 or i == 10 or i == 11 or i == 12 or i == 13:
                file.write('<td>' + c4[i] + '</td>')
        file.write('</tr>')  
        file.write('</table>')



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
    sub_dirs.sort(reverse=True)
    # Start HTML file
    file = start_html_file(sys.argv[1], main_dir + "/earthquakes.html")
    #file = start_html_file(sys.argv[1],  "/home/hunter.gabbard/public_html/earthquake_mon/html_pages/earthquakes.html")

    # Iterate through subdirectories
    for dir in sub_dirs:
        # Process each subdirectory, looking for earthquakes.txt
        process_sub_dir(os.path.join(main_dir, dir), file)

    # End HTML file
    end_html_file(file)


if __name__ == "__main__":
   main() 
