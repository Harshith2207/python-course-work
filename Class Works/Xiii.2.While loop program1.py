bullets=10
while bullets>0:
    if bullets<3:
        print("User dead, Game over")
        break
    bullets-=1
    print(f"shoot(),{bullets} are left")
else:
    print("Game over. You win the game")
