{\rtf1\ansi\ansicpg949\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 class Solution:\
    def lemonadeChange(self, bills: List[int]) -> bool:\
        change=[0]*3\
        for n in bills:\
            if n==5:\
                change[0]+=1\
            elif n==10:\
                if change[0]==0:\
                    return False\
                change[0]-=1\
                change[1]+=1\
            else:\
                if change[1]!=0 and change[0]!=0:\
                    change[1]-=1\
                    change[0]-=1\
                    change[2]+=1\
                elif change[0]>=3:\
                    change[0]-=3\
                    change[2]+=1\
                else: return False\
        return True}