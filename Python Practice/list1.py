class Solution:
    def Learning(self, arr, n):
            # Your code goes here
            # return (0.1, 0.2, 0.3);
            p = 0
            ne = 0
            z = 0
            for i in arr:
               
                if i > 0:
                    p = p + 1
                   
                    continue
                if i < 0:
                    ne = ne + 1
                    # print(ne)
                    continue
                if i == 0:
                    z = z + 1
                    continue
            # print(p)
            # print(ne)
            # print(z)
            pn = n / p

            nd = n / ne
            zn = n / z
            
            if zn.is_integer():
                rn_n = (int(zn))
            else:
                rn_n = round(zn, 5)
                
                
            if nd.is_integer():
                nd_n = (int(nd))
            else:
                nd_n = round(nd, 5)
                
                
            if pn.is_integer():
                pn_n = (int(pn))
            else:
                pn_n = round(pn, 5)

            return(pn, nd_n, rn_n)
                
           
            
            
       
arr1 = [-86, 77, 0, -15, 93, 0, -35, 86, 0, -92, 49, 0, 0, 0, 0, 0, 0]
n = 17
obj = Solution()
re = obj.Learning( arr1, n)
print(re)

