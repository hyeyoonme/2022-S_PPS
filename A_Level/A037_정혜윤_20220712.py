{\rtf1\ansi\ansicpg949\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 class Solution:\
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:\
        result=[]\
        for n in range(left,right+1):\
            flag=0\
            if str(0) in str(n): continue\
            for i in str(n):\
                if n%int(i)!=0:\
                    flag=1\
            if flag!=1:\
                result.append(n)\
        return result}