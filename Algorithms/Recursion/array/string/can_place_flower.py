class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        def can_plant(flowerbed, idx):
            length = len(flowerbed) - 1
            
            # Handle case when flowerbed has only one plot
            if len(flowerbed) == 1:
                return flowerbed[0] == 0
            
            # Check for the first position
            if idx == 0:
                return flowerbed[0] == 0 and flowerbed[1] == 0
            
            # Check for the last position
            elif idx == length:
                return flowerbed[length] == 0 and flowerbed[idx - 1] == 0
            
            # Check for positions in between
            else:
                return flowerbed[idx - 1] == 0 and flowerbed[idx + 1] == 0

        # Iterate through the flowerbed and try to plant flowers
        for idx, plot in enumerate(flowerbed):
            if plot == 0 and can_plant(flowerbed, idx):
                flowerbed[idx] = 1
                n -= 1
                if n == 0:
                    break
        
        return n <= 0
