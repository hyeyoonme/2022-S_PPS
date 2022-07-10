{\rtf1\ansi\ansicpg949\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import string \
\
def solution(skill, skill_trees):\
    answer = -1\
    alpha = string.ascii_uppercase\
    temp=skill\
    for a in skill:\
        alpha=alpha.replace(a,'')\
    for tree in skill_trees:\
        for a in alpha:\
            tree=tree.replace(a,'')\
        for i,a in enumerate(skill):\
            tree=tree.replace(a,str(i))\
            temp=temp.replace(a,str(i))\
\
        if tree.startswith('0') and tree in temp or tree=='':\
            answer+=1\
            \
    answer+=1\
    return answer}