class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # start and end variables
        # while loop while start < end, if start and end are not the same
        # return false.
        # if we exit while loop, return true

        stringed_x = str(x)
        start = 0
        end = len(stringed_x) - 1

        while start < end:
            if stringed_x[start] != stringed_x[end]:
                return False
            else:
                start+=1
                end-=1
                
        return True