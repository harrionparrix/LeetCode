class Solution:
    def convert(self, s: str, numRows: int) -> str:
        k=""
        if(numRows==1):
            return s
        for r in range(numRows):
            inc=2*(numRows-1)
            for i in range(r,len(s),inc): 
                k+=s[i]
                if( r>0 and r<numRows-1 and i+inc-2*r< len(s)):
                    k+=s[i+inc-2*r]
        return k