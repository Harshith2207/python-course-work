#Generators
''' To save memory Generators are used '''
''' Yield pause the output returns the function'''

def show_feed(l):
    for i in l:
        yield i
        
reels=['001..100','101..200','201..300','301..400','401..500']
nextfeed=show_feed(reels)

print(next(nextfeed)) #variable declaration passing
print(next(nextfeed))
print(next(nextfeed))
print(next(nextfeed))
print(next(nextfeed))


def show_feed(l):
    for i in l:
        start,end=i.split('..')
        reelsofi=[i for i in range(int(start),int(end)+1)]
        yield reelsofi
        
reels=['001..100','101..200','201..300','301..400','401..500','501..600','601..700','701..800','801..900']
nextfeed=show_feed(reels)

while True:
    scroll=input("[c]ontinue / [e]xit: ")
    if scroll=='c':
        print(next(nextfeed))
    else:
        break
        
print(next(nextfeed)) #variable declaration passing
print(next(nextfeed))
print(next(nextfeed))
print(next(nextfeed))
print(next(nextfeed))

