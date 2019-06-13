# 图论

## 图

A与B无序积
: $A \& B = \{ \{a, b\} \mid a \in A \wedge b \in B \}$

无序对
: $(a, b)$

有穷多重子集
: 某元素可重复出现

无向图
: $G = \langle V, E \rangle$, $V$是非空有穷集， $E$是$V\ \&\ V$的有穷多重子集

有向图
: $D = \langle V, E \rangle$, $V$是非空有穷集， $E$是$V \times V$的有穷多重子集

阶
: 图顶点数

零图
: 没有边的图

n阶零图
: $N_n$

平凡图
: $N_1$

空图
: 顶点集为空 (运算过程中出现)

(非)标定图(图形表示图时)
: 每个顶点和边都有符号

$e_k$与$v_i$关联
: $e_k=(v_i, v_j)$

关联次数
: `length $ filter (== vi) ek`{.haskell}

孤立点
: 顶点无关联边

环
: $e_k$与$v_i$关联次数为2

$v_i$与$v_j$相邻
: $(v_i, v_j) \in E$

$v_i$是终点
: $<v_j, v_i> \in E$

$v_i$是始点
: $<v_i, v_j> \in E$

$e_i$与$e_j$相邻(无向图)
: $e_i$与$e_j$有至少一个公共端点

$e_i$与$e_j$相邻(有向图)
: 一条边的终点是另一条的始点

平行边
: 端点相同(方向相同)

多重图
: 含平行边的图

简单图
: 不含平行边也不含环的图

<!-- TODO P296 -->

## 通路和回路

通路
: $\Gamma = v_{i_0}e_{j_0}v_{i_1}e_{j_1}\ldots e_{j_l}v_{i_l}$

通路的长度
: $\Gamma$中边的个数

回路
: $v_{i_0} = v_{i_l}$

简单通路(回路)
: 无重复边

初级通路, 路径
: 无重复顶点($v_{i_0}$, $v_{j_0}$除外)的简单通路

初级通路, 圈
: 无重复顶点($v_{i_0}$, $v_{j_0}$除外)的简单回路

## 图的连通性

### 无向图

连通 $u \sim v$
: $u, v \in V$, $u$与$v$之间存在通路. $\forall v \in V, v \sim v$

连通图 $\langle V, E \rangle$
: $\forall u, v \in V, u \sim v$

连通分支
:  $V$关于顶点之间连通关系$\sim$的一个等价类

连通分支数 $p(G)$
: $p(G) = 1$时, G为连通图

短程线
: $u$与$v$间最短通路

距离 $d(u, v)$
: 短程线的长度

### 有向图

可达 $u \rightarrow v$
: $u, v \in V$, $u$与$v$之间存在通路

相互可达 $u \leftrightarrow v$
: $u \rightarrow v \wedge u \leftarrow v$

短程线
: 同无向图

距离 $d<u, v>$
: 同无向图


<!--
    vi: ft=pandoc.markdown
-->
