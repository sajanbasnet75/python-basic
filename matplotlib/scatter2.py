import matplotlib.pyplot as plt
import numpy as np
dict = {
    'Asia':'red',
    'Europe':'green',
    'Africa':'blue',
    'Americas':'yellow',
    'Oceania':'black'
}

year=[2011,2012,2013,2014,2015]
popn=[1.2,2.2,3.2,4.2]

life_exp=[10,20,30,40,50]
np_pop=np.array(popn)
np_pop=np_pop*10
plt.scatter(year,life_exp,s=np_pop)
plt.xlabel("Year")
plt.ylabel("Life expectancy")
plt.xticks(year,['2011 AD','2012 AD','2013 AD','2014 AD','2015 AD'])
#plt.xticks([1000,10000,100000], ['1k','10k','100k'])


plt.xscale('log')
plt.grid(True)
plt.show()
