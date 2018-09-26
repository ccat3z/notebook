---
# vi: ft=pandoc.markdown
---

# 假设检验

`假设检验`{.idx}

原假设和备择假设
: 

   1. 双边检验: $H_0: \Theta = \Theta_0$, $H_1: \Theta \not= \Theta_0$
   1. 右边检验: $H_0: \Theta \leq \Theta_0$, $H_1: \Theta > \Theta_0$
   1. 左边检验: $H_0: \Theta \geq \Theta_0$, $H_1: \Theta < \Theta_0$

::: {.example}
右边检验$\mu_0 = -0.545, \sigma = 0.008, \bar{x} = -0.535, n = 5, a = 0.05$

原假设和备择假设: $H_0: \mu \leq \mu_0 = -0.545, H_1: \mu > \mu_0$

拒绝域: $z = \frac{\bar{x} - \mu_0}{\frac{\sigma}{\sqrt{n}}} = 2.7951 \geq z_{0.05} = 1.645$

即在显著性水平$a = 0.05$下拒绝$H_0$
:::
