# Sketch

## 数据流模型

根据对实际数组的影响不同:

1. 时间序列模型: 每次来一个新数据
2. 收银机模型: 每次输入一个增量
3. 十字转盘模型: 每次输入一个diff

根据元素重要度:

1. 界标模型: 某一时间t到现在
2. 滑动窗口模型: W窗口大小
3. 衰减窗口模型: 新到达的重要程度较高

## Misra Gries

使用k个计数器, 若计数器满了, 所有计数器减1

## Count Sketch

### 简单抽样算法

按照概率$p$存入元素, 最终概率为$\frac{c_i}{p}$,
$c_i$为存入的元元素个数.

### Basic Count Sketch

两个hash函数, 一个控制位置, 另一个控制+1还是-1

### Count Sketch

多个Basic Count Sketch取中位数

#### 例题

::: {.example}
证明$\bar{f_a} = \text{median}_{1 \le i \le t} g_i(a) C[i] [h_i (a)]$中$t = O(log(1/\delta))$

``` {=latex}
$E(\bar{f_a}) = f_a$, $Var(\bar{f_a}) = \frac{||f_{-a}||_2^2}{k}$

$
P(|\bar{f_a} - f_a| \ge \epsilon ||f||_2)
\le P(|\bar{f_a} - f_a| \ge \epsilon ||f_{-a}||_2)
\le \frac{Var(\bar{f_a})}{\epsilon^2 ||f_{-a}||_2^2}
= \frac{1}{k \epsilon^2}
$

令$\frac{1}{k\epsilon^2} = \frac{1}{3}$, 定义:

\[
    Y_i = \begin{cases}
        1 & |\bar{f_a} - f_a| \ge \epsilon ||f||_2 \\
        0
    \end{cases}
\]

则有$P(Y_i = 1) \le \frac{1}{3}$, 记$\mu = E(\sum_{i=1}^{t} Y_i) \le \frac{t}{3}$

$P(\sum_{i=1}^{t} Y_i > \frac{t}{2}) \le P(\sum_{i=1}^{t} Y_i > (1 + \frac{1}{2}) \mu) \le exp(-\frac{\mu}{16}) < \delta$

$exp(-\frac{t}{48}) \le exp(-\frac{\mu}{16}) < \delta$
```
:::

::: {.example}
$\bar{f_a} = \frac{g_i(a) C[i] [h_i (a)]}{t}$, 分析性能

``` {=latex}
$Var(\bar{f_a}) = \frac{||f_{-a}||_2^2}{tk}$

$
P(|\bar{f_a} - f_a| \ge \epsilon ||f||_2)
\le P(|\bar{f_a} - f_a| \ge \epsilon ||f_{-a}||_2)
\le \frac{Var(\bar{f_a})}{\epsilon^2 ||f_{-a}||_2^2}
= \frac{1}{t k \epsilon^2} < \delta
$

因此$t = O(\frac{1}{\epsilon^2 \delta})$
```
:::

### Count-min Sketch

Count Sketch基础上, 改为取最小值, 只增.
计数器个数: $O(\log(1/\delta) / \epsilon)$