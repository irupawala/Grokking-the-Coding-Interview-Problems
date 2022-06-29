# Ibrahim Solution
class Solution:
    def backspaceCompare(self, s, t):
        return self.stringBackspace(s) == self.stringBackspace(t)
    
    
    def stringBackspace(self, text):
        l, r, last_stop = 0, 0, 0
        result_string = ""
        last_stop = 0
        while r < len(text):
            if text[r] != "#":
                l += 1
                r += 1
            else:
                l -= 1
                r += 1
                if l < 0: l = 0
                result_string += text[last_stop:l]
                l = last_stop = r
                
                if r < len(text) and text[r] == "#":
                    count = 0
                    result_string_len = len(result_string)
                    while r < len(text) and text[r] == "#" and result_string_len != 0 :
                        count += 1
                        result_string_len -= 1
                        r += 1
                    result_string = result_string[:-count]
                    l += count
                    r = last_stop = l
            
        if last_stop < len(text):
            result_string += text[last_stop:]
        
        return result_string
        
        
# Grokking Solution
'''
class Solution:
    def backspaceCompare(self, s, t):
        # use two pointer approach to compare the strings
        index1 = len(s) - 1
        index2 = len(t) - 1
        while (index1 >= 0 or index2 >= 0):
            i1 = self.get_next_valid_char_index(s, index1)
            i2 = self.get_next_valid_char_index(t, index2)
            if i1 < 0 and i2 < 0:  # reached the end of both the strings
                return True
            if i1 < 0 or i2 < 0:  # reached the end of one of the strings
                return False
            if s[i1] != t[i2]:  # check if the characters are equal
                return False

            index1 = i1 - 1
            index2 = i2 - 1

        return True


    def get_next_valid_char_index(self, str, index):
        backspace_count = 0
        while (index >= 0):
            if str[index] == '#':  # found a backspace character
                backspace_count += 1
            elif backspace_count > 0:  # a non-backspace character
                backspace_count -= 1
            else:
                break

            index -= 1  # skip a backspace or a valid character

        return index
'''
       
    
#S = Solution()
#print(S.stringBackspace("ab#cde##fgh#ijk###lm#"))


'''
Time Complexity - O(N+M), However, on average Grokking solution is faster as it returns False immediately the character does not match
Space Complexity - O(N+M) - Ibrahim, O(1) - Grokking
'''
