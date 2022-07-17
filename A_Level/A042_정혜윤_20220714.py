{\rtf1\ansi\ansicpg949\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 class Solution:\
    def backspaceCompare(self, s: str, t: str) -> bool:\
        s_i=t_i=0\
        s_c=[]\
        t_c=[]\
        while True:\
            if s_i<len(s):\
                if s[s_i] in '#':\
                    if len(s_c)!=0:\
                        s_c.pop()\
                else: s_c.append(s[s_i])\
                s_i+=1\
            if t_i<len(t):\
                if t[t_i] in '#':\
                    if len(t_c)!=0:\
                        t_c.pop()\
                else: t_c.append(t[t_i])\
                t_i+=1\
            if s_i>=len(s) and t_i>=len(t):\
                break\
        return (s_c==t_c)}