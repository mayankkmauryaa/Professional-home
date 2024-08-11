class Solution(object):
    def reverse(self, x):
        st=''
        sign=1
        for i in str(x):
            if i=='-':
                sign=-1
            else:
                st+=i
        st=sign* int(st[::-1])
        if st < -(2 ** 31) or st >(2**31 - 1):
            return 0

        return st