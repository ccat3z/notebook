<!--
  vi: ft=pandoc.markdown
-->

# 振动

## 简谐振动

胡克定律 `胡克定律`{.idx}
: $a = \dfrac{F}{m} = - \underline{\dfrac{k}{m}} x = - \underline{\omega^2} x$

  可由胡克定律求弹簧劲度系数$k$

简谐振动方程 `简谐振动方程`{.idx}
: $x = Acos(\omega t + \varphi)$

周期 `周期`{.idx}
: $T = \dfrac{2\pi}{\omega\ \text{(角频率)}}$

频率 `频率`{.idx}
: $\nu = \dfrac{1}{T}$

相位 `相位`{.idx}
: $\varphi = \omega t + \varphi_0\ \text{(初相位)}$

总能量 `总能量`{.idx}
: $E = \dfrac{1}{2} m \omega^2 A^2$

### 同方向同频率简谐振动的合成

旋转矢量图
: \ 
  \begin{tikzpicture}
    \draw[->] (0,0) -- (4,0) node[below] {$x$} node[coordinate] (x) {};
    \fill (0,0) circle (1pt) node[below left] {$O$} node[coordinate] (o) {};
  
    \path (2,1) node[below right] {$A_1$} node[coordinate] (a1) {};
    \path (1,3) node[above left] {$A_2$} node[coordinate] (a2) {};
    \path ($(a1) + (a2)$) node[above right] {$A$} node[coordinate] (a) {};
  
    \path [draw,->,solid] (o) -- (a1);
    \path [draw,->,solid] (o) -- (a2);
    \path [draw,->,solid] (o) -- (a);
    \path [draw,dotted] (a1) -- (a) (a2) -- (a);
  \end{tikzpicture}

$A = \sqrt{A_1^2 + A_2^2 + 2A_1A_2 cos(\varphi_2 - \varphi_1)}$

$tan \varphi = \dfrac{A_1 sin \varphi_1 + A_2 sin \varphi_2}{A_1 cos \varphi_1 + A_2 cos \varphi_2}$
