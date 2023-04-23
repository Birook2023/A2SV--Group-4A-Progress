class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        p, t, count = len(players) - 1, len(trainers) - 1, 0
        players.sort()
        trainers.sort()
        
        while p >= 0 and t >= 0:
            if players[p] <= trainers[t]:
                count += 1
                p -= 1
                t -= 1
            else:
                p -= 1
        
        return count
