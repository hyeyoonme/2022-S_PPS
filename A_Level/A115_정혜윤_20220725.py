{\rtf1\ansi\ansicpg949\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 class Solution:\
    def maxNumberOfBalloons(self, text: str) -> int:\
        balloon=['b','a','l','o','n']\
        count=[0]*5\
        for w in text:\
            if w in balloon:\
                i=balloon.index(w)\
                count[i]+=1\
        count[2]=count[2]//2\
        count[3]=count[3]//2\
        return min(count)}