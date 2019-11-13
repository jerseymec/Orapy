import csv

fieldnames = ['Company','Voucher Type','Voucher Number','Accounting Year']
with open('DeleteVouchers.sql','w') as scriptfile:

    with open('Vouchers.csv','r') as f :
        next(f,None)
        next(f,None)
        next(f,None)
        Dictcsv = csv.DictReader(f )
        #rows = Dictcsv[1]
        #size = len(rows)
        #print("size = ", size)
        print ("begin ")
        scriptfile.write(    "begin \n")
        for row in Dictcsv:
            #print(row[fieldnames[0]]+" "+ row[fieldnames[1]]+" "+ row[fieldnames[2]]+" "+ row[fieldnames[3]])
            print( "dfj_remove_voucher_api.remove_voucher('"+row[fieldnames[0]]+"', '"+row[fieldnames[1]]+"', '"+row[fieldnames[2]]+"',"+row[fieldnames[3]]+");")
            row = "dfj_remove_voucher_api.remove_voucher('"+row[fieldnames[0]]+"', '"+row[fieldnames[1]]+"', '"+row[fieldnames[2]]+"',"+row[fieldnames[3]]+"); \n"
            scriptfile.write(row)

        print("end; ")
        scriptfile.write("end; \n")
        scriptfile.write("commit; \n")
    f.close()
scriptfile.close()
