class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        indegree = defaultdict(int)
        graph = defaultdict(list)

        for i in range(len(recipes)):
            recipe = recipes[i]
            ing = ingredients[i]
            indegree[recipe] = len(ing)
            for ingredient in ing:
                graph[ingredient].append(recipe)
        
        poss = []
        queue = deque(supplies)
        reci = set(recipes)
        
        while queue: 
            current_supply = queue.popleft()
            
            if current_supply in reci:
                poss.append(current_supply)
            
            for recipe in graph[current_supply]: 
                indegree[recipe] -= 1
                if indegree[recipe] == 0:
                    queue.append(recipe)
        
        return poss
