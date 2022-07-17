{\rtf1\ansi\ansicpg949\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 def solution(a, b):\
    day=['FRI','SAT','SUN','MON','TUE','WED','THU']\
    lastdays = [31,29,31,30,31,30,31,31,30,31,30,31]\
    t = 0\
    answer = ''\
    \
    if a == 1:\
        t = b%7\
        answer = day[t-1]\
    else :\
        for i in range(a-1) :\
            t += lastdays[i]\
        t +=b\
        t= t % 7\
        answer = day[t-1]\
    return answer}