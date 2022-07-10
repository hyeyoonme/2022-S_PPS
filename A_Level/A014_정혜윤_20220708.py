{\rtf1\ansi\ansicpg949\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 class Solution:\
    def summaryRanges(self, nums: List[int]) -> List[str]:\
        result=[]\
        if len(nums)<1:\
            return result\
        st=nums[0]\
        end=nums[0]\
        flag=0\
        for i,n in enumerate(nums):\
            if flag==1:\
                st=n\
                end=n\
                flag=0\
            if n+1 in nums:\
                end=nums[i+1]\
            else:\
                if st==end:\
                    a=str(st)\
                    flag=1\
                else: \
                    end=n\
                    a=str(st)+'->'+str(end)\
                    flag=1\
                result.append(a)\
                \
        return result}