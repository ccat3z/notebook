# 向量和矩阵的基础

## 向量和矩阵的概念

<!-- Lec2 -->

### 向量

<!-- Lec2 -->

### 矩阵

<!-- Lec2 -->

::: {.mthm latex=true}
矩阵的乘积满足下列规律：

1. 结合律 $(AB)C = A(BC)$
1. 左分配律 $A(B + C) = AB + AC$, 右分配律 $(B + C)A = BA + CA$。
:::

::: {.mthm latex=true}
分块矩阵乘法, 若$A$的列的分法与$B$的行的分法一致, 就和矩阵乘法一致.
:::

::: {.define latex=true}
**`#对称矩阵`**: $A = A^T$
:::

::: {.define latex=true}
**`#非奇异矩阵`**是**`#满秩矩阵`**.
:::

::: {.define latex=true}
**`#正交矩阵`**: $A^T = A^{-1}$
:::

::: {.define latex=true}
**`#k阶子式`**: 取$k$行$k$列. 
**`#k阶主子式`**: 取$k$行$k$列, 行列序号相等. 
**`#顺序主子式`**: 取$[11:11], [11:22], \ldots, [nn,nn]$.
:::

## 向量空间

<!-- Lec3 -->

### 向量间线性关系

::: {.define latex=true}
如果两个向量组互相可以线性表出， 则称为它们**`#等价`**。
:::

#### 生成集、基底和坐标

::: {.define latex=true}
**`#生成集`**$\{a_1, a_2, \ldots, a_r\}$
**`#张成的子空间`**
$L(a_1, a_2, \ldots, a_r)$或$span(a_1,a_2,...,a_r)$
:::

::: {.define latex=true}
**`#基`**为线性无关的**`#生成集`**.
:::

::: {.define latex=true}
**`#维数`** $dim(\mathbb{V})$
$=$ (**`#秩`**) $rank\{a_1 , a_2 , \ldots , a_r\}$
:::

### 线性组合

::: {.example}
已知$\beta = (1, 2, 1, 1)^T$, 以及
$\alpha_1 = (1, 1, 1, 1)^T$, $\alpha_2 = (1, 1, −1, −1)^T$,
$\alpha_3 = (1, −1, 1, −1)^T$, $\alpha_4 = (1, −1, −1, 1)^T$.
试将向量$\beta$表示成$\alpha1$, $\alpha2$, $\alpha3$, $\alpha4$的线性组合.

假设$k_1$, $k_2$, $k_3$, $k_4$为组合系数,
将$\beta$表示成$\alpha1$, $\alpha2$, $\alpha3$, $\alpha4$的线性组合.
即求解:

$$
    \begin{pmatrix}
        1 &  1 &  1 &  1 \\
        1 &  1 & -1 & -1 \\
        1 & -1 &  1 & -1 \\
        1 & -1 & -1 &  1
    \end{pmatrix}
    \begin{pmatrix}
        k_1 \\ k_2 \\ k_3 \\ k_4
    \end{pmatrix}
    =
    \begin{pmatrix}
        1 \\ 2 \\ 1 \\ 1
    \end{pmatrix}
$$

使用初等变换法求解线性方程组:

\begin{multline*}
    \begin{pmatrix}
        1 &  1 &  1 &  1 & 1 \\
        1 &  1 & -1 & -1 & 2 \\
        1 & -1 &  1 & -1 & 1 \\
        1 & -1 & -1 &  1 & 1
    \end{pmatrix}
    \rightarrow
    \begin{pmatrix}
        1 &  1 &  1 &  1 & 1 \\
        0 &  0 & -2 & -2 & 1 \\
        1 & -1 &  1 & -1 & 1 \\
        0 &  0 & -2 &  2 & 0
    \end{pmatrix}
    \rightarrow
    \begin{pmatrix}
        1 &  1 &  1 &  1 & 1 \\
        1 & -1 &  1 & -1 & 1 \\
        0 &  0 &  1 &  0 & -\frac{1}{4} \\
        0 &  0 &  0 &  1 & -\frac{1}{4}
    \end{pmatrix}
    \rightarrow \\
    \begin{pmatrix}
        1 &  1 &  0 &  0 & \frac{3}{2} \\
        1 & -1 &  0 &  0 & 1 \\
        0 &  0 &  1 &  0 & -\frac{1}{4} \\
        0 &  0 &  0 &  1 & -\frac{1}{4}
    \end{pmatrix}
    \rightarrow
    \begin{pmatrix}
        1 &  0 &  0 &  0 & \frac{5}{4} \\
        0 &  1 &  0 &  0 & \frac{1}{4} \\
        0 &  0 &  1 &  0 & -\frac{1}{4} \\
        0 &  0 &  0 &  1 & -\frac{1}{4}
    \end{pmatrix}
\end{multline*}

可得:

$$
    \beta = \frac{5}{4}\alpha_1 + \frac{1}{4}\alpha_2
    - \frac{1}{4}\alpha_3 - \frac{1}{4}\alpha_4
$$
:::

## 线性映射

<!-- Lec4 -->

::: {.define latex=true}
**`#线性映射`**
$\varphi: \mathbb{V} \rightarrow \mathbb{W}
\Leftrightarrow
\varphi(\alpha x + \beta y) = \alpha \varphi(x) + \beta \varphi(y)$
:::

::: {.define latex=true}
(`#等价`和`#相似`是不同基的变换矩阵)

* $A = T^{-1} B S$成立, $A$, $B$**`#等价`**.
* $A = T_S(B) = S^{-1} B S$成立, $A$, $B$**`#相似`**.
  称$T$为**`#相似变换`**.
:::

### `#核空间`和`#像空间`

### 线性变换

::: {.define latex=true}
**`#线性变换`**
满足$\varphi: \mathbb{V} \rightarrow \mathbb{V}$的`#线性映射`.
:::

#### 初等变换

::: {.define latex=true}
由单位矩阵$I$经过一次初等行 (列) 变换得到的矩阵称为**`#初等矩阵`**.
:::

齐次方程组通解? <!-- https://www.bilibili.com/read/cv2649977 -->

#### 逆

::: {.define latex=true}
\label{可逆矩阵与初等矩阵}
`逆矩阵`{.idx}

$n$阶矩阵$A$可逆 $\Leftrightarrow$
$A = Q_1 Q_2 \ldots Q_m$,
$Q_i$为初等矩阵.
:::

::: {.prop latex=true}
`逆矩阵`{.idx}
由\ref{可逆矩阵与初等矩阵}可得: $(Q_1 Q_2 \ldots Q_m)^{-1} (A I) = (I A^{-1})$
:::

::: {.define latex=true}
**`#广义逆`**: $(A^T A)^{-1} A^T$
:::

## `#行列式`

<!-- Lec5 -->
<!-- P67 -->

::: {.define latex=true}
`逆序`{.idx} `逆序数`{.idx}
一个排列中，如果一个大元素在小
元素前，则称这两个数构成一个**逆序**。
一个排列中存在的所有逆序的数目称为排列的
**逆序数**: $\tau(j_1 , j_2 , \ldots , j_n)$.
:::

::: {.define latex=true}
$n$ 阶行列式中，
划去元素 $a_{ij}$ 所在第 $i$ 行和第 $j$ 列元素，
剩余的元素按原来的次序组成的
$n − 1$ 阶行列式称为元素 $a_ij$的
**`#余子式`**，记成 $M_{ij}$ 。令 $A_{ij} = (−1)^{i+j} det(M_{ij})$ ，
称 $A_{ij}$ 是元素 $a_{ij}$的**`#代数余子式`**。
:::

::: {.define latex=true}
**`#行列式`**:
\begin{align*}
det(A) = 
\begin{vmatrix}
a_{11} & \ldots & a_{1n} \\
\vdots & \ddots & \vdots \\
a_{n1} & \ldots & a_{nn}
\end{vmatrix}
&=
\sum_{j_i, \ldots, j_n}
(-1)^{\tau(j_1 , j_2 , \ldots , j_n)} a_{1 j_1} \ldots a_{n j_n} \\
&=
\sum_{j=1}^n a_{ij} A_{ij} \text{(按行展开)}
\end{align*}
:::

::: {.prop latex=true}
`#行列式`即有向体积
:::

::: {.prop latex=true}
设$A, B \in R^{n \times n}$

* $det(A) = det(A^T)$
* $det(aA) = a^n det(A)$
* $det(AB) = det(BA) = det(A) det(B)$
:::

::: {.mthm latex=true}
`#克莱姆法则`? `(Lec5#12)`
:::

::: {.prop latex=true}
交换矩阵两行(或两列) 改变矩阵行列式的符号
:::

::: {.prop latex=true}
行列式关于矩阵的每行(或每列) 是线性的。
:::

::: {.prop latex=true}
如果将行列式的某一行 (列)k 倍加到另一行 (列)，则行列式的值不变。
:::

::: {.define latex=true}
**`#伴随矩阵`**: $A^{*}_{ij} = A_{ji}$
:::

::: {.mthm latex=true}
$$
\sum_{k=1}^n a_{ik} A_{jk} =
\begin{cases}
|A| & i = j \\
0 & i \neq j
\end{cases}
$$
$$
AA^* = A^*A = |A|I
$$
:::

## 迹

<!-- Lec5 -->

::: {.define latex=true}
**`#迹`**: $Tr(A) = \sum_{i=0}^n a_{ii}$
:::

::: {.prop latex=true}
**迹的循环不变性**`迹!循环不变性`{.idx}
$$Tr(ABC) = Tr(CAB) = Tr(BCA)$$

同理`#相似矩阵`的迹相等:
$$Tr(Q^{−1} AQ) = Tr(QQ^{−1} A) = Tr(A)$$
:::

## 二次型

<!-- Lec5 -->

::: {.define latex=true}
定义$f$为`#二次型`, $A$为`#二次型矩阵` (`#对称矩阵`).

\begin{align*}
f(x_1, x_2, \ldots, x_n) =
&\ a_{11} x_1^2 + 2 a_{12} x_1 x_2 + \ldots + 2 a_{1n} x_1 x_n \\
&  + \ldots + a_{nn} x+n^2 \\
= &\ x^T A x = Tr(x^T A x)
\end{align*}
:::

::: {.define latex=true}
$A$**`#合同`**于$B$, $A \simeq B$: $C^T A C = B$.
(即不同基下的二次型)
:::

::: {.prop latex=true}
**`#合同变换`**:

* 交换$A$的第$i$行和第$j$行，再交换其第$i$列和第$j$列；
* 将$A$的第$i$行乘以非零常数$k$，再将其第$i$列乘以$k$；
* 将$A$的第$i$行乘以$k$加到第$j$行，再将其第$i$列乘以$k$加到第$j$列。
:::

::: {.define latex=true}
设$A$是属于$K$上的非零对称矩阵,
则必存在非奇异矩阵$C$，使$C^T A C$的第$1$行第$1$个元素不为零.
:::

::: {.define latex=true}
设$A$是属于$K$上的非零对称矩阵,
则必存在非奇异矩阵$C$，使$A$合同于$C^T A C = \begin{pmatrix}
a_{11}^{\prime} & 0_{1 \times k} \\
0_{k \times 1} & \lambda{k \times k}
\end{pmatrix}$.
:::

### 标准型

::: {.define latex=true}
`#线性替换`: 使用$y_i$替换$x_i$, $x_{n \times 1} = C_{n \times n} y_{n \times 1}$.
当$det(C) > 0$时, 线性替换非退化.
:::

::: {.define latex=true}
每一个`#二次型`都能非退化的`#线性替换`化为平方和, 称为**`#标准型`**.
`#标准型`不唯一.
:::

::: {.mthm latex=true}
每一个`#二次型矩阵`都能通过`#合同变化`为`#对角矩阵`.

$$
\begin{pmatrix} A \\ I \end{pmatrix}
\xrightarrow{\text{对A合同变化}}
\begin{pmatrix} D \\ C \end{pmatrix}
$$

$D$是对角矩阵, $C$是非退化的`#线性替换`矩阵.

例如将$f(x)$替换为`#标准型`$g(y) = y^T D y$, $x = Cy$.
:::

::: {.mthm latex=true}
`#二次型`矩阵的`#特征值`即`#标准型`的系数.
:::

### 规范型

::: {.define latex=true}
**`#规范性`**即在**`#标准型`**的基础上把系数变成$1$和$-1$.
**`#正惯性指数`** $p$为$1$的数量.
**`#负惯性指数`** $r-p$为$-1$的数量.
:::

### 正定型

::: {.define latex=true}
令$x \neq 0$.
**`#正定二次型`**: $x^T A x > 0$, $A$为**`#正定矩阵`**.
**`#半正定二次型`**: $x^T A x \ge 0$, $A$为**`#半正定矩阵`**
`负定二次型`{.idx} `半负定二次型`{.idx}
:::

::: {.prop latex=true}
`#正定二次型`的等价条件:

1. $x^T A x > 0$ (定义).
2. `#标准型`/`#规范型`系数全部为正数, `#正惯性指数`等于$A$的`#秩`.
3. `#顺序主子式`全大于$0$ (对于`#负定二次型`: 奇数阶全小于0, 偶数阶全大于0).
:::

## 特征值

<!-- Lec5 -->

::: {.define latex=true}
$Ax = \lambda x \Rightarrow det(\lambda I - A) = 0$
:::

## 内积和范数

<!-- Lec6 -->

### 范数

::: {.define latex=true}
**`#范数`** $||x||$ 满足:

1. 非负性: $\begin{cases}||x|| > 0 & x \not= 0\\||x|| = 0 & x = 0\end{cases}$
2. 齐次性: $||\lambda x|| = |\lambda| ||x||$
3. 三角不等式: $||x+y|| \le ||x|| + ||y||$
:::

::: {.define latex=true}
`lp范数`{.idx} **$l_p$范数**:

$$||x||_p = (\sum_{i=1}^{n}|x_i|^p)^{\frac{1}{p}}, 1 \le p < \infty$$

$l_1$范数, 1范数, Manhattan范数

$l_2$范数, 2范数, 欧几里得范数
:::

::: {.define latex=true}
$l_0 = \text{非零元素个数}$, $l_0$并不符合范数定义

$l_\infty = \max_j |x_i|$
:::

### 内积

::: {.define latex=true}
**`#内积`**: $\langle \cdot, \cdot \rangle: \mathbb{V} \times \mathbb{V} \rightarrow \mathbb{R}$, 并满足以下条件

1. 非负性：$\langle x, x \rangle \ge 0, \langle x, x \rangle = 0$ 当且仅当 $x = 0$
2. 对称性：$\langle x, y \rangle = \langle y, x \rangle$
3. 齐次性：$\langle \lambda x, y \rangle = \lambda \langle x, y \rangle$
4. 线性性：$\langle x + y, z \rangle = \langle x, z \rangle + \langle y, z \rangle$
:::

::: {.define latex=true}
**`#点积`** (`#标准内积`): $\langle x, y \rangle = x^T y$
:::

### 距离

::: {.define latex=true}
**`#距离`**: $d: \mathbb{V} \times \mathbb{V} \rightarrow \mathbb{R}$, 满足:

1. 非负性: $d(x, y) \ge 0$, 且$d(x, y) = 0 \Leftrightarrow x = y$
1. 对称性: $d(x, y) = d(y, x)$
1. 三角不等式: $d(x, z) \le d(x, y) + d(y, z)$
:::

::: {.define latex=true}
**`#欧式距离`**: $d(x, y) = ||x - y|| = \sqrt{\langle x - y, x - y \rangle}$.
其中内积定义为点积.
:::

### 夹角

::: {.define latex=true}
**`#夹角`**: $\cos \theta = \frac{\langle x, y \rangle}{||x||_2 ||y||_2}$
:::

::: {.define latex=true}
**`#正角`**: $\langle x, y \rangle = 0$,
如果$||x|| = ||y|| = 1$, 则为**`#标准正交`**.
:::

### 矩阵内积和范数

::: {.define latex=true}
**`#向量化`**: $vec(A)$: 将$m \times n$的矩阵拉长为$mn x 1$向量
:::

::: {.define latex=true}
**`#矩阵内积`**: $\langle A, B \rangle = \langle vec(A), vec(B) \rangle = vec(A)^T vec(B) = Tr(A^T B)$
:::

::: {.define latex=true}
**`#广义矩阵范数`**: 和向量范数的条件类似.

**`#矩阵范数`**: 附加`#相容性条件`: $||AB|| \le ||A|| ||B||$.
:::

::: {.define latex=true}
常见矩阵范数

* **$l_1$范数**: $||A||_{m_1} = \sum_{i=1}^m \sum_{j=1}^{n} |a_{ij}|$
* **$l_2$范数**, **`#Fiobenius范数`**:
  $||A||_{F} = (\sum_{i=1}^m \sum_{j=1}^{n} |a_{ij}|^2)^\frac{1}{2}$
* **$l_\infty$范数** (广义): $||A||_{m_\infty} = \max |a_{ij}|$
:::

#### 算子范数

::: {.define latex=true}
相容的向量范数和矩阵范数: $||Ax||_v \le ||A||_M ||x||_v$
:::

::: {.define latex=true}
由向量范数$||\cdot||_v$诱导出的**`#算子范数`**:
$||A|| = \max \{ ||Ax||_v : ||x||_v = 1 \}$
:::

::: {.define latex=true}
常见的算子范数, 对于$A \in \mathbb{R}^{m \times n}$

* `#1范数`: $||A||_1 = \max_{1 \le j \le n} \sum_{i=1}^m |a_{ij}|$, 列向量的$l_1$范数最大值
* `#∞范数`: $||A||_\infty = \max_{1 \le i \le m} \sum_{j=1}^n |a_{ij}|$, 行向量的$l_1$范数最大值
* `#2范数`: $||A||_2 = \sqrt{\lambda_{max} (A^T A)}$
:::