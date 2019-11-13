import os
from collections import Counter
import matplotlib.pyplot as plt

#from typing import List, Tuple

print(os.getcwd())

totalsize = 0
FileTypes = []
Listfile = os.listdir('L:\\My Documents')

for Lf in Listfile :
     if (Lf.find('.') != -1 ):
       splitfiles = Lf.split('.')
       FileTypes.append(splitfiles)


extensions = [x[1] for x  in FileTypes]
print(extensions)

#FileTypes1= [lf for Lf in Listfile  Lf.split('.')]

FileTCounts = {}

FileTCounts =   Counter(extensions)
print(FileTCounts)

xs = range(200)
ext_length=len(FileTCounts)

xaxis = list(FileTCounts.keys())

print(xaxis)

ys = list(FileTCounts.values())
plt.bar(xaxis,ys)
plt.ylabel("# of files")
plt.show()


for filename in os.listdir('L:\\My Documents'):
    totalsize += os.path.getsize(os.path.join('L:\\MY Documents',filename))

print(totalsize)