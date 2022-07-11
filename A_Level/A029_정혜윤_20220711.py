{\rtf1\ansi\ansicpg949\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 N=int(input())\
f=int(input())\
pa=[]\
pa.append(f)\
flag=0\
for i in range(1,N):\
    pa.append(1 if pa[i-1]==0 else 0)\
    if i>1 and (i+1)%2==0 and pa[1]!=pa[i]:\
        flag=1  \
        break\
    elif i>2 and (i+1)%3==0 and pa[2]!=pa[i]:\
        flag=1  \
        break\
\
if flag==1:\
    print("Love is open door")\
else:\
  for i in range(1,N):\
    print(pa[i])}