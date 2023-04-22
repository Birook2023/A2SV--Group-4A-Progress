class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        zipped = zip(heights, names)
        zipped = sorted(zipped, reverse = True)
        sorted_names = []
        
        for heights, name in zipped:
            sorted_names.append(name)
        
        return sorted_names
