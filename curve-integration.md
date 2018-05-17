---
# vi: ft=markdown.pandoc
---

# 曲线积分与曲面积分

## 曲线积分

### 第一类曲线积分(对弧长的曲线积分)

$$\iint_L f(x, y, z) ds$$

$\left\{\begin{array}{l} x = \varphi(t)\\ y = \psi(t) \end{array}\right., (\alpha \leq t \leq \beta)$时, $\iint_L f(x, y) ds$ = $\int_\alpha^\beta f[\varphi(t), \psi(t)]\sqrt{\varphi^{'2}(t) + \psi^{'2}(t)}dt$

### 第二类曲线积分(对座标的曲线积分)

$$\iint_L Pdx + Qdy + Rdz$$

#### 与第一类曲线积分相互转换

$$\iint_L Pdx + Qdy + Rdz = \iint_L (Pcos \alpha + Qcos \beta + Rcos \gamma) ds$$

### 格林公式

二重积分与曲线积分相互转换

<div latex="true" class="mthm" args="格林公式" id="格林公式">
设闭区域$D$由分段光滑的曲线$L$围成, 若函数$P(x, y)$与$Q(x, y)$在$D$上具有一阶连续偏导数, 则有
$$\iint_D (\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}) dxdy = \oint_L Pdx + Qdy$$
</div>

## 曲面积分

### 第一类曲面积分

$$\iint_{\sum} f(x, y, z) dS = \iint_{D_{xy}} f[x, y, z(x, y)] \sqrt{1 + z_x^2(x, y) + z_y^2(x, y)} dxdy$$
