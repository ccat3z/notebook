# Spark Streaming

根据用户指定的时间间隔进行切割(离散化), 得到的每一小批数据的独立RDD,
DStream维护一系列RDD信息.

## 体系架构

与Spark的区别:

* Driver: StreamingContext extends SparkContext
* Executor: 某些Task将负责从外部不断获取数据流

## 容错机制

* Cluster Manager故障：不考虑
* Executor(Worker)故障
  * 不含Receiver: 利用RDD Lineage进行恢复
  * 含有Receiver: 利用日志进行恢复.
    Reciever将数据存入本地和外部存储, 记录日志, 通知Driver.
    Driver记录元数据日志.
* Driver故障: 利用(元数据)检查点进行恢复

### 端到端的容错语义

* 接收数据: at-least or exactly once

  取决于数据是使用Receiver或其它方式从数据源接收的

* 转换数据: exactly once

  接收到的数据是用Dstream和RDD做转换的

* 输出数据: at-least or exactly once

  取决于最终的转换结果被推出到外部系统如文件系统，数据库，仪表盘等