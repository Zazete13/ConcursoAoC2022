rounds = open("inputdia2.txt", "r").read().splitlines()
total_score = 0 
strategy_score = 0 

for i in range(len(rounds)):
    rounds[i] = rounds[i].split(" ")

for i in range(len(rounds)):
    for j in range(len(rounds[0])):
        if rounds[i][j] == 'A' or rounds[i][j] == 'X':
            rounds[i][j] = 1
        elif rounds[i][j] == 'B' or rounds[i][j] == 'Y':
            rounds[i][j] = 2
        elif rounds[i][j] == 'C' or rounds[i][j] == 'Z':
            rounds[i][j] = 3

for i in range(len(rounds)):
    match rounds[i][0]:
        case 1:
            match rounds[i][1]:
                case 1:
                    total_score += 3 + 1
                    strategy_score += 0 + 3
                case 2:
                    total_score += 6 + 2
                    strategy_score += 3 + 1
                case 3:
                    total_score += 0 + 3
                    strategy_score += 6 + 2
        case 2:
            match rounds[i][1]:
                case 1:
                    total_score += 0 + 1
                    strategy_score += 0 + 1
                case 2:
                    total_score += 3 + 2
                    strategy_score += 3 + 2
                case 3:
                    total_score += 6 + 3
                    strategy_score += 6 + 3
        case 3:
            match rounds[i][1]:
                case 1:
                    total_score += 6 + 1
                    strategy_score += 0 + 2
                case 2:
                    total_score += 0 + 2
                    strategy_score += 3 + 3
                case 3:
                    total_score += 3 + 3
                    strategy_score += 6 + 1

print(total_score)
print(strategy_score)
