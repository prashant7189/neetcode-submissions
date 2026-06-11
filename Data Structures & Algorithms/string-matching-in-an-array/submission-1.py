class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = set()

        for i,v in enumerate(words):

            for idx, value in enumerate(words):

                if i != idx and v in value:
                    res.add(v)
        return list(res)