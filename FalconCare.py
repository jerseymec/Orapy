import sys
import codecs
from tkinter import  filedialog
import os
import time
import datetime
import shutil
import pyodbc as db

root = Tk()
root.filename = filedialog.askopenfilename()
basename=os.path.basename(root.filename)
pathname=os.path.dirname(root.filename)

thepath=os.path.dirname(root.filename)
foldername=os.path.basename(thepath)

path=pathname
filename = root.filename

print(pathname)
print(filename)
print(foldername)

Button(root, text="Process the file", command=root.destroy).pack()
root.mainloop()

filenew=filename
print(filenew)

def add_ClaimantName():
    infile=open(filename, 'r') # open file for appending
    outfile = open(filenew, "a") # open file for appending
    outfile.write(infile.read().replace("\n",',""\n'))
    infile.close()
    outfile.close()
    print(:extra comma added")

##read the input file
#loop through for each row and query external database to create a new index file

def readfileCreatenewfile(filenew, thepath, pathname):
##
##          #infile =open(filenew, 'r') #open file for appending
##          #outfile= open(filenew,"a") #open file for appending
##

          file_name, file_extension = os.path.splitext(filenew)
          newfile = file_name + "_NewFinal.txt"
          errorfile= file_name + "_Error.txt"

          connection= db.connect('DRIVER={ODBC Driver 11 for SQL Server}; SERVER=TEB-FALCONBID;Trusted_Connection=yes;DATABASE=DFJ_stgFACTS;uid=Onbase_User;Onbase_2018$')
          cur = connection.cursor()

                  with open(filenew,'r') as f:
                       with open(newfile, "w") as f1:
                             with open(errorfile,"w") as f2:
                                        for line in f:
                                             try:
                                                  #line=line.replace('""','')
                                              #line= line.replace('"','')
                                              #list_of_items_in_line = line.strip().split(",")

                                               list_of_items_in_line = line.strip().split("|")
                                               claim_number = list_of_items_in_line[0]
                                               pfd_file = list_of_items_in_line[9]
                                               list_of_lines_in_line[10] = ""

                                               claim_number = claim_number.replace('"','')
                                               #print(claim_number)
                                               #SQLCommand = ("SELECT WorkOrder,ClaimDate, AircraftType,AircraftSerail, PartRemoved, SNRemoved FROM [Onbase].[vw_SRWC] WHERE claimnumber=?")  
                                                SQLCommand = (
                                                    "SELECT WorkOrder,ClaimDate,AircraftType, AircraftSerail,PartRemoved, SNRemoved FROM [Onbase].[vw_SRWC] WHERE claimnumber =")
                                                SQLCommand = SQLCommand + "'"+ claim_number + "'"                                
                                                #Values = [claim_number]
                                                #print(Values)
                                                # cur.execute(SQLCommand, Values)
                                                #print(SQLCommand)

                                                cur.execute(SQLCommand)
                                                results = cur.fetchone()
                                                #if resilts is not None:
                                                    #print (results)
                                                    #while results:
                                                       #print(str(results[0])+" "+ str(results[1])+" "+ str(results[2])
                                                       #results = cur.fetchone()
                                                list_of_items_in_line[1] = results[0].strip() #workorder
                                                list_of_items_in_line[2] = results[1] #claimDate
                                                list_of_items_in_line[3] = str(results[2].strip()) #aircraftmodel
                                                list_of_items_in_line[4] = results[3].strip() #circraftSerialNumber
                                                list_of_items_in_line[5] = results[4].strip() #partRemoved
                                                list_of_items_in_line[6] = results[5].strip() #snRemoved

                                                newline = "|".join(str(i) for i in list_of_items_in_line)
                                                f1.write(newline+ '\n')
                                             except:
                                                f2.write(line + '\n')
          f.close()
          f1.close()
          f2.close()
          connection.close()
          print("Done")


readfileCreatnewFile(filenew,thepath, pathname)
          

