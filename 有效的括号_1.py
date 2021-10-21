class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = []
        DICT = {'[':1,']':1,'{':2,'}':2,'(':3,')':3}
        Left = ['{','(','[']
        n = len(s)
        if n%2 == 1:
            return False
        else:
            for letter in s:
                if letter in Left:
                    res.append(letter)
                else:
                    if not res or DICT[res[-1]] != DICT[letter]:
                        
                        return False
                    else:
                        
                        res.pop()
        return not res###太妙了不用在判断是否为空了
