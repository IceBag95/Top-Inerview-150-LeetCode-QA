class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
        def find_next_index(arr: list[int]) -> int:     # finds next possible index j with prices[j] > prices[i] 
            N = len(arr)                                # with prices[j] - prices[i] -> MAX within i,j area in list arr
            j = 1
            while arr[j] > arr[0]:
                
                if j+1 >= N: 
                    break
                
                if arr[j] > arr[j+1]:
                    break

                j += 1
            
            return j



        def find_current_profit(curr_arr: list[int]) -> int:  # finds current profit accoriding to instructions
            S = 0                                             # initialize a Sum
            while len(curr_arr) > 1:
                if prices[i] == max(curr_arr):
                    S = -1
                    break

                j = find_next_index(curr_arr)                 # find a j that prices[j] > prices[j+1] or return 0
                profit = curr_arr[j] - curr_arr[0]
                S += profit
                curr_arr = curr_arr[j+1:N]                    # cuts the checked piece of list and continues with the rest
            
            return S





        N = len(prices)

        max_profit = -1
        for i in range(N):
            curr_arr = prices[i: N]      # make a copy list of prices from i to N-1 element
            
            current_profit = find_current_profit(curr_arr)
            if max_profit < current_profit:
                max_profit = current_profit

        return max_profit
