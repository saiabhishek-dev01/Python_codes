#problem no - 1422
#Maximum score After Splitting a String

class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        left_zeros=0
        total_ones=s.count('1')
        right_ones=total_ones
        max_score = 0
        for i in range(len(s)-1):
            if s[i]=='0':
                left_zeros+=1
            else:
                right_ones-=1
            sum_score = left_zeros+right_ones
            max_score=max(max_score,sum_score)
        return max_score

 
        