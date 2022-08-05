{\rtf1\ansi\ansicpg949\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import sys\
N=int(input())\
queue=[]\
for i in range(N):\
    order=list(sys.stdin.readline().split())\
    if order[0]=='push':\
        queue.insert(0,int(order[1]))\
    elif order[0]=='pop':\
        if len(queue)<1:\
            print('-1')\
        else: print(queue.pop())\
    elif order[0]=='front':\
        if len(queue)<1:\
            print('-1')\
        else: print(queue[0])\
    elif order[0]=='back':\
        if len(queue)<1:\
            print('-1')\
        else: print(queue[-1])\
    elif order[0]=='size':\
        print(len(queue))\
    else:\
        if len(queue)<1:\
            print('1')\
        else: print('0')}