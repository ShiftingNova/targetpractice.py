def print_board(target_string, character):
    current_hit_x = int(target_string[0] + target_string[1])
    current_hit_y = int(target_string[2] + target_string[3])
    y = 5
    i=0
    while y >- 6:
        x = -7
        while x < 8:

            if (x == current_hit_x) and (y == current_hit_y):
                print(character, end="")
                i += 4
                if i<len(target_string):
                    current_hit_x = int(target_string[i] + target_string[i+1])
                    current_hit_y = int(target_string[i+2] + target_string[i+3])
            elif x == 0:
                print("|", end= "")
            elif y == 0:
                print("-", end="")
            else:
                print(" ", end="")
            x+=1
        print()
        y-=1



sequence = input("Hit string:\n")
while not(len(sequence) > 3 and len(sequence)%4==0):
    print("Please provide a valid hit string.")
    sequence = input("Hit string:\n")
marker = input("Marker:\n")
while len(marker)>1:
    print("Please provide a valid marker.")
    marker = input("Marker:\n")
print_board(sequence, marker)

