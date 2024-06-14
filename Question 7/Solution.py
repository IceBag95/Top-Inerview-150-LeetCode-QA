class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        N = len(prices)

        # logic for determining how to find the maximum possible profit for each day
        # compare every next value of list prices (currently is called arr) 
        # with the prices[day] value
        def find_max_of(day: int, arr: list[int]) -> int:
            max_prft = -1 
            for i in range(len(arr)):
                current_prft = arr[i] - prices[day]
                if current_prft > 0 and max_prft < current_prft:
                    max_prft = current_prft

            return max_prft
        

        # the find_max_of() helper function must be called for each day of the original prices list
        # here is the logic for that
        total_max = -1
        for i in range(N):
            arr = prices[i+1:N-1]
            max_of_arr = find_max_of(i, arr)
            if total_max < max_of_arr:
                total_max = max_of_arr
        

        if total_max <= 0:
            return 0
        
        return total_max