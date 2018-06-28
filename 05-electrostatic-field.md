---
# vi: ft=markdown.pandoc
---

# 静电场

* $\mathit{e} = 1.602 \times 10^{-19} C$
* $\varepsilon_{0} = 8.85 \times 10^{-12} C^2 \cdot N^{-1} \cdot m^{-2}$
* $1eV = 1.602 * 10^{-19} J$

电场强度
: $E = \frac{F}{q_0}$

电场强度通量(电通量)
: $\Phi_e = \oint_s \vec{E} \cdot d \vec{S}$

电势差
: $U_{A \rightarrow B} = \int_A^B \vec{E} \cdot d \vec{l}$

电势
: $V_A = U_{Al_0}$, $l_0$为零势能面

电势能 
: $E_{pA} = q_0 \int_{AB} \vec{E} \cdot d \vec{l}\ (E_{pB} = 0)$

库伦定理
: $F = \frac{1}{4 \pi \varepsilon_{0}} \frac{q_1 \Rightarrow q_2}{r^2} \vec{e_r}$

高斯定理
: $\phi = \oint_{S} E \cdot dS = \frac{q}{\varepsilon _{0}}$

## 常见带电物体

1. 点电荷

   电场强度
   : $E = \frac{1}{4 \pi \varepsilon _{0}} \frac{Q}{r^2} \vec{e_r}$

   电势
   : $V = \int_A^\infty \frac{q}{4\pi\varepsilon_0 r^2} dr = \frac{1}{4\pi\varepsilon_0} \frac{q}{r}$

1. 球面

   电场强度
   : $E = \begin{cases} 0 & r \leq R \\ \frac{1}{4 \pi\varepsilon_0} \frac{Q}{r^2} & r > R\end{cases}$

   电势
   : $V = \begin{cases} \frac{1}{4 \pi\varepsilon_0} \frac{Q}{R} & r \leq R \\ \frac{1}{4 \pi\varepsilon_0} \frac{Q}{r} & r > R\end{cases}$

   ::: {.example}
   半径为R, 均匀带电为Q的球面, 求电场强度, 球内任意两点电势差, 球外任意两点电势差, 球内任意点电势, 球外任意点电势

   1. 电场强度

      以$r$为半径作一球面$O$,

      **当$r \leq R$时**, $O$内$\sum q = 0$, $E \times 4\pi r^2 = 0$

      **当$r > R$时**, O内$\sum q = Q$, $E \times 4\pi r^2 = \frac{Q}{\varepsilon_0} \Rightarrow E = \frac{Q}{4\pi\varepsilon_0 r^2}$

   1. 球内两点电势差
    
      $$E = 0 \Rightarrow U_{AB} = 0$$

   1. 球外两点电势差

      $$U_{AB} = \int_A^B \frac{1}{4\pi\varepsilon_0} \frac{Q}{r^2} = \frac{Q}{4\pi\varepsilon_0} (\frac{1}{r_A} - \frac{1}{r_B})$$

   1. 球外任意点电势

      $$V(r) = U_{r\infty} = \frac{Q}{4\pi\varepsilon_0 r}$$

   1. 球内任意点电势

      $$V(r) = V(R) = \frac{Q}{4\pi\varepsilon_0 R}$$
   :::

1. 无限均匀带电直线

   电场强度
   : $E = \frac{1}{4\pi\varepsilon_0} \frac{2\lambda}{r}$

   电势
   : $V = \frac{1}{4\pi \varepsilon_0} 2\lambda ln \frac{r_B}{r}$

   ::: {.example}
   无限长均匀带电直线, 电荷线密度为$\lambda$

   作半径为$r$, 高为$h$的圆柱面

   $$E \times 2\pi rh = \frac{\lambda h}{\varepsilon_0} \Rightarrow E = \frac{\lambda}{2\pi\varepsilon_0 r}$$
   :::

1. 无限均匀带电平面

   电场强度
   : $E = \frac{\sigma}{2\varepsilon_0}$

   ::: {.example}
   无限长均匀带电平面, 电荷面密度为$\sigma$

   如图作圆柱体 \
   ![](./images/electrostatic-field/surface.svg){width=100px}

   (前后两个圆面)电场强度通量为$E \times 2 \pi r^2$，
   所包含的电量$\sigma \times \pi r^2$

   可得$E = \frac{\sigma}{2\varepsilon_0}$
   :::
