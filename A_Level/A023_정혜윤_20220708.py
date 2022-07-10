{\rtf1\ansi\ansicpg949\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 class Solution:\
    def addDigits(self, num: int) -> int:\
        s_num=str(num)\
        ssum=0\
        result=10\
        \
        while True:\
            for n in s_num:\
                ssum+=int(n)\
            s_num=str(ssum)\
            result=ssum\
            ssum=0\
            \
            if result<10: break\
        return result}