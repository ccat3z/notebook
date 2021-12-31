# Sketch

## 数据流模型

根据对实际数组的影响不同:

1. 时间序列模型: 每次来一个新数据
2. 收银机模型: 每次输入一个增量
3. 十字转盘模型: 每次输入一个diff

根据元素重要度:

1. 界标模型: 某一时间t到现在
2. 滑动窗口模型: W窗口大小
3. 衰减窗口模型: 新到达的重要程度较高

## Misra Gries

使用k个计数器, 若计数器满了, 所有计数器减1

## Count Sketch

### 简单抽样算法

按照概率$p$存入元素, 最终概率为$\frac{c_i}{p}$,
$c_i$为存入的元元素个数.

### Basic Count Sketch

两个hash函数, 一个控制位置, 另一个控制+1还是-1

### Count Sketch

多个Basic Count Sketch取中位数

### Count-min Sketch

Count Sketch基础上, 改为取最小值, 只增