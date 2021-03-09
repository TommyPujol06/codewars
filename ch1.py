n = int(input())
players = []
for i in range(n):
    players.append(input())

def best_player(players):
    max_points = []

    for player in players:
        player, _, goals, _, _, _, spades, _ = player.split()
        points = (int(goals) * 4) + (int(spades) * 2)
        if not max_points:
            max_points = [player, points]
        else:
            if max_points[1] < points:
                max_points = [player, points]
            elif max_points[1] == points:
                max_points = ["DRAW", points]
    
    if max_points[0] != "DRAW":    
        return f"{max_points[0]} is the MVP with {max_points[1]} points!"      
    
    return "DRAW"

print(best_player(players))