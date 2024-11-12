import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        removed_symbol_paragraph = re.sub(r'[!?\',;.]', ' ', paragraph.lower())
        paragraph_counter = Counter(removed_symbol_paragraph.split())

        for ban in banned:
            paragraph_counter[ban] = 0

        key, count = paragraph_counter.most_common(1)[0]

        return key