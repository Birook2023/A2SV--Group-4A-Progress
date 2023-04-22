class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        count = 0
        compare = skill[0] + skill[-1]
        l, r = 0, len(skill) - 1
        
        while l < r:
            if skill[l] + skill[r] == compare:
                count += skill[l] * skill[r]
                l += 1
                r -= 1
            else:
                return -1
        
        return count
