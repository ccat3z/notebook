<!--
    vi: ft=pandoc.markdown
-->

# 概论

## 电路基本概念

* 电路分类: 模拟电路, 数字电路
* 数字电路分类

    * 输入信号的相应规格: 组合逻辑电路, 时序逻辑电路
    * 器件: TTL, CMOS `TTL`{.idx} `CMOS`{.idx} 
    * 集成度: SSI(小规模), MSI, LSI, VLSI, ULSI `SSI`{.idx} `MSI`{.idx} `LSI`{.idx} `VLSI`{.idx} `ULSI`{.idx}

## 二进制

### 反码, 补码

`反码`{.idx} `补码`{.idx}

原码 | 反码 | 补码
:--: | :--: | :--:
0110 | 0110 | 0110
1110 | 1001 | 1010

### BCD码

二进制编码十进制
    
`BCD`{.idx}

* 有权码
  * 8421码 `BCD!8421`{.idx}
  * 2421 `BCD!2421`{.idx}
  * 5421 `BCD!5421`{.idx}
* 无权码
  * 余3码 (8421码 + 3) `BCD!余3码`{.idx}
  * 余3循环码 (格雷码首尾去除3位) `BCD!余3循环码`{.idx}
  * 格雷码 `BCD!格雷码`{.idx}
    * 8421转BCD: `map (\a prev -> a + prev)`{.haskell} ($1011 \rightarrow 1110$))
    * BCD转8421: `foldl (\acc a -> (acc:(acc[-1] + a)))`{.haskell} ($1101 \rightarrow 1001$)
