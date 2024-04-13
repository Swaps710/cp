class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        lst=[]
        set1=set()
        for i in range(0,len(s)-9):
            tmp=s[i:i+10]
            if tmp not in set1:
                set1.add(tmp)
            else:
                lst.append(tmp)
        return list(set(lst))

        
