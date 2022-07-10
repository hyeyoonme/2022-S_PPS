{\rtf1\ansi\ansicpg949\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 HelveticaNeue;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab560
\pard\pardeftab560\slleading20\partightenfactor0

\f0\fs26 \cf0 def countPrimes(self, n: int) -> int:\
        count=0\
        if n == 0 or n ==1:\
            return count\
        \
        for i in range(2,n):\
            flag=0\
            for j in range(2,i):\
                if i%j==0:\
                    flag=1\
            if flag==0:\
                count+=1\
        return count}