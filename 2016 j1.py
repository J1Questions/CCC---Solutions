game_1 = input("Did you win or lose Game 1?(W for win, L for loss):")
game_2 = input("Did you win or lose Game 2?(W for win, L for loss):")
game_3 = input("Did you win or lose Game 3?(W for win, L for loss):")
game_4= input("Did you win or lose Game 4?(W for win, L for loss):")
game_5 = input("Did you win or lose Game 5?(W for win, L for loss):")
game_6 = input("Did you win or lose Game 6?(W for win, L for loss):")

count_w = 0

if(game_1=="w"):
    count_w+=1
    
if(game_2 =="w"):
    count_w += 1
    
if(game_3 =="w"):
    count_w += 1
    
if(game_4 =="w"):
    count_w += 1
    
if(game_5 =="w"):
    count_w += 1
    
if(game_6 =="w"):
    count_w += 1
   
if(5<=count_w<=6):
    group=1
    

elif(3<=count_w<=4):
    group=2

elif(1<=count_w<=2):
    group=3

elif(count_w==0):
    group=-1

print(group)

