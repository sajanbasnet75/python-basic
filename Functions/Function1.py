def out(word):
    print("i am outside")
    def inside(word2):
        print("i am "+str(word2))
         
    return inside    
ins=out("outside")
ins("inside")
