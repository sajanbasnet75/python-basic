#dictionary contains a unique key as a index and this key can conatin a value
#creating a dictionary

animals={'cats':'companian',
         'dogs':'security',
         'cows':'milk',
         'goats':'meat'
         }

print("before adding")
print(animals)

print(animals['cats'])
#add and edit to dictionary

animals['sheep']='wool'
print("after adding")
print(animals)
#removing from dict
del(animals['goats'])
print("after del")
print(animals)

#dictionary inside dictionary

asia={'china':{'popn':'12.2','language':'chienese'},
      'nepal':{'popn':'3.0','language':'neplease'}
    }
print(asia)
#adding data above
data={
     'popn':'4.4',
     'language':'indian'
    }
asia['india']=data
print(asia['nepal'])
print(asia)
