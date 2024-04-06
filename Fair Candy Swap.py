class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        totalalice = sum(aliceSizes)
        totalbob = sum(bobSizes)
        targettotal = (totalalice + totalbob)//2
        for aliceCandy in aliceSizes:
            bobCandy = aliceCandy + (targettotal - totalalice)
            if bobCandy in bobSizes:
                return(aliceCandy,bobCandy)

        
        
        
