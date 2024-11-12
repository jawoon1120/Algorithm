class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1 : return s
        output = ""
        def extends(left_index, right_index):
            while left_index >= 0 and right_index < len(s) and s[left_index] == s[right_index]:
                left_index -= 1
                right_index += 1
            left_index += 1
            right_index -= 1
            return left_index, right_index

        for i in range(0,len(s)):
            if s[i:i+1] == s[i:i+1][::-1]:   
                three_left_index, three_right_index = extends(i, i+2)
                if(len(s[three_left_index: three_right_index+1]) > len(output)):
                    output = s[three_left_index: three_right_index+1]
            if s[i:i+2] == s[i:i+2][::-1]: 
                two_left_index, two_right_index = extends(i, i+1)
                if(len(s[two_left_index: two_right_index+1]) > len(output)):
                    output = s[two_left_index: two_right_index+1]


        return output