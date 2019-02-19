investment = input("Enter an Investment amount: ")
Investment = float(investment)
rate = float(input("Enter the expected rate : ")) *.01
years = int(input("Enter the number of years you want to invest : "))

for i in range(years):
    Investment = Investment + (Investment * rate)
print (" After " + str(years) + " years your investment will be : {:.2f}". format(Investment))


#print ("Round to 2 decim3.5als :1000 {:2f}".format(your_float))