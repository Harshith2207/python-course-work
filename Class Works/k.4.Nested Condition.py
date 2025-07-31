#4. Nested Conditional Statements

#Influencer level Detection...

followers = int(input("Enter your Instagram followers count: "))
print("Welcome to the Instagram Kiddooo...\nThanks for using Instagram!")
if followers > 0:
    print("...")
    if followers>1000000:
        print("You're an Influencer God!!! Salaam Rocky Bhai")
    elif followers>100000:
        print("Influencer detected: CEO of Reels, Nice To Meet you Sarkaar!")
    elif followers>10000:
        print("Influencer detected: You can start earning now & buy Alekhya Chitti Pickles...")
    elif followers>1000:
        print("Just a reel away from going viral. Keep posting viral stuff!")
    elif followers>100:
        print("You can't buy Alekhya Chitti Pickles!!!")
    else:
        print("I know kiddooo that You’re here for fun")
else:
    print("No followers? Are You Stalking your EX brooo ??")


