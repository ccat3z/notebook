# 社区发现

## 模块度

## 例题

\begin{problem}{254}{4}
设有权图$G$的权重矩阵为

\[
    W = \begin{pmatrix}
        0 & 2 & 3 \\
        2 & 0 & 0 \\
        3 & 0 & 0
    \end{pmatrix}
\]

\begin{enumerate}[label=(\arabic*)]
\item 如果两个社区分别为$C_1 = \{1, 3\}$和$C_2 = \{2\}$, 试使用

\[ 
    Q = \frac{1}{2m} \sum_{s \in C} \sum_{i \in c} \sum_{j \in c}
        \left(W_{ij} - \frac{k_i k_j}{2m}\right)
\]

计算模块度。

\item 社区结构如(1)相同，试使用

\[
    Q = \sum_{c \in C}\left[
        \frac{\sum_{in}^c}{2m}
        - \left(\frac{\sum_{tot}^c}{2m}\right)^2
    \right]
\]

计算模块度。

\item 社区结构如(1)相同，试使用

\[
    Q = \frac{1}{4m} s^T B s
\]

计算模块度。其中$B_{ij} = W_{ij} - \frac{k_i k_j}{2m}$。
\end{enumerate}
\end{problem}
\begin{solution}{解}
\begin{enumerate}[label=(\arabic*)]
\item
\begin{align*}
Q &= \frac{1}{2m} \sum_{s \in C} \sum_{i \in c} \sum_{j \in c}
     \left(W_{ij} - \frac{k_i k_j}{2m}\right) \\
  &= \frac{1}{2 \times 5} \left[
        % c = {1, 3}
        \left(0 - \frac{5 \times 5}{2 \times 5}\right) % 1, 1
        + 2 \left(3 - \frac{5 \times 3}{2 \times 5}\right) % 1, 3; 3, 1
        + \left(0 - \frac{3 \times 3}{2 \times 5}\right) % 3, 3
        % c = {2}
        + \left(0 - \frac{2 \times 2}{2 \times 5}\right) % 2, 2
     \right] \\
  &= -0.08
\end{align*}

\item
\begin{align*}
Q &= \sum_{c \in C}\left[
        \frac{\sum_{in}^c}{2m}
        - \left(\frac{\sum_{tot}^c}{2m}\right)^2
     \right] \\
  &= \left[
        \frac{3 + 3}{2 \times 5} - \left(\frac{3 + 5}{2 \times 5}\right)^2
     \right] % C_1
     + \left[
        \frac{0}{2 \times 5} - \left(\frac{2}{2 \times 5}\right)^2
     \right] \\ % C_2
  &= -0.08
\end{align*}

\item

\[
    s = \begin{pmatrix}1 \\ -1 \\ 1\end{pmatrix},
    B = \begin{pmatrix}
        -2.5 & 1 & 1.5 \\
        1 & -0.4 & -0.6 \\
        1.5 & -0.6 & -0.9
    \end{pmatrix}
\]

\begin{align*}
Q &= \frac{1}{4m} s^T B s \\
  &= \frac{1}{20} \times \begin{pmatrix}1 & -1 & 1\end{pmatrix}
     \begin{pmatrix}
         -2.5 & 1 & 1.5 \\
         1 & -0.4 & -0.6 \\
         1.5 & -0.6 & -0.9
     \end{pmatrix}
     \begin{pmatrix}1 \\ -1 \\ 1\end{pmatrix} \\
  &= -0.08
\end{align*}
\end{enumerate}
\end{solution}