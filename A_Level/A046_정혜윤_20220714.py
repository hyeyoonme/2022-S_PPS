{\rtf1\ansi\ansicpg949\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import string\
N=int(input())\
lower=[i for i in string.ascii_lowercase]\
fn=[0]*26\
for i in range(N):\
    t=input()\
    fn[lower.index(t[0].lower())]+=1\
choose=""\
for i in range(len(fn)):\
    if fn[i]>=5:\
        choose+=lower[i]\
if len(choose)<1:\
    print("PREDAJA")\
else: print(choose)}