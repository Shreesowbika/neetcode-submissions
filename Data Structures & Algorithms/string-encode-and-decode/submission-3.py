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
            j=encoded.find("#",i)
            len_=int(encoded[i:j])
            i=j+1
            res.append(encoded[i:i+len_])
            i+=len_
        return res