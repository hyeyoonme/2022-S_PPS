{\rtf1\ansi\ansicpg949\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 class Solution:\
    def generate(self, numRows: int) -> List[List[int]]:\
        p=[]\
        r=0\
        while r < numRows:\
            row=[]\
            n=0\
            while n < r+1:\
                if n==0:\
                    row.append(1)\
                elif n==r:\
                    row.append(1)\
                else:\
                    row.append(p[r-1][n-1]+p[r-1][n])\
                n+=1\
            p.append(row)\
            r+=1\
        return p}