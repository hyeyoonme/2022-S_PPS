{\rtf1\ansi\ansicpg949\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 ran=list(map(int,input().split()))\
al=[]\
i=1\
count=0\
if ran[0]==1 and ran[1]==0:\
    print(1)\
else:\
    while True:\
        for j in range(i):\
            al.append(i)\
            count+=1\
        if count>=ran[1]: break\
        i+=1\
    print(sum(al[ran[0]-1:ran[1]]))}