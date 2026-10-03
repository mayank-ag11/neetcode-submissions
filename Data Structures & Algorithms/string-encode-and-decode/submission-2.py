class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += f"{len(s)}:{s}"
            # result += f"{len(s):03d}{s}"
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != ":":
                j += 1
            
            length = int(s[i:j])
            result.append(s[j + 1:j + 1 + length])
            i = j + 1 + length

            # This assumes that the length of the string can't go beyond 999
            # length = int(s[i:i + 3])
            # subStr = s[i+3:i+3+length]
            # result.append(subStr)
            # i += 3 + length

        return result