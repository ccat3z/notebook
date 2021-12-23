# 哈希

## 布隆过滤器

* `insert(v)`: 使用$k$个`hash`, 在`hash(v)`对应的位置标志$1$
* `exists(v)`: 使用$k$个`hash`, `hash(v)`对应的位置标志全部为$1$

### 误判率

插入$n$个元素后, `exists(v)`的错误率:

假设每个hash函数有m个可能结果，且平均分布.

\begin{align*}
    \varepsilon
        &= \overbrace{\prod_{i=1}^{k} P(X_i = 1)}^{\text{所有标志均为1}}
         = P(X_i = 1)^k \\
        &= (1 - P(X_i = 0))^k \\
        &= (1 - \overbrace{
            (\underbrace{1-\frac{1}{m}}_{\text{没有被单个hash选中}})^{kn}
            }^{\text{没有被n个元素的k个hash选中}})^k \\
        &\approx (1 - e^{-\frac{kn}{m}})^k
\end{align*}

最优解: $k = \ln 2 \cdot \frac{m}{n}$, $m \ge 1.44 n \log_2 \frac{1}{\varepsilon}$

## 局部敏感哈希 (LSH)

以Jaccard距离为例: $Jaccard(A, B) = \frac{|A \cap B|}{|A \cup B|}$

## k-Shingling

::: {.define latex=true}
文本中$k$个token组成的序列.
例如$D = abcab$, 2-Shingling为$\{ab, bc, ca\}$
:::

## Min-Hashing

::: {.define latex=true}
$h_{\pi}(C) = \min_{\pi} (C)$: 随机排列Shingles, 取第一个匹配的Shingle.
:::

::: {.mthm latex=true}
$P(h_{\pi}(C_1) = h_{\pi}(C_2)) = Jaccard(C_1, C_2)$
:::

### 最小哈希签名(矩阵)

::: {.define latex=true}
最小哈希签名:
使用$n$个随机排列进行最小哈希。
随机排列可以用`hash(index)`模拟。
:::

+---------+-------+-------+-------+
|         | $d_1$ | $d_2$ | $d_3$ |
+=========+=======+=======+=======+
| $\pi_1$ |  1    |  3    |  4    |
+---------+-------+-------+-------+
| $\pi_2$ |  2    |  2    |  1    |
+---------+-------+-------+-------+
| $\pi_3$ |  5    |  5    |  1    |
+---------+-------+-------+-------+

Table: 最小哈希签名矩阵

### 基于最小哈希的局部敏感哈希

::: {.define}
将最小哈希矩阵分为b组(bands), 每组r行.
每组有多个向量对应多个文档, 如果相同代表文档很可能相似.
:::

- [ ] 概率计算? P64