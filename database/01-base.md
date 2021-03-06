---
# vi: ft=pandoc.markdown
---

# 概述

## 数据处理与数据管理

数据处理
: 指信息的收集, 管理, 加工, 传播等一系列活动的总和

数据管理
: 数据管理是指对数据进行分类, 组织, 编码, 存储, 检索和维护. 是数据处理的基本环节, 是任何数据处理业务中必不可少的共有部分, 是数据处理的中心问题

## 数据库技术

数据库技术主要研究**数据的管理**问题

### 数据库管理技术的发展

1. 人工管理阶段
1. 文件系统阶段

    1. 数据共享性差, 冗余度大
    1. 程序与数据之间独立性不高
    1. 数据缺乏统一的管理和控制

1. 数据库系统阶段(**60年代后期**)

### 数据库技术的特点

1. **整体结构化(主要特征, 与文件系统的区别)**, 数据的共享性高, 冗余度小
1. 程序与数据之间的独立性高
1. 数据得到统一的管理和控制

文件系统是数据库技术的基础, 数据库技术中的读写操作通过文件系统实现

### 开发信息系统时采用数据库技术的原因

尽管有各种各样的信息系统, 但它们的**主要功能都是进行信息处理(即数据处理)**, 而数据处理都涉及到数据的管理问题. \sout{如果数据的管理由各个信息系统自己去实现, 不但耗时耗钱, 而且系统的稳定性, 可靠性, 安全性, 响应时间都不能得到保证.} 因为数据管理软件的编写是一项专业性很强的工作, 不是一般的程序员可以胜任的. 采用数据库技术后, 数据的管理就由DBMS去完成, 而DBMS是专业公司开发的, **系统的稳定性, 可靠性, 安全性, 响应时间都有保证**, 而且**缩短了系统的开发时间, 节约了成本**

## 数据库系统(DBS)的组成

`数据库系统`{.idx}
`DBS`{.idx}

数据库系统(DBS)
: 包括软硬件 *补充? P6*, 由数据库(DB), 数据库管理系统(DBMS)(及其开发工具), 数据库应用系统, 数据库管理人员(DBA)组成

### 数据库(DB)

`数据库`{.idx}
`DB`{.idx}

长期储存在计算机内, 有组织的, 可共享的大量**数据及其联系**的集合

### 数据库管理系统(DBMS)等软件

`数据库管理系统`{.idx}
`DBMS`{.idx}

数据库管理系统(DBMS)
: 位于用户与系统间专门负责数据管理的软件, 用户调用DBMS, **DBMS调用系统**, 是**数据库系统的核心**

#### 数据库管理系统的6大功能

1. 数据定义功能: 数据定义语言(DDL) `数据定义语言`{.idx} `DDL`{.idx}

    数据定义语言(DDL)主要定义数据库的逻辑结构, 包括定义基本表, 索引和视图三个部分

1. 数据组织, 存储和管理
1. 数据操控功能: 数据操控语言(DML), **实现数据的增删改查** `数据操控语言`{.idx} `DML`{.idx}

    数据操纵语言(DML)包括数据查询和数据更新两大类操作, 其中数据更新又包括插入, 删除和修改三种操作

1. 数据库的运行管理和事务管理: 数据控制语言(DCL) `数据控制语言`{.idx} `DCL`{.idx}

    数据控制语言(DCL)主要有对基本表和视图的授权, 事务控制语句等

1. 数据库的建立和维护功能

### 数据库管理员(DBA)

数据库系统中的人员主要有: **数据库管理员**(最重要), 系统分析员各数据库设计人员, 应用程序员, 最终用户

`数据库管理员`{.idx}
`DBA`{.idx}

#### 数据库管理员职责

1. 决定数据库中的信息内容和结构
1. 决定数据库的存储结构和存取策略
1. 定义数据的安全性要求和完整性约束条件
1. 监视数据库的使用和运行
1. 数据库的改进和重组

## 数据库的体系结构

### 三级模式结构

三级模式是对数据的三个抽象级别, 它把数据的具体组织留给DBMS管理, 使用户能逻辑地抽象地处理数据, 而不必关心数据在计算机中的具体表示方式和存储方式, 不必考虑存取路径等细节. 另外, 外模式是数据库安全性的一个有力措施, 模式实现了数据的共享, 减少了数据的冗余

1. 外模式

    **用户使用的数据视图的描述**, 是与某一具体应用有关的数据的逻辑表示. 显然, 外模式是模式的子集, 且可以有多个

1. 模式

    **用来描述数据库中全体数据的逻辑结构及特征**, 是全体用户数据的最小并集. 数据库模式以某一种数据模型为基础, 综合考虑了所有用户的需求, 并将这些需求有机地结合成一个逻辑整体. 一个数据库只有一个模式

1. 内模式

    **数据库中数据的物理结构和存储方法的描述**, 是数据在数据库内部的表示方式. 内模式负责定义所有数据的物理存储策略和访问控制方法. 一个数据库只有一个内模式. 

### 二级映像和二级独立性

二级映像保证了数据库系统中的数据具有较高的逻辑独立性和物理独立性

1. 外模式/模式映像, 逻辑独立性

    当模式改变时, 可由数据库管理员改变外模式/模式映像, 使得每个外模式保持不变, 而应用程序是根据外模式编写的, 从而不必修改应用程序

1. 模式/内模式映像, 物理独立性, 数据库系统中**唯一**

    指当内模式改变时, 可由数据库管理员改变模式/内模式映像, 使得模式保持不变(外模式当然也不变), 从而不必修改应用程序
