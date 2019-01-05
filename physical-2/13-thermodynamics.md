<!--
  vi: ft=pandoc.markdown
-->

# 热力学基础

热力学第一定律
: $Q = \Delta E + W$, $Q$: 系统从外界吸收的能量, $E$: 系统内能, $W$: 系统对外界做功

$V_1 \rightarrow V_2$系统对外界做功
: $W = \int_{V_1}^{V_2} p dV$

$\Delta E = \nu C_V \Delta T$

## 等容过程

摩尔定容热容
: $C_{V,m} = \frac{i}{2} R$

$\Delta Q = \Delta E = \nu C_{V} \Delta T$

## 等压过程

摩尔定压热容
: $C_{p,m} = (\frac{i}{2} + 1)R$

$\Delta Q = \nu C_p \Delta T$

## 等温过程

$pV = \nu RT \Rightarrow Q_T = W_T = \nu RT ln\ \dfrac{V_2}{V_1} = \nu RT ln\ \dfrac{p_1}{p_2}$

## 绝热过程

* $pV^\gamma$为常量
* $TV^{\gamma - 1}$为常量
* $p^{\gamma - 1}T^{-\gamma}$为常量
* 泊松比: $\gamma = \dfrac{i + 2}{i}$

## 热机和制冷剂

热机
: $p-V$正循环, 热效率$\eta = \dfrac{W}{Q_1} = \dfrac{Q_1 - Q_2}{Q_1}$, $Q_1$为吸热量, $Q_2$为放热量

制冷机
: $p-V$逆循环, 制冷系数$e = \dfrac{Q_2}{W} = \dfrac{Q_2}{Q_1 - Q_2}$, $Q_2$为吸热量, $Q_1$为放热量

## 卡诺循环

两个等温过程, 两个绝缘过程

卡诺热机效率
: $\eta = 1 - \dfrac{T_2}{T_1}$

卡诺制冷机制冷效率
: $e = \frac{T_2}{T_1 - T_2}$
