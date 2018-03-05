#
word="Sajan"
it=iter(word)

print(next(it))
print(next(it))


#iterating at once using can be done by using "*"

its=iter(word)
print(*its)


print("Example/n")
# Create a list of strings: flash
flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

print("Print each list item in flash using a for loop")
for person in range(len(flash)):
    print(flash[person])
    


# Create an iterator for flash: superspeed
superspeed=iter(flash)


print("Print each item from the flash using iterator")

print(next(superspeed))
print(next(superspeed))
print(next(superspeed))
print(next(superspeed))
