class Solution:
    def candy(self, ratings: List[int]) -> int:      
            
        N = len(ratings)
        number_of_candy = [1] * len(ratings)


        for i in range(N):
            if ratings[i] > ratings[i-1]:
                number_of_candy[i] = number_of_candy[i-1] + 1



        for i in range(N-1, 0, -1):

            if ratings[i] < ratings[i-1]:
                number_of_candy[i-1] = max(number_of_candy[i-1], number_of_candy[i] + 1)
        
        
        return sum(number_of_candy)
