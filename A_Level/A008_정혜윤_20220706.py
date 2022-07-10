{\rtf1\ansi\ansicpg949\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 re=int(input())\
rate_a=[]\
for i in range(re):\
    a = list(map(int, input().split()))\
    total=0\
    per=0\
    for j in range(a[0]):\
        total=total+a[j+1]\
    avg=total/a[0]\
    for j in range(a[0]):\
        if a[j+1]>avg:\
            per=per+1\
    rate = round(per/a[0]*100,6)\
    rate_a.append(rate)\
for i in range(len(rate_a)):\
    print("\{:.3f\}%".format(rate_a[i]),sep='')}