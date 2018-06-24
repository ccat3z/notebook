---
# vi: ft=pandoc.markdown
---

# SQL

`SQL`{.idx}

```{.sql}
CREATE DATABASE database_name ON (
    name = database_name, filename = 'file_path',
	size = 5, filegrowth = 2
)

CREATE TABLE table_name (
    column_name_1 INT
        FOREIGN KEY REFERENCES other_table(column)
            /* ON INSERT 不存在, 默认NO ACTION */
            ON DELETE CASCADE /* NO ACTION | SET NULL | SET DEFAULT */
            ON UPDATE NO ACTION,
    column_name_2 SMALLINT UNIQUE,
    column_name_3 DECIMAL(12, 1) CHECK (column_name_3 > 0),
    column_name_4 CHAR(5) NOT NULL PRIMARY KEY,
    column_name_5 VARCHAR(5),

    CONSTRAINT constraint_name_a
        CHECK (column_name_3 > column_name_1 AND ...)
    CONSTRAINT constraint_name_b
        PRIMARY KEY (column_name_1, column_name_2)
)

CREATE INDEX index_name ON table_name(column_1, column_1)

CREATE VIEW view_name /* (column_name, ...) */ AS
SELECT ...

ALTER TABLE table_name ADD column_name DATE NOT NULL
ALTER TABLE table_name DROP COLUMN column_name
ALTER TABLE table_name ALTER COLUMN column_name INT

ALTER TABLE table_name
    ADD CONSTRAINT constraint_name PRIMARY KEY (primary_key, ...)
ALTER TABLE table_name DROP CONSTRAINT constraint_name

DROP TABLE table_name

SELECT /* TOP 1 */ DISTINCT
    column, COUNT(DISTINCT column), SUM(column),
    AVG(column), MAX(column), MIN(column) AS A
FROM table_name, view_name, ... /* 笛卡儿积 */
/* FROM table_name
   [INNER | {LEFT | RIGHT | FULL} [OUTER]] JOIN
   table_name ON ... */
WHERE
    column_1 NOT IN (data, ...)
    AND column_2 LIKE '_A%' /* _ -> ?, % -> * */
    OR column_3 BETWEEN a AND b
    AND column_4 IS NOT NULL
    OR column_5 EXIST /* > {{ANY | SOME} | ALL} */ (SELECT ...)
GROUP BY column_name, ...
HAVING logical_expression
ORDER BY column_name DESC
UNION /* INTERSECT | EXCEPT */
SELECT ...

INSERT INTO table_name VALUES (column_data, ...)
INSERT INTO table_name (column_name_1, ...) VALUES (column_data, ...)

DELETE FROM table_name WHERE logical_expression
UPDATE table_name SET column_name = data WHERE logical_expression
```

## SQL语言的主要特点

1. 综合统一, 即集DDL, DML和DCL功能于一体
2. 面向集合的操作方式, 即操作的对象和操作的结果都是元组的集合
3. 高度非过程化, 即在完成某项查询要求时, 用户无需了解存取路径, 只要提出"做什么", 不必指出"怎么做"
4. 以同一种语法结构提供两种使用方式, 即独立地用于联机交互的使用方式和嵌入到高级语言中这两种不同的使用方式下, 语法结构是基本上一致的
5. 支持三级模式结构
