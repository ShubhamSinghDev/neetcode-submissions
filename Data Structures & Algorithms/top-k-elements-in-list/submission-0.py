class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
                dict1={}
                
                for ch in nums:
                    dict1[ch]=dict1.get(ch,0)+1
                d=list(dict1.keys())
                p=list(dict1.values())
                lst=[]
                for i in range(len(d)):
                    lst.append([p[i],d[i]])
                lst.sort()
                res=[]
                for r in range(k):
                    res.append(lst.pop()[1])
                return res


                