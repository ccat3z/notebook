<!-- Lec3 -->

# 向量空间

## 向量子空间

`向量子空间!直和`{.idx}
\begin{define}
如果$\mathbb{Y}$中的每个向量$x$可唯一地表成
$x = y_1 + y_2 (y_1 \in \mathbb{Y}_1 , y_2 \in \mathbb{Y}_2 )$ 的形式，
则称$\mathbb{Y}$为
$\mathbb{Y}_1$与$\mathbb{Y}_2$的\textbf{直和}。
记作$\mathbb{Y} = \mathbb{Y}_1 + \mathbb{Y}_2$或$\mathbb{Y}_1 \oplus \mathbb{Y}_2$
\end{define}

\begin{mthm}
$\mathbb{Y}_1 + \mathbb{Y}_2$为直和的必要充分条件是：
有$y_1 + y_2 = 0 (y_1 \in \mathbb{Y}_1, y_2 \in \mathbb{Y}_2$
可退出$y_1 = y_2 = 0$。
\end{mthm}

\begin{mthm}
$\mathbb{Y}_1 + \mathbb{Y}_2$为直和的必要充分条件是：
有$\mathbb{Y}_1 \cap \mathbb{Y}_2 = {0}$。
\end{mthm}

## 线性无关性

`向量组等价`{.idx}
\begin{define}
如果两个向量组互相可以线性表出， 则称为它们\textbf{等价}。
\end{define}

## 生成集、基底和坐标

`张成的子空间`{.idx} `生成集`{.idx}
\begin{define}
称为由$a_1 , a_2 , \ldots , a_r$\textbf{张成的子空间}$\mathbb{V}$，记作
$L(a_1 , a_2 , \ldots , a_r )$ 或 $spa_n(a_1 , a_2 , \ldots , a_r )$。
${a_1 , a_2 , \ldots , a_r }$ 叫做 $\mathbb{V}$ 的一个\textbf{生成集}。
\end{define}

`维数`{.idx} `基`{.idx}
\begin{define}
维数: $dim(\mathbb{V}) = n$, $n$为$\mathbb{V}$的基。
\end{define}

## 秩

`秩`{.idx}
\begin{define}
$dim(L(a_1 , a_2 , \ldots , a_r )) = rank{a_1 , a_2 , \ldots , a_r }$
\end{define}

## 仿射子空间

`仿射子空间`{.idx}
\begin{define}
令$\mathbb{V}$是一线性空间，$x_0 \in \mathbb{V}$且
$\mathbb{U} \subseteq \mathbb{V}$ 是一线性子空间，则子集
$L = x_0 + \mathbb{U} := {x_0 + u|u \in \mathbb{U}} \subseteq \mathbb{V}$
是一仿射子空间。我们定义线性子空间的维数为仿射子空间的维数。
\end{define}