# 抽样算法

## 系统抽样

::: {.define latex=true}
**系统抽样**: 先随机抽一个样本, 然后按照一定规律选后面的样本.
:::

::: {.define latex=true}
**直线(圆形)等距抽样**:
假设在$N$个中抽$n$个,
在前$k = \frac{N}{n}$中随机抽一个,
然后每隔$k$抽取.
$\frac{N}{n}$不是整数时可以用圆形列表.
:::

## 分层抽样

## 水库抽样

::: {.define latex=true}
**水库抽样**: 从数据流中取$k$个数据

1. 先取$k$个进水库
2. 接下来的第$i$个元素以$\frac{k}{i}$的概率替换水库中的任意一个
:::

## 例题

\begin{problem}{28}{6}
从词库中随机等概率抽取100个单词，请写出水库抽样的主要步骤。
若被告知词库容量为10000，请设计合理的抽样方法抽取由100个单词组成的样本。
\end{problem}
\begin{solution}{解}
\begin{enumerate}[label=(\alph*)]
\item
    水库抽样的主要步骤:
    \begin{enumerate}[label=\arabic*.]
        \item 将数据流中的前100条记录保存下来
        \item 对于第m条记录 ($m > k$),
              以$\frac{k}{m}$的概率决定是否替换水库中的一条概率
        \item 重复执行第2步, 直至数据流终止
    \end{enumerate}
\item
    若知道词库容量为10000, 可以使用直线等距抽样。

    \[k = \frac{10000}{100} = 100\]

    在$1 \sim 100$中随机抽取一个变化$r$。
    取第$r + 100k$个数据,
    其中$1 \le r + 100k \le 10000$。
\end{enumerate}
\end{solution}

\begin{problem}{28}{15}
在水库抽样算法中，当第$i$个元素到达时，
以$\frac{1}{i}$的概率替换水库中选定的某个元素，
直到最后一个元素到达为止。试证明每个元素被选中的概率相等，
即为$\frac{1}{n}$。
\end{problem}
\begin{solution}{解}
\begin{enumerate}[label=(\alph*)]
\item
    当输入第1个元素时, 该元素必被选中($\frac{1}{i} = 1$)。
\item
    当输入第i个元素时, 该元素被选中的概率为$\frac{1}{i}$。
\item
    当输入第$i+1$个元素，
    只有当第$i+1$个元素不被选中时,
    第$i$个元素才会被保留。
    因此第$i$个元素仍保留在水库中的概率为:

    \[
        \frac{1}{i} ( 1 - \frac{1}{i+1} ) = \frac{1}{i+1}
    \]
\end{enumerate}

因此根据归纳假设，对于长度$n$的数据，水库抽样能保证每条记录以$\frac{1}{n}$
的概率保留在水库中，即每个元素被选中的概率相等。
\end{solution}