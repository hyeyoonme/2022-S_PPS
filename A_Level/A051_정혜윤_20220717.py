{\rtf1\ansi\ansicpg949\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 S=input()\
time=0\
for w in S:\
    if w in 'ABC':\
        time+=3\
    elif w in 'DEF':\
        time+=4\
    elif w in 'GHI':\
        time+=5\
    elif w in 'JKL':\
        time+=6\
    elif w in 'MNO':\
        time+=7\
    elif w in 'PQRS':\
        time+=8\
    elif w in 'TUV':\
        time+=9\
    else: time+=10\
print(time)}