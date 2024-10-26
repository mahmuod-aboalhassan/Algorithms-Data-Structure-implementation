from typing import List 
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i ,asteroid in enumerate(asteroids):
            if i==0 or asteroid>0:
                stack.append(asteroid)
                continue
            if asteroid<0:
                while len(stack) and stack[-1]>0:
                    if abs(asteroid)>abs(stack[-1]):
                        stack.pop()
                    else:
                        break
                if len(stack) and abs(asteroid)==stack[-1]:
                    stack.pop()
                elif not len(stack) or (stack[-1]<0 and asteroid<0):
                    stack.append(asteroid)
        return stack

            

                 
solution=Solution()
solution.asteroidCollision([8,-8])