{\rtf1\ansi\ansicpg949\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 def solution(s):\
    answer = len(s)\
    for j in range(1,len(s)):\
        i=0\
        new=""\
        pat=""\
        t=1\
        while i<len(s):\
            if(s[i:i+j]!=pat):\
                if(t==1):\
                    new=new+pat\
                else:\
                    new=new+str(t)+pat\
                pat=s[i:i+j]\
                t=1\
            elif(s[i:i+j]==pat):\
                t=t+1\
            i=i+j\
        if(t==1):\
            new=new+pat\
        else:\
            new=new+str(t)+pat\
        if(answer>len(new)):\
            answer=len(new)\
    return answer}