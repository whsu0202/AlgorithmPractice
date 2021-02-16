from functools import cmp_to_key

# https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem
class Player:
    def __init__(self, name, score):
        self.name=name
        self.score=score
        
    def __repr__(self):
        return self.name,self.score
        
    def comparator(a, b):
        if a.score<b.score:
            return 1
        if a.score>b.score:
            return -1
        if a.name<b.name:
            return -1
        if a.name>b.name:
            return 1
        return 0
        
        
n = 5
data = []
# 5
# amy 100
# david 100
# heraldo 50
# aakansha 75
# aleksa 150

for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)
