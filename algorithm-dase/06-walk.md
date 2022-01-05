# 随机游走

* 马尔科夫性: 只与上一时刻的状态有关
* 可约的(irreducible): 强连通
* 状态$x$的周期: $\{n | P^n_{x,x} > 0\}$的公约数
* 反周期(aperiodic): 所有状态周期为1
* PageRank: $pr^T = pr^T \cdot P$直至平稳
  * PageRank的改进: $P^{\prime} = \beta P + (1 - \beta) [\frac{1}{n}]_{n \times n}$