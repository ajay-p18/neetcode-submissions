class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str = ""
        for s in strs:
            new_str += str(len(s)) + "$" + s
        
        return new_str
        

    def decode(self, s: str) -> List[str]:

        decoded_strings = []
        pointer = 0
        

        while(pointer < len(s)):
            j = pointer
            length = ""
            while s[j] != "$":
                length += s[j]
                j += 1
            
            length = int(length)
            decoded_strings.append(s[j+1:j+length+1])

            j = j +length+1
            pointer = j
            length = ""

        return decoded_strings
