
# instructions for running pycharm successfully
# source /usr/local/bin/oraenv
#echo $ORACLE_BASE
# if it returns value then oracle environment is set
# then start pycharm
#pycharm.sh
import cx_Oracle

conn = cx_Oracle.connect ('system/zx9204Rwasdbp@XE')
print (conn.version)
cur = conn.cursor()
cur.execute('select * from dba_users')
for results in cur:
     if str(results[11]) == "SYS_GROUP":
         print ("This is a POWER USER: ", str(results[0]))
     elif str(results[11]) == 'DEFAULT':
         print("This is a Reg User :", results[1])
     else:
         print("This is a other USER: ", results[1])
cur.close()


conn.close()