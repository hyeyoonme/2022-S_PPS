{\rtf1\ansi\ansicpg949\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 class Solution:\
    def halvesAreAlike(self, s: str) -> bool:\
        a= s[:len(s)//2]\
        b= s[len(s)//2:]\
        a_v=b_v=0\
        vowels=['a','e','i','o','u','A','E','I','O','U']\
        for v in vowels:\
            a_v+=a.count(v)\
            b_v+=b.count(v)\
        if a_v!=b_v:\
            return False\
        else: return True}