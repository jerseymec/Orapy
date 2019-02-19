import ftplib
import os
import shutil

print(shutil.get_archive_formats())

ftp = ftplib.FTP('192.170.1.155','oracle','noponen')
ftp.cwd('/bckup/ESPEC1P/export/')
ftp.dir()
filename = 'ESPEC1P_01.dmp'
savedir='N:\ESPEC'

os.chdir(savedir)
#print(str(os.curdir())

print(os.getcwd())
file= open(filename,"wb")
ftp.retrbinary("RETR " + filename , file.write)
file.close()
ftp.close()
