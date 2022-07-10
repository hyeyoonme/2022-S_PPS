{\rtf1\ansi\ansicpg949\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 HelveticaNeue;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab560
\pard\pardeftab560\slleading20\partightenfactor0

\f0\fs26 \cf0 class Solution:\
    def findContentChildren(self, g: List[int], s: List[int]) -> int:\
        g.sort()\
        s.sort()\
        g_i=0\
        s_i=0\
        while g_i<len(g) and s_i<len(s) :\
            if g[g_i]>s[s_i]:\
                s_i=s_i+1\
            else:\
                g_i=g_i+1\
                s_i=s_i+1\
        return g_i\
}