import cx_Oracle
con = cx_Oracle.connect ( "system/zx11203Respec1q@ESPEC1Q_SLPAR2")
cur = con.cursor()
cur.execute("select * from cat")
i=0
results = cur.fetchone()
#while (cur.fetchone()) :
while (results):
    print(results)
    i += 1
    results = cur.fetchone()

print ("Total = " +str(i))
