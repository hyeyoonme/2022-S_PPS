{\rtf1\ansi\ansicpg949\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 def solution(people, limit):\
    answer = 0\
    people.sort()\
    while True:\
        s=0\
        e=len(people)-1\
        if s!=e and people[s]+people[e]<=limit:\
            people.pop(e)\
            people.pop(s)\
            answer+=1\
        else:\
            people.pop(e)\
            answer+=1\
        if len(people)==0: break \
    return answer}