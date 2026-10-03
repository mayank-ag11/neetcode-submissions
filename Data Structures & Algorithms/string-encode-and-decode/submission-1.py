class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += f"{len(s):03d}{s}"
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            length = int(s[i:i + 3])
            subStr = s[i+3:i+3+length]
            result.append(subStr)
            i += 3 + length

        return result