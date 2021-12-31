#!/usr/bin/env python3
#change to length of data - should be able to determine by first column
#convert everything to numpy? Try to get rid of error message?

#for plot
import matplotlib.pyplot as plt
import numpy as np

#for excel reading
import pandas
import math

import numpy

import os 

stream = os.popen("ls *.xlsx")
files = stream.readlines()

#    print(number.strip())



#change colors
#colors = ["darkorange", "teal", "royalblue", "slategrey", "navy", "red", "coral", "gold", "orchid", "greenyellow", "sandybrown", "maroon", "silver", "olivedrab", "tan", "firebrick", "khaki", "darkslategrey", "fuschi"]
colors = ["darkorange", "teal", "royalblue", "slategrey", "navy", "red", "gold", "orchid", "greenyellow", "sandybrown",  "firebrick", "darkslategrey", "pink"]


#I'm assuming that there are non nans after any nans
def last_valid(list_of_values):
   last=0
   for x in list_of_values:
	
      #check if it is a nan
      if math.isnan(x): #if it is, break
         break
      else: #if not, increment total, keep going
         last = last+1
   #return the last non-nan
   return last; 

def first_valid(list_of_values):
   first=0
   for x in list_of_values:
	
      #check if it is a nan
      if math.isnan(x): #if it is, keep going
         first = first+1
         continue
      else: #if not, increment total, break
         break
   #return the first non-nan
   return first; 


#I'm assuming that there are non nans after any nans
def print_nans(list_of_values):
   last=0
   for x in list_of_values:
	
      #check if it is a nan
      if math.isnan(x): # if it is, don't print anything, stop immediately
         break
      else:
         print(x)

#loop on everything matching xlsx in current directory
for name_of_file in files:
  name_of_file = name_of_file.strip()
  #old one took in a single file name
  #name_of_file=input()
  excel_data_df = pandas.read_excel(name_of_file, sheet_name='Sheet1')
  
  #set up plotting sizes
  plt.rc('font', size=12) 
  SIZE = 11
  plt.rc('legend', fontsize=SIZE)
  
  
  #read in A1, save as name
  col_names = excel_data_df.columns.ravel()
  
  #read in rest of first column - use this as X variable
  x_values = excel_data_df[col_names[0]]
  max_x=len(x_values)
  figure_name = str(col_names[0])
  
  
  
  #for labelling
  col_number=0
  #current number of line being plotted
  num_line = 0
  for x in col_names[1:]: #for each column that isn't the first
     #find the first row in the column that doesn't have a number - save this for this column (call it num_xs) - need it for plot later
     start_of_col = first_valid(excel_data_df[x])
     length_of_col = last_valid(excel_data_df[x][start_of_col:max_x])
     x_sub_values = numpy.asarray(x_values[start_of_col:start_of_col+length_of_col])
     y_sub_values = numpy.asarray(excel_data_df[x][start_of_col:start_of_col+length_of_col])
     plt.plot(x_sub_values,y_sub_values,label=x, color=colors[num_line])
     num_line=num_line+1
  
  
  #set up the plots of the graph
  plt.semilogy()
  plt.xlabel('Total Iterations')
  plt.ylabel('Residual Norm')
  
  plt.legend()
  plt.legend(loc='upper right')
  plt.savefig(figure_name + '.png', dpi = 500)
  plt.close()
  
  
  
