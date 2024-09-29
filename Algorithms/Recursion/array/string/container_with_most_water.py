from typing import  List
class Solution:
    def maxArea1(self, height: List[int]) -> int:
        self.areas=[]
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                line_height=min(height[i],height[j])
                width=j-i
                # print(line_height,width,)
                self.areas.append(line_height*width)
                # self.areas(f'height {line_height} width { width} area ={line_height*width}')
        # print(self.areas)
        return max(self.areas)
    def maxArea(self, height: List[int]) -> int:
        self.areas=[]
        i=0
        j=len(height)-1
        max_area=0
        while i<j:
            right=height[i]
            left=height[j]
            line_height=min(height[i],height[j])
            width=j-i
            area=line_height*width
            if area>max_area:max_area=area
            if right<left:
                i+=1
            else:
                j-=1
        return max_area
            

