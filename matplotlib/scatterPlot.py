import matplotlib.pyplot as plt
year=[2011,2012,2013,2014]
popn=[1.2,2.2,3.2,4.2]
plt.scatter(year,popn)
plt.xscale('log')
plt.xlabel("year")
plt.ylabel("population")

plt.title("Population Graph")
plt.yticks([0,1,2,3,4,5],['0','1Billion','2Billion','3Billion','4Billion','5Billion'])
plt.xticks(year,['2011AD','2012AD','2013AD','2014AD',])

plt.show()
