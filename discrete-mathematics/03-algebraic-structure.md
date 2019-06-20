<!--
    vi: ft=pandoc.markdown
-->

# 二元运算

**封闭**

幂等律
: $\forall x \in S, x \times x = x$

吸收率
: $\circ$, $\times$是两个可交换的二元运算, $x \times (x \circ y) = x \circ (x \times y) = x$

## 特殊元

{左, 右, }幺元 (单位元) $e_l$
: $e_l \circ x = x$, 

{左, 右, }零元 $\theta_l$
: $\theta_l \circ x = \theta_l$

## 特殊运算

* 模n加法 $\oplus$
* 模n乘法 $\otimes$
* r整除k $r | k$

# 代数系统

同类型代数系统
: $\langle A, +, \times, 0, 1 \rangle$, $\langle B, *, \circ, x, y \rangle$

## 同态映射

同态映射
: {单, 满}(自)同态, 同构, 零同态(映射到幺元)

##### 同态判定

\ 

$V_1 = \langle A, \circ \rangle$, $V_2 = \langle B, * \rangle$

1. $f: A \rightarrow B, \forall x \in A, f(x) \in B$
2. $\forall x, y \in A, f (x \circ y) = f(x) * f(y)$

## 群

半群
: $V = \langle S, \circ \rangle$, $\circ$是二元运算, 满足结合律

幺半群(独异点)
: $e \in S$

群
: $\forall a \in  S, a^{-1} \in S$

平凡群
: 只有幺元

交换群, Abel群
: 可交换

### 特殊群

#### Klein四元群

$G = {e, a, b, c}$

1. $e$为幺元
1. $G$中运算可交换
1. $\forall x \in G, x^{-1} = x$
1. 任意两个元素运算的结果都等于另一个元素

子群: 生成子群 + 群本身

#### 循环群

$G = \langle a \rangle$

子群: 生成子群

##### 例题

1. 判定, 求单个生成元: $\exists a \in G, |a| = |G|$
1. 生成元: $\text{生成元}^{\text{与}|G|\text{互质}}$
1. {$n = |G|\text{的正因子}$}阶子群: $\langle \text{生成元}^{\frac{|G|}{n}} \rangle$
