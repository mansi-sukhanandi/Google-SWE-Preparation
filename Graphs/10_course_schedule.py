from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Adjacency List (course -> list of prerequisites)
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
            
        # Graph traversal tracker
        visiting = set() # Path mein abhi kon sa node stack par hai

        def dfs(crs):
            # Base Case 1: Cycle detect ho gayi!
            if crs in visiting:
                return False
                
            # Base Case 2: Is course ke prerequisites pehle se verified/cleared hain
            if preMap[crs] == []:
                return True

            visiting.add(crs)
            
            # Saare prerequisites check karo
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
                    
            visiting.remove(crs) # Backtrack
            preMap[crs] = []     # Optimization: Mark as fully verified safe
            return True

        # Pure forest / all unconnected nodes check karo
        for crs in range(numCourses):
            if not dfs(crs):
                return False
                
        return True
