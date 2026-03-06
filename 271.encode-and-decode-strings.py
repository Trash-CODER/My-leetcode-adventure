class Solution:

    def encode(self, strs: List[str]) -> str:
        # too complicated: should have attatched the length of the str after the delimiter
        re_str = []
        for str in strs:
            re_str.append('#')
            for i in range(len(str)):
                if (str[i] == '#'):
                    re_str.append('\\')
                    re_str.append('#')
                elif(str[i] == '\\'):
                    re_str.append('\\')
                    re_str.append('\\')
                else:
                    re_str.append(str[i])
        return "".join(re_str)
                    
        

    def decode(self, s: str) -> List[str]:
        str_list = []
        i = 0
        tmp_str = []
        # if the the encode str is empty  then return an empty
        # otherwise it will have a empty str ""
        if (len(s) < 1):
            return str_list
        while(i <  len(s)):
            if s[i] == '#':
                if i != 0:
                    str_list.append("".join(tmp_str))
                tmp_str = []
            elif s[i] =='\\':
                i += 1 
                tmp_str.append(s[i])
            else:
                tmp_str.append(s[i])
            i += 1
        # last str need to be added here
        str_list.append("".join(tmp_str))
        return str_list