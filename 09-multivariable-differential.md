---
# vi: ft=markdown.pandoc
---

# 多元函数微分

## 多元函数的基本概念

### 平面点集

#### 邻域

$U(P_0, \delta) = \{ P \mid |P P_0| < \delta \}$

去心邻域 
: $\mathring{U}(P_0, \delta) = \{ P \mid 0 < |P P_0| < \delta \}$

##### 领域描述点与点集关系

\figref{点与点集关系}

\begin{figure}[htp]
    \centering
    \psscalebox{0.75}{\begin{pspicture*}(-3,-5)(3,3)\pscircle[linewidth=2pt,linestyle=dashed,dash=1pt 1pt,fillcolor=black,fillstyle=solid,opacity=0.16](1.88466,1.50033){0.83489}\pscircle[linewidth=2pt,linestyle=dashed,dash=1pt 1pt,fillcolor=black,fillstyle=solid,opacity=0.16](0.32207,-0.55827){0.78091}\pscircle[linewidth=2pt,linestyle=dashed,dash=1pt 1pt,fillcolor=black,fillstyle=solid,opacity=0.16](2.27518,-2.21389){0.71610}\rput{60.73200}(-0.16,-0.25){\psellipse[linewidth=2pt](0,0)(2.86614,1.96518)}\begin{scriptsize}\psdots[dotstyle=*](1.88466,1.50033)\rput[bl](1.91967,1.58952){$P_3$}\psdots[dotstyle=*](0.32207,-0.55827)\rput[bl](0.36154,-0.46310){$P_1$}\psdots[dotstyle=*](2.27518,-2.21389)\rput[bl](2.31154,-2.12387){$P_2$}\end{scriptsize}\end{pspicture*}}
    \caption{点与点集关系}\label{点与点集关系}
\end{figure}

* 内点: $P_1$
* 外点: $P_2$
* 边界点: $P_3$
* 聚点: $\forall \delta > 0, \mathring{U}(P_0, \delta) \text{内有} E \text{中点}$

#### 平面点集合分类

* 开集:
   \inlineps{\pscircle[linewidth=1pt,linestyle=dashed,dash=5pt 2pt,fillcolor=black,fillstyle=solid,opacity=0.33](0,0){1}}
* 闭集:
   \inlineps{\pscircle[linewidth=1pt,linestyle=solid,fillcolor=black,fillstyle=solid,opacity=0.33](0,0){1}}
* 连通集:
   \inlineps{\rput{90}(-0.43011,0.07747){\psellipse[linewidth=1pt,fillcolor=black,fillstyle=solid,opacity=0.27](0,0)(0.34095,0.22741)}\rput{65.44954}(0.51130,0.14720){\psellipse[linewidth=1pt,fillcolor=black,fillstyle=solid,opacity=0.23](0,0)(0.59639,0.39867)}}
   不是连通集
   * 区域 (开区域): 连通开集
   * 闭区域: 连通闭集
* 有界集
* 无界集

### 多元函数概念

极限
: $P_0(x_0, y_0) \text{是} D \text{的聚点}\ \exists A\ \forall \varepsilon\ P \in D \cap \mathring{U}(P_0, \delta)\ |f(P) - A| = |f(x,y) - A| < \delta$

连续
: $P_0(x_0, y_0) \text{是} D \text{的聚点}\ \lim_{(x, y)\rightarrow(x_0, y_0)} f(x, y) = f(x_0, y_0)$

    * 间断点

##### 有界连续多元函数点性质

* 具有最大最小值
* 介值定理
* 一致连续性: 各个二维切面上都连续

## 偏导数

`重点!偏导数`{.idx}

$$ \left. \frac{\partial f}{\partial x} \right|_{\begin{smallmatrix}x = x_0\\y = y_0\end{smallmatrix}} = f_x(x_0, y_0) $$

计算方法
: 把其他自变量看做常数

::: {.mthm latex=true}
高阶混合偏导数在其连续的条件下与求导次序无关
:::

## 全微分

偏增量和偏微分
: 

    $$ f(x + \Delta x, y) - f(x, y) \approx f_x(x, y) \Delta x $$
    左端是对x\uwave{偏增量}, 右端是对x\uwave{偏微分}

全增量
: $\Delta z = f (x + \Delta x, y + \Delta y) - f(x, y)$

可微与全微分
: \underline{全方向切线在同一平面}

    若全增量$\Delta z$可表示为: $\Delta z = A \Delta x + B \Delta y + o(\rho)$
    其中$A$, $B$仅与$x$, $y$有关, $\rho = \sqrt{(\Delta x)^2 + (\Delta y)^2}$,
    那么称$z = f(x, y)$在$(x, y)$\uwave{可微分}\
    $dz = A \Delta x + B \Delta y$ 为$z = f(x, y)$在$(x, y)$的\uwave{全微分}

(全)可微与(偏)可导的关系
: 

    `重点!可微与可导的关系`{.idx}

    \begin{align*}
        \text{可微} &\Rightarrow \text{可导} \\
        \text{可微} &\Leftarrow \text{可导且导函数连续} \\
        \text{可微} &\Rightarrow \text{连续}
    \end{align*}

    ::: {.mthm latex=true args="[可微一定可导]"}
    如果$z = f(x, y)$在点$(x, y)$可微, 那么该函数在点$(x, y)$点偏导数$\frac{\partial z}{\partial x}$与$\frac{\partial z}{\partial x}$必定存在,
    且全微分为
    $$
        dz = \frac{\partial z}{\partial x} dx + \frac{\partial z}{\partial x} dy
    $$
    又称\underline{叠加原理}
    :::

    ::: {.mthm latex=true args="[可导不一定可微]"}
    函数$z = f(x, y)$的偏导数$\frac{\partial z}{\partial x}$, $\frac{\partial z}{\partial y}$在点$(x, y)$连续, 那么该函数在该点可微分
    :::

### 全微分近似计算

::: {.example}
求$(1.04)^{2.02}$的近似值

$f(x, y)= x^y$, $x = 1, y = 2, \Delta x = 0.04, \Delta y = 0.02$, $(1.04)^{2.02} \approx 1 + f_x (1, 2) \times 0.04 + f_y (1, 2) \times 0.02 = 1.08$
:::

## 多元复合函数求导法则

### 通用复合

`重点!偏导数!多元复合`{.idx}

\label{多元复合函数通用求导法则}

对于$z = f(u, v)$, $u = \phi (x, y)$, $\Psi (x, y)$

$$
\begin{pmatrix}
    \dfrac{\partial z}{\partial x} & \dfrac{\partial z}{\partial y}
\end{pmatrix}=
\begin{pmatrix}
    \dfrac{\partial z}{\partial u} & \dfrac{\partial z}{\partial v}
\end{pmatrix}
\begin{pmatrix}
    \dfrac{\partial u}{\partial x} & \dfrac{\partial u}{\partial y} \\[8pt]
    \dfrac{\partial v}{\partial x} & \dfrac{\partial v}{\partial y}
\end{pmatrix}
$$

::: {.example}
$z = f(x + y, xy), \frac{\partial ^2 z}{\partial x \partial y}$

**补充**
:::

### 全微分形式不变性质

对于$z = f(u, v)$, $u = \phi (x, y)$, $v = \Psi (x, y)$, 且这两个函数具有连续偏导数

\begin{align*}
    dz &= \frac{\partial z}{\partial u} du + \frac{\partial z}{\partial v} dv \\
       &= \frac{\partial z}{\partial x} dx + \frac{\partial z}{\partial y} dy
\end{align*}

::: {.example}
设$z = e^u sin\ v$, $u = xy$, $v = x + y$, 求$\frac{\partial z}{\partial x}$, $\frac{\partial z}{\partial y}$

\begin{align*}
    dz &= d(e^u sin\ v) \\
       &= e^u sin\ v du + e^u cos\ v dv \\
       &= e^u sin\ v d(xy) + e^u cos\ v d(x + y) \\
       &= e^u sin\ v (ydx + xdy) + e^u cos\ v (dx + dy)
\end{align*}
:::

## 隐函数求导法

### 一个方程
对于$F(x, y, z) = 0$若函数$F(x, y, z)$在点$P(x_0, y_0, z_0)$的某一领域内具有连续偏导数

$$
\frac{\partial y}{\partial x} = - \frac{F_x}{F_y}
$$

### 方程组
\label{方程组定义隐函数求导}

对于$\begin{cases}F(x, y, u, v) = 0 \\ G(x, y, u, v) = 0\end{cases}$,
四个变量中一般只能有两个个变量独立变化,
因此可确定两个二元函数$\begin{cases}F(x, y, u(x, y), v(x, y)) = 0 \\ G(x, y, u(x, y), v(x, y)) = 0\end{cases}$,
应用\nameref{多元复合函数通用求导法则}则对两边对x求导可得
$\begin{cases}
F_x  + F_u \frac{\partial u}{\partial x} + F_v \frac{\partial v}{\partial x} = 0 \\
G_x  + G_u \frac{\partial u}{\partial x} + G_v \frac{\partial v}{\partial x} = 0
\end{cases}$
解得
$\begin{cases} \frac{\partial u}{\partial x} = \frac{\left|\begin{smallmatrix}-F_x && F_v \\ -G_x && G_v\end{smallmatrix}\right|}{\left|\begin{smallmatrix}F_u && F_v \\ G_u && G_v\end{smallmatrix}\right|} = -\frac{1}{J}\frac{\partial(F, G)}{\partial(x, v)} \\ \frac{\partial v}{\partial x} = \frac{\left|\begin{smallmatrix}F_u && -F_x \\ G_u && -G_x\end{smallmatrix}\right|}{\left|\begin{smallmatrix}F_u && F_v \\ G_u && G_v\end{smallmatrix}\right|} = -\frac{1}{J}\frac{\partial(F, G)}{\partial(u, x)} \end{cases}$

::: {.define latex=true args="[雅可比行列式]"}
$$
\frac{\partial (F, G)}{\partial (u, v)} = \begin{vmatrix}F_u & F_v \\ G_u & G_v\end{vmatrix}
$$
:::

## 多元函数微分学的几何应用

### 一元向量值函数及其导数(导向量)

### 空间曲线的切线和法平面
\label{空间曲线的切线和法平面}

对于空间曲线$\Gamma = \begin{cases} x = \varphi (t) \\ y = \psi (t) \\ z = \omega (t) \end{cases}$切向量为
$$
    T = \begin{pmatrix} \varphi^{'} (t_0) && \psi^{'} (t_0) && \omega^{'} (t_0) \end{pmatrix}
$$
切线方程为
$$
    \frac{x - x_0}{\varphi^{'} (t_0)} = \frac{y - y_0}{\psi^{'} (t_0)} = \frac{z - z_0}{\omega^{'} (t_0)}
$$
法平面方程
$$
    {\varphi^{'} (t_0)}({x - x_0}) + {\psi^{'} (t_0)}({y - y_0}) + {\omega^{'} (t_0)}({z - z_0}) = 0
$$
\begin{example}
    {对于空间曲线$\begin{cases} F(x, y, z) = 0 \\ G(x, y, z) = 0 \end{cases}$求切线与法平面}
    将$\begin{cases} F(x, y, z) = 0 \\ G(x, y, z) = 0 \end{cases}$看作
    $$\begin{cases} F(x, y(x), z(x)) = 0 \\ G(x, y(x), z(x)) = 0 \end{cases}$$
    对两边求全导数得
    $$\begin{cases}F_x  + F_y \dfrac{\partial y}{\partial x} + F_z \dfrac{\partial z}{\partial x} = 0 \\[8pt] G_x  + G_y \dfrac{\partial y}{\partial x} + G_z \dfrac{\partial z}{\partial x} = 0\end{cases}$$
    应用\ref{方程组定义隐函数求导}可得到
    $$\begin{pmatrix}\dfrac{dx}{dx} && \dfrac{dy}{dx} && \dfrac{dz}{dx}\end{pmatrix} = \begin{pmatrix} 1 && -\dfrac{1}{J}\dfrac{\partial(F, G)}{\partial(x, z)} && -\dfrac{1}{J}\dfrac{\partial(F, G)}{\partial(y, x)} \end{pmatrix}, J = \frac{\partial(F, G)}{\partial(y, z)}$$
    乘J可得切向量
    $$T = \begin{pmatrix} \dfrac{\partial(F, G)}{\partial(y, z)} && \dfrac{\partial(F, G)}{\partial(z, x)} && \dfrac{\partial(F, G)}{\partial(x, y)} \end{pmatrix}$$
    由此可得切线方程和法平面
\end{example}

### 曲面的切平面与法线

对于隐式确定的曲面方程$F(x, y, z) = 0$法向量为
$$n = (F_x, F_y, F_z)$$
切平面与法线参考\nameref{空间曲线的切线和法平面}

## 方向导数与梯度

### 方向导数

`重点!方向导数`{.idx}

若$f(x, y)$在点$P_0(x_0, y_0)$可微分, 那么函数在该点沿任一方向$l$的方向导数存在
$$
    \left.\frac{\partial f}{\partial l}\right|_{(x_0, y_0)} = f_x\ cos\ \alpha + f_y\ cos\ \beta
$$
$cos\ \alpha$和$cos\ \beta$是方向$l$的方向余弦, $(cos\ \alpha, cos\ \beta)$为$l$的单位向量

::: {.example}
求$z = xe^{2y}$在点$P(1, 0)$从$P(1, 0)$到$Q(2, -1)$的方向的方向导数

方向为$\vec{PQ} = (1, 1)$, $\vec{e_l} = (\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}})$
$$\left. \frac{\partial z}{\partial x} \right|_{(1, 0)} = 1, \left. \frac{\partial z}{\partial y} \right|_{(1, 0)} = 2$$

所以方向导数为$\left. \frac{\partial z}{\partial l} \right| _{(1, 0)} = 1 \times \frac{1}{\sqrt{2}} + 2 \times (- \frac{1}{\sqrt{2}}) = - \frac{\sqrt{2}}{2}$
:::

### 梯度

对于$f(x, y)$在点$P_0(x_0, y_0)$的梯度为
$$grad\ f = \nabla f = f_x \vec{i} + f_y \vec{j}$$
如果$f$在该点可微分, 那么
\begin{align*}
    \left.\frac{\partial f}{\partial l}\right|_{(x_0, y_0)} &= f_x\ cos\ \alpha + f_y\ cos\ \beta \\
    &= grad\ f \cdot \vec{e_l} = |grad\ f|\ cos\ \theta
\end{align*}
其中$\theta$为$grad\ f$与$\vec{e_l}$的夹角

由上式可得

$\theta = 0$
: 方向导数取最大值

$\theta = \pi$
: 方向导数取最小值

$\theta = \frac{\pi}{2}$
: 方向导数取0

## 多元函数的极值及其求法

### 无条件极值

若$z = f(x, y)$在点$(x_0, y_0)$的某领域内连续且有一阶及二阶连续偏导数, 又$f_x (x_0, y_0) = 0$, $f_y (x_0, y_0) = 0$,
令

$$\begin{cases}f_{xx} (x_0, y_0) = A \\ f_{xy} (x_0, y_0) = B \\ f_{yy} (x_0, y_0) = C\end{cases}$$

则取得极值条件如下:
\begin{itemize}
    \item $AC - B^2 > 0$时具有极值, 且当$A < 0$时有极大值, $A > 0$时有极小值
    \item $AC - B^2 < 0$时没有极值
    \item $AC - B^2 = 0$时不能确定
\end{itemize}

### 条件极值 拉格朗日乘数法

对于函数$z = f(x, y)$在附加条件$\varphi (x, y) = 0$下的可能极值点, 作拉格朗日函数
$$L(x, y) = f(x, y) + \lambda \varphi (x, y) = 0$$
求解方程组
$$
    \begin{cases}
        L_x = 0 \\
        L_y = 0 \\
        \varphi (x, y) = 0
    \end{cases}
$$
解得$(x, y)$即可能极值点

可扩展为三维形式
