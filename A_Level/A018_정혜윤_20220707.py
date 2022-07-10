{\rtf1\ansi\ansicpg949\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 N=int(input())\
A=list(map(int,input().split()))\
B=list(map(int,input().split()))\
A.sort()\
t=sorted(range(len(B)),key=lambda k : B[k], reverse=True)\
\
A_s=[0]*N\
for i,j in zip(t,range(N)):\
    A_s[i]=A[j]\
\
result=0\
for i in range(N):\
    result+=A_s[i]*B[i]\
print(result)}