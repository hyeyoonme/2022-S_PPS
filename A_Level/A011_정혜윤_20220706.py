{\rtf1\ansi\ansicpg949\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 def solution(N, stages):\
    answer = []\
    rate=\{\}\
    total=len(stages)\
    for i in range(1,N+1):\
        if total!=0:\
            s_count= stages.count(i)\
            rate[i]=s_count/total\
            total=total-s_count\
        else:\
            rate[i]=0\
    answer=sorted(rate, key=lambda k:rate[k], reverse=True)\
    return answer}