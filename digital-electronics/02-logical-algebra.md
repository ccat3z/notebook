<!--
    vi: ft=pandoc.markdown
-->

# 逻辑代数

## 基本定律和规则

### 常用恒等式

* $A + \widebar{A} \cdot B = A + B$
* $A \cdot B + \widebar{A} \cdot C + B \cdot C = A \cdot B + \widebar{A} \cdot C$
* $A \cdot B + \widebar{A} \cdot C + B \cdot C \cdot D = A \cdot B + \widebar{A} \cdot C$

### 对偶规则

`对偶规则`{.idx}

与, 或互换, 0, 1互换

## 表达形式

### 基本形式

`与-或表达式`{.idx} `或-与表达式`{.idx}

* 与-或表达式: $L = A \cdot C + \widebar{C} \cdot D$
* 或-与表达式: $L = (A + C) \cdot (B + \widebar{C}) \ cdot D$

### 最大项和最小项

注意下定义和性质(P46)

* 最小项

  $$L(A, B, C) = \sum m (3, 5) = \widebar{A}BC + A\widebar{B}C$$

* 最大项

  $$\begin{aligned}
    L(A, B, C) &= \prod M (3, 5) = \widebar{\sum m (3, 5)} \\
               &= (A + \widebar{B} + \widebar{C}) \cdot (\widebar{A} + B + \widebar{C})
  \end{aligned}$$

### 化简

* 化简形式

  $$\begin{aligned}
    L &= AC + \widebar{C}D & \text{与-或表达式} \\
      &= \overline{\overline{AC} \cdot \overline{\overline{C}D}} & \text{与非-与非表达式}
      &= (A + \widebar{C})(C + D) & \text{或-与表达式}
      &=
  \end{aligned}$$

* 卡诺图化简
