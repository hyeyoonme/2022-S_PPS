{\rtf1\ansi\ansicpg949\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 N=int(input())\
result=[]\
\
for i in range(N):\
    li=list(input().split())\
    n=float(li[0])\
    for j in range(1,len(li)):\
        if li[j]=='@':\
            n*=3\
        elif li[j]=='%':\
            n+=5\
        elif li[j]=='#':\
            n-=7\
    result.append(n)\
 \
for i in range(N):\
    print("\{:.2f\}".format(result[i]))}