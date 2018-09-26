---
# vi: ft=markdown.pandoc
---

# 重积分

## 二重积分

`重点!二重积分`{.idx}

$$\iint _ {D} f(x, y) d\sigma$$

### 换元法

$$\iint _ {D} f(x, y) dx dy = \iint _ {D^{'}} f (x(u, v), y(u, v)) |J(u, v)| dudv$$
其中$J(u, v)$为雅可比式$J(u, v) = \frac{\partial (x, y)}{\partial (u, v)}$

极座标
: $\iint _ {D} f(x, y) dx dy = \iint _ {D^{'}} f (\rho cos\ \theta, \rho sin\ \theta) \rho d\rho d\theta$


## 三重积分

`重点!三重积分`{.idx}

$$\iiint _ {\Omega} f(x, y, z) dv$$

## 重积分的应用

### 曲面的面积

对于曲面$z = f(x, y)$面积可写为

$$A = \iint _{D} \sqrt{1 + f_x^2 + f_y^2} d\sigma$$

### 质心

对于面密度为$\mu (x, y)$的薄片, 质心为

$$(\bar{x}, \bar{y}) = (\frac{\iint _{D} x \mu (x, y) d\sigma}{\iint _{D} \mu (x, y) d\sigma}, \frac{\iint _{D} y \mu (x, y) d\sigma}{\iint _{D} \mu (x, y) d\sigma})$$

若密度均匀

$$(\bar{x}, \bar{y}) = (\frac{\iint _{D} x d\sigma}{A}, \frac{\iint _{D} y d\sigma}{A})$$

$A = \iint _{D} d\sigma$为面积

