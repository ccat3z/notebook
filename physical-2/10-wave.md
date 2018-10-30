<!--
  ft=pandoc.markdown
-->

# 波动

波线`波线`{.idx}, 波面`波面`{.idx}, 波前`波前`{.idx}
: \ 
  \begin{tikzpicture}
    \coordinate (o) at (0,0);
    \fill (o) circle (1pt) node[below] {S};
    \draw (o) circle (1);
    \draw (o) circle (2);
    \draw (o) circle (3);
 
    \begin{scope}
        \path (o) -- (90:1) node[pos=0.5] (tag) {$\lambda$};
        \draw[->] (tag) -- (90:1);
        \draw[->] (tag) -- (o);
    \end{scope}
 
    \draw[->] (o) -- (0:3) node[pos=0.5, below] {波线};
 
    \draw[->] (30:3) -- (4,2) node[right] {波前};
 
    \draw[->] (-30:3) -- (4,-2) node[right] {波面};
    \draw[->] (-45:2) -- (4,-2);
    \draw[->] (-40:1) -- (4,-2);
  \end{tikzpicture}

\begin{tikzpicture}[domain=-0.5:4,samples=100]
  \draw[->] (-0.5,0) -- (4,0) node[below] {x};
  \draw[->] (0,-1) -- (0,2) node[right] {y};
  \node[below left] at (0,0) {O};
  \draw plot function{sin(2*x)};

  \draw[->] (1.5,1.5) -- node[below] {$u$} +(0.5,0);
\end{tikzpicture}

平面简谐波波动方程
: $y = A cos\ \omega (t - \dfrac{x}{u})$

角波速
: $k = \dfrac{2\pi}{\lambda}$

## 多普勒效应

`多普勒效应`{.idx}

观察者面向波源以$v_0$运动
: $\nu' = \dfrac{u + v_2}{u} \nu$

波源面向观察者以$v_s$运动
: $\nu' = \dfrac{u}{u - v_s} \nu$

<!-- TODO: 相干波, +NOTE 不要在波动方程图上看相位 -->
