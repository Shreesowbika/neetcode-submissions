class Solution:

    def encode(self, strs: List[str]) -> str:
        encoder=""
        for s in strs:
            n=len(s)
            encoder =encoder + str(n) + "#" + s
        return encoder

    def decode(self, encoded: str) -> List[str]:
        res = []
        i = 0

        while i < len(encoded):

            # Find the position of '#'
            j = encoded.find("#", i)

            # Length of the next string
            length = int(encoded[i:j])

            # Move to the first character of the string
            i = j + 1

            # Extract exactly 'length' characters
            res.append(encoded[i:i + length])

            # Move to the beginning of the next encoded string
            i += length

        return res