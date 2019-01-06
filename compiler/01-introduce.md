<!--
  vi: ft=pandoc.markdown
-->

# 引论

`词法分析`{.idx} `语法分析`{.idx} `语义分析`{.idx}
`中间代码生成`{.idx} `代码优化`{.idx} `目标代码生成`{.idx}

编译过程
: 

    \begin{tikzpicture}[baseline={(0.base)}]
        \path (0,0) node (0) {源程序}
            ++(0,-1) node[draw] (1) {词法分析}
            ++(0,-1) node[draw] (2) {语法分析}
            ++(0,-1) node[draw] (3) {语义分析}
            ++(0,-1) node[draw] (4) {中间代码生成}
            ++(0,-1) node[draw] (5) {代码优化}
            ++(0,-1) node[draw] (6) {目标代码生成}
            ++(0,-1) node (7) {目标程序};
        \draw[->] (0) -- (1);
        \draw[->] (1) -- (2);
        \draw[->] (2) -- (3);
        \draw[->] (3) -- (4);
        \draw[->] (4) -- (5);
        \draw[->] (5) -- (6);
        \draw[->] (6) -- (7);
    \end{tikzpicture}

