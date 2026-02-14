## 数据库系统学习笔记
##### 本篇笔记参考了 Zhang-Each 学长的笔记
- [学长笔记链接](https://github.com/Zhang-Each/CourseNoteOfZJUSE/tree/master/DBS%E6%95%B0%E6%8D%AE%E5%BA%93%E7%B3%BB%E7%BB%9F)

### 基本概念和关系代数

#### 1.1 Relational Database 关系型数据库
- 关系型数据库是一些系列表的集合
- 一张表是一个基本单位
- 表的一行代表一条关系

#### 1.2 基本概念和结构
- a **relation r** is a subset of $D_1 \times D_2 \times ... \times D_n$
- relation 关系: 指的是一张表
  - relation is a set of tuples 关系是元组的集合
- tuple 元组: 指的是表的一行
- attribute 属性: 指的是表的列
  - attribute type
  - attribute value: 必须(?)是不可分割的(**atomic**) 
  - domain 域: 属性允许取值的集合
- relation schema 关系模式
  - $R = (A_1, A_2, ...,A_n)$ 
  - 其中，$R$指代的是一种关系模式， $A_i$是一系列属性，关系模式是对关系的一种**抽象**
  - $r(R)$ 表示关系模式R中的一种关系， table 指代的也是关系
  - 举个例子,下面是一个关系模式R

$$
\text{Relation Schema: } Student(\underline{ID}, Name, Dept\_Name, Salary)
$$

  - 这是一个关系r,一般画成一张表table,横行代表一个r的一个元素,也就是一个元组tuple
  
  - | ID | Name | Dept_Name |
    | :--- | :--- | :--- |
    | 10101 | Srinivasan | Comp. Sci. |
    | 12121 | Wu | Finance |
    | 15151 | Mozart | Music |
    | 22222 | Einstein | Physics |

  - null value 空值: 一个特殊的值，表示一个值未知或不存在
  - 在访问和更新数据库时会带来许多麻烦，应当尽量避免使用

#### 1.3 Keys 键
- superkey 超键: 一个属性的集合，将这些属性组合在一起可以允许我们唯一标识关系中的元组
- candidate key 候选键: K是R的超键，而K的任意真子集都不是超键，这样的K成为候选键
- primary key 主键: 被设计者选出来作为区分不同元组的候选键，不能是null value
- 在上面的例子里，我们已经用下划线标出了主键(一个attribute用作primary key)
$$
\text{Relation Schema: } Student(\underline{ID}, Name, Dept\_Name, Salary)
$$
- 类似的还有(两个attribute用作primary key)
$$
\text{Relation Schema: } classroom(\underline{building},\underline{room \_ number},capacity)
$$
- referecing relation & referenced realtion 引用与被引用关系
  - forign key 外键: 用来描述两个表的关系
  - 如果关系模式$R_1$中的一个属性是另一个关系模式$R_2$中的一个主键，那么这个属性就是$R_1$的一个外键
  - a foreign key from $r_1$ referencing $r_2$

#### 1.4 关系代数

- Select 选择：$\sigma_{p}(r)=\{t|t\in r \wedge p(t) \}$ 
  - 筛选出所有满足条件p(t)的元素t
- Project投影：$\prod_{A_1,A_2,\cdots,A_k}(r)$
  - 运算的结果是原来的关系r中各列只保留属性$A_1,A_2,\dots,A_k$ 后的关系
  - 会**自动去掉重复**的元素，因为关系是元组的**集合**(不可以重复)
- Union 并操作：$r \cup s=\{t|t\in r \vee t \in s\}$  
  - 两个关系的属性个数必须相同 
  - 各属性的domain必须是可以比较大小的
- Set difference 差操作：$r-s=\{t| t\in r \wedge t \notin s\}$ 
- Cartesian-Product笛卡尔积：$r\times s=\{tq| t\in r\wedge q\in s\}$ 
  - 两个关系必须是不相交的，如果相交则需要对结果中重复的属性名进行重命名
  - 笛卡儿积运算的结果关系中元组的个数应该是rs的个数之乘积
- Renaming重命名：$\rho_{X}(E)$ 
  - 将E重命名为x, 让一个关系拥有多个别名，同时X可以写为$X(A_1,A_2,\dots,A_n)$ 表示对属性也进行重命名
  - 类似于C++中的引用
- 扩展运算: 可以用前面的六种基本运算得到
  - Intersection 交运算$r \cap s=\{t|t\in r \wedge t \in s\}=r-(r-s)$   
  - Natual-Join 自然连接：$r\Join s$ 
    - 两个关系中同名属性在自然连接的时候当作**同一个属性**来处理
    - **Theta join** 满足某种条件的合并：$r\Join_{\theta} s=\sigma_{\theta}(r\Join s)$  
  - Outer-Join外部连接，分为左外连接，右外连接，全外连接
    - 用于应对一些**信息缺失**的情况(有null值)
    - 左外连接$\ltimes $ 
      - 左边的表取全部值按照关系和右边连接，右边不存在时为空值 
    - 右外连接$\rtimes $ 
      - 右边的表取全部值按照关系和右边连接，不存在为空值
    - Full join左右全上，不存在对应的就写成空值
  - Division除法：$r\div s=\{t|t\in\prod_{R-S}(r)\wedge \forall u \in s (tu\in r)\}$
    - 如果$R=(A_1,A_2,\dots,A_m,B_1,\dots,B_n)\wedge S=(B_1,\dots,B_n)$ 则有$R- S=(A_1,A_2,\dots,A_m)$ 
  - Assignment 声明：类似于变量命名用$\leftarrow$  可以把一个关系代数操作进行命名 
- Aggregation operations聚合操作
  - 基本形式：$_{G_1,G_2,\dots,G_n}{\mathcal{G}}_{F_1(A_1),\dots,F_n(A_n)}(E)$
  - G是聚合的标准，对于关系中所有G值相同的元素进行聚合，F( )是聚合的运算函数
  - 常见的有SUM/MAX/MIN/AVG/COUNT

### SQL语言

#### 2.1 SQL基本概念
- SQL:结构化查询语言，分为DQL(查询)，DDL(定义)，DML(操作)，DCL(控制)几种类型，用的最多的是SQL-92
- 非过程式语言
- 四大核心功能(**CRUD**): “增删查改”四大件
  - C Create 创建
  - R Read 查询
  - U Update 更新
  - D Delete 删除

#### 2.2 SQL 表的创建，更新，删除
- SQL 支持的数据类型有：
  - char(n);  varchar(n)
    - 前者字符串长度固定为n，后者字符串长度**上限**为n
  - int; smallint; numeric(p,d); real ; double precision; float(n)
    - 前两个字面意思
    - `numeric(p,d)`中p是小数点前的位数，d是小数点后的位数
    - `real` 是单精度浮点数，`double precison` 是双精度浮点数
    - `float(n)`是精度至少为n位的浮点数
  - date; time; time stamp
    - 三种分别是
    - 年-月-日
    - 时-分-秒
    - 年-月-日-时-分-秒
  - boolean
    - 三种: true false unknown
  - 所有属性支持null value 作为属性值，在声明属性时可以限定其值为not null
- create 创建
  - create table的通用格式
```sql
create table  r (
  A1  D1,
  A2  D2,
  A3  D3,
  <integrity_constraint_1>,
  <integrity_constraint_2>,
  <integrity_constraint_3>
);
/*
 * A 代表 Attribute 属性
 * D 代表 Domain 域
 * integrity_constraint 
 * 意思是 完整性约束
 * 例如， primary key之类
 */
```
- 例子
```sql
create table section (...);
create table instructor (...);
create table teaches (
  ID          varchar(5)    NOT NULL;
  course_id   varchar(5)    NOT NULL;
  sec_id      varchar(5)    NOT NULL;
  semester    varchar(6)    NOT NULL;
  year        numeric(4,0)  NOT NULL;
  primary key (ID, course_id, sec_id, semester, year),
  foreign key (course_id, sec_id, semester,year) references section,
  foreign key (ID) references instructor
);
```
- SQL会禁止破坏完整性约束的任何数据库的更新，条件如下：
  1. 主键出现 null value
  2. 更新时出现与已有主键相同的元组
- 对table声明修改的命令
  - 删除关系
    - `drop r` 删除整改关系，包括关系模式
    - `delete from r` 删除关系内所有的元组，但保留了关系模式
  - 修改属性声明 
    - `alter table r add A D` 向表r中添加 属性A 类型D 的一列变量，初始化是全部为null
    - `alter talbe r drop A`  从表r中删除 属性A

#### 2.3 SQL 查询
- 最重要的，考试也是最常考
- 查询的基本形式是`select`语句
- SQL select 通用格式
```sql
  SELECT  A1, A2,...,Ak
  FROM    r1,r2,...,rm
  WHERE   P;
```
  - 上述查询等价于$\prod_{A_1,A_2,\cdots,A_k}(\sigma_{p}(r_1\times r_2\times \dots\times r_m))$ 
  - 查询的结果是一个关系
  - 查询的结果会**有重复**，因为实践中去除重复是费时的
- SELECT 部分
  - 强行去除重复 请写`SELECT DISTINCT`
  - 防止重复丢失 请写`SELECT ALL`(默认行为)
  - `SELECT`字句支持基本四则运算，比如·
  ```sql
  SELECT  ID, name, dept_name, salary*2
  FROM    insturctor;
  ```
- FROM 部分
  - 重命名操作: 可以通过 `old_name AS new_name` 进行重命名
  - `FROM` 可以选择多个表，此时会将这些表进行笛卡尔积运算，然后再 `SELECT`
  - 元组变量: 可以从多个表中select满足一定条件的几个不同属性的元组
  ```sql
  SELECT  DISTINCT T.name
  FROM    instructor AS T,
          instructor AS S
  WHERE   T.salary > S.salary AND
          S.dept_name = 'Biology';
  ```
  - 字符串部分支持正则表达式,使用关键字 `LIKE`,后续的正则表达式用 `''` 包起来
  ```sql
  SELECT name
  FROM   teacher
  WHERE  name LIKE '%hihci%'; -- 意思是任何含有"hihci"片段的字符串，%是省略
  ```

  |符号|描述|示例|匹配结果|
  |----|---|----|--------|
  |.|匹配除换行符外的任意单个字符|'b.g'|"big, bag, bug"|
  |^|匹配字符串的开始位置|'^A'|"以 ""A"" 开头的字符串"|
  |$|匹配字符串的结束位置|'z$'|"以 ""z"" 结尾的字符串"|
  |*|匹配前面的元素 0 次或多次|'ab*'|"a, ab, abbb"|
  |+|匹配前面的元素 1 次或多次|'ab+'|"ab, abbb（不匹配 a）"|
  |?|匹配前面的元素 0 次或 1 次|colou?r'|"color, colour"|
  |[abc]|匹配方括号中的任意一个字符|'[Vv]ip'|"Vip, vip"|
  |[^abc]|排除方括号中的字符|'[^0-9]'|任何非数字字符|
  |`\|`|逻辑“或”（OR）|'Huawei\|Apple'|Apple|
  |{n}|精确匹配 n 次|'\d{3}'|连续的 3 个数字|

    - 提供一个正则表达式的教程[RUNOOB](https://www.runoob.com/regexp/regexp-tutorial.html)
  - 输出结果排序 使用 `ORDER BY` 命令
    - 升序 asc; 降序 desc (默认升序)
  ```sql
  SELECT    *
  FROM      instructor
  WHERE     dept_name = 'Physics'
  ORDER BY  salary desc, 
            name asc;
  ```
- WHERE 部分
  - 支持逻辑运算 `AND` `OR` `NOT` ...
  - `BETWEEN A AND B` 等价于 `x >= A AND x <= B`
  - `NOT BETWEEN A AND B` 等价于 `x < A AND x > B`
  - 行构造器 row constructor
    - `A <= B AND C <= D` 等价于 `(A,B) <= (C,D)` 
- 集合操作
  - 在关系上使用 `union`,`intersect`和`except` 运算
  - `all` 关键字用于保留重复项
  ```sql
  (SELECT   course_id
   FROM     section
   WHERE    semester = 'Fall' AND
            year = 2017)
  INTERSECT ALL
  (SELECT   course_id
   FROM     section
   WHERE    semester = 'Spring' AND
            year = 2018);
  ```
- 聚合操作
  - 五个标准聚合函数:
    - AVG; MIN; MAX; SUM; COUNT
   ```sql
  SELECT AVG(salary) AS avg_salary
  FROM   instructor
  WHERE  dept_name = 'CS'
  ```
  - 分组聚合
    - 使用 `GROUP BY` 命令
    ```sql
    SELECT   dept_name,COUNT(DISTINCT instructor.ID) AS instr_count
    FROM     instructor, teaches
    WHERE    instructor.ID = teaches.ID AND
             semester      = 'Spring'   AND
             year          = 2018
    GROUP BY dept_name;
    ```
  - having 字句
    - 用于给分组加限定条件
    ```sql
    SELECT   AVG(salary) AS avg_salary
    FROM     instructor
    WHERE    dept_name = 'CS'
    GROUP BY semester
    having   AVG(salary) > 3000;
    ```  
- null value 空值
  - 空值的存在给运算带来了问题
  - 涉及空值的**算数表达式**结果均为**空值**
  - 涉及空值的**比较运算**结果均为**未知(unkown)**
    - 这就是第三种布尔值的由来
  - 涉及空值的**逻辑表达式**
    - 记住一个规则: `unkown` 介于 `true` 和 `false` 之间
    - 举个 :chestnut: : `true AND unknown`
      - AND 运算取更弱的那个，因此输出为 `unkown`
- nested subquery 嵌套查询
  - 回看查询范式
  ```sql
  SELECT  A1, A2,...,Ak
  FROM    r1,r2,...,rm
  WHERE   P;
  ```
    - 我们指出，在 A,r,P 处均可嵌入查询
  - WHERE 处的嵌套查询
    - 成员资格测试: 关键字 `in` 
      - 测试元组在关系中的成员资格，返回布尔值
      - `<>` 意思是"不等于",在SQL中`!=`是非正式写法
      - 可以和其他关键词结合产生不同的效果(也可以是其他逻辑符号)
        - some : 存在性问题
        - all  : 任意性问题
    - 子查询存在性测试: 关键字 `exists` 
      - 判断子查询是否非空,返回布尔值
    - 重复元组存在性测试: 关键字 `unique`
      - 测试元组中是否存在不多于一份的元组
  - FROM 处的嵌套查询
    - 关键字 `lateral` ,支持横向子查询
  - with 字句
    - 临时定义一个子查询，在后一个查询可以调用
    - 例子(with字句后接多条查询注意用`,`隔开)
    ```sql
    WITH   dept_total (dept_name,value) AS(
           SELECT   dept_name,SUM(salary)
           FROM     instructor
           GROUP BY dept_name),
           dept_total_avg(value) AS(
           SELECT AVG(value)
           FROM   dept_total)
    SELECT dept_name
    FROM   dept_total, dept_total_avg
    WHERE  dept_total.value > dept_total_avg.value;         
    ```
  - scalar subquery 标量子查询
    - 需要用到查询结果的值时使用
  - join 字句
    - 用来连接关系，分为内连接和外连接;自然连接和条件连接
    - 自然连接 `natural` 找到所有同名的属性然后连接
      - 内连接 `natural join` 
      - 自动连接所有相同值的属性
      - 外连接 `natural full/left/right outer join`
      - 补全只有单侧有，但没有相同值的情况，
    - 条件连接  在特定条件下连接，更**灵活**
      - 指定属性 `using (ATTRIBUTE)`
      - 指定谓词 `on P`
#### 2.4 SQL数据库的修改
- 删除

    ```sql
    DELETE FROM r
    WHERE       P;
    ```
    - 需要注意，该语句一次只能从一个关系中删除元组，删除多个关系中的元组必须使用多个DELETE才可以实现
    - `WHERE TRUE` 最后的结果是删掉所有的元组，但是保留了关系

    ```sql
    DELETE FROM instructor
    WHERE       dept_name IN (SELECT dept_name
                              FROM   department
                              WHERE  building = 'Waston');          
    ```

- 插入

    ```sql
    -- 第一种
    INSERT INTO r(A_1, A_2, ...,A_n)
            VALUES(D_1, D_2, ...,D_n);
    /*
      * r 后面的属性列表可以省略
      * 但是后面的数据就要和默认属性顺序一致
    */

    --第二种
    INSERT INTO r_1
            SELECT (A_1, A_2, ...,A_n)
            FROM   r_2
            WHERE  P;
    /*
      * 适用于在查询结果的基础上向关系插入元组
    */         
    ```

- 更新

    ```sql
    -- 第一种
    UPDATE  r
    SET     A = VALUE
    WHERE   Predicate;

    --第二种
    UPDATE r
    SET A = case
                WHEN pred_1 THEN result_1
                WHEN pred_2 THEN result_2
                ...
                WHEN pred_n THEN result_n
                ELSE reult_0
            END;
    /*
      * 适用多重分支
    */         
    ```

#### 2.5 SQL 视图&索引
- view 视图
  - 视图概念上包含查询的结果，但只在执行查询时才进行计算和存储
  - 格式：
  ```sql
  CREATE VIEW v AS 
  <Query Expression>;
  ```
  - 例子：
  ```sql
  CREATE VIEW department_total_salary(dept_name, total_salary) AS
    SELECT    dept_name,sum(salary)
    FROM      instructor
    GROUP BY  dept_name;
  ```
- 视图更新
  - 使用`insert`关键字对视图进行更新
  - 然而，这一操作会导致很多问题，因此更新是**有条件的**
  - 条件：
    - FROM 字句后只有一条关系
    - SELECT 子句中只包含属性名，不包含：表达式，聚集，DISTINCT声明
    - SELECT 字句中未出现的属性都可以取null value
    - 查询中不可以有 having 和 group by 字句
  - `WITH CHECK OPTION`可放在创建视图的末尾
    - 保证插入能满足WHERE字句要求，否则拒绝插入请求
- 用户自定义类型 & 自定义域
  - 用户自定义数据类型分为两种
    - distinct type 独特类型
    - structured data type 结构化数据类型
    - 这里，我们讲第一种
  - 用户自定义数据
    - `CREATE TYPE` 字句
    ```sql
    CREATE TYPE Dollars AS numeric(12,2) FINAL;
    ```
      - 这种实现不能添加完整性约束，这是一个缺点
    - `CREATE DOMAIN` 字句
    ```sql
    CREATE Degree_level AS varchar(10)
      CONSTRAINT Degree_level_test
        CHECK (VALUE IN ('Bachelors','Masters','Doctorate'));
    ```
    - 由上可见，自定义域可以灵活的添加完整性约束
    - 然而，应当指出自定义域并不是自定义类型的加强版
    - 首先，创建新类型本质是给已知数据套了一个壳，两个不一样的壳的数据无法比较（除非强制转换类型）
    - 其次，创建新的域是给已知数据加一个名字，只要数据相容两个域可以进行赋值或比较
    - Large-Object Types 大对象类型，分为blob(二进制大对象)和clob(文本大对象)两种，当查询需要返回大对象类型的时候，返回的是一个指向大对象的**指针**
- Index 索引
  - 冗余但高效
  - 格式：
  ```sql
  CREATE INDEX index_name
  ON table_name (column1, column2, ...);
  ```
  - 撤销索引
  - `DROP INDEX index_name`
- Transactions 事务
  - 一系列操作的集合
  - atomic tansaction 原子事务
    - 只能杯完全执行或者回滚(roll back)

#### 2.6 完整性约束
- 单个关系的约束
  - primary key; not null; unique
  - check
    - 一般
    ```sql
    CHECK (P)
    ```
    - Domain check
    ```SQL
    CREATE DOMAIN domain_name
    CONSTRAINTS check_name CHECK(P)
    ```
  - Reference integrity 引用完整性
    - 使用`FOREIGN KEY`字句
    - 此时，如果缺省被引用表的属性值，默认是被引用表的主键属性
    - 这种缺省某些系统**不支持**，尤其是MySQL
  - Cascading action 级联操作
    - 定义：子关系引用父关系中的属性
    - 问题：在父属性的被引用属性发生变化时，子表应当同时改变防止产生脏数据(dirty data)
    - 解决办法：当**引用关系**上的删除或更新违反了约束，系统可以通过改变引用关系中的元组来恢复完整性约束
    - on delete cascade 级联删除
    - on update cascade 级联更新
    - 可以有外码依赖链
    ```sql
    CREATE TABLE course (
        FOREIGN KEY dept_name REFERENCES department
            ON DELETE CASCADE
            ON UPDATE CASCADE,
    );
    ```
- 对整个数据库的约束
  - Assertions 断言
    - 对**整个数据库**任何一个元组发生变动之前都要检查一次断言
    - 与`CHECK`级别不同，`CHECK`仅针对单个关系
    ```sql
    CREATE ASSERTION credits_earned_constraint CHECK (
        NOT EXISTS (SELECT ID
                    FROM   student
                    WHERE  tot_credit <> (SELECT COALESCE (sum(credits),0)
                                          FROM   taks NATURAL JOIN course
                                          WHERE  student.ID = takes.ID
                                              AND grade is NOT NULL 
                                              AND grade <> 'F')))
    -- COALESCE 函数 可以将空值返回为一个设定的非空参数
    ``` 
    - 断言实际上使用场景复杂，开销巨大
    - 也并没有被广泛使用的数据库系统，要么支持在`CHECK`字句嵌入子查询，要么支持`CREATE ASSERTION`结构
    - 然而，如果数据库系统支持触发器，可以用触发器实现同等效果
  - TRIGGER 触发器
    - 触发器有两个时间节点可供选择：BeforeTrigger和AfterTrigger
    - 一般来说，前者用于删除，后者用于插入，更新两者都可以
    - 语法:
    ```sql
    CREATE TRIGGER trigger_name BEFORE/AFTER trigger_event OF table_name ON attribute --或者 ON table_name 也是可以的
        REFERNCING NEW/OLD row AS XXX --创建一个过渡变量，是一个过渡表
        FOR EACH ROW -- 行级触发，一个事件影响的所有行数都要检查
        WHEN XXX --执行命令的条件
        BEGIN -- BEGIN ATOMIC 如果有多条SQL语句汇集成单条复合语句
        XXX --执行命令
        END
    -- 可能会用到roll back
    ```
#### 2.7 Authorization 授权
- 四种权限：read; insert; update; delete 
- Security specification in SQL
  - grant 授予权限
    ```sql
    GRANT <privilege_list>
    ON    <relation_name or view_name>
    TO    <user_list>;
    ``` 
    - ON 字句可以具体到属性名
    - TO 字句后面可以跟public
    - grant 语句后面可以跟`with grant option`,表明用户同时拥有给其他用户该权限的能力
  - revoke 收回权限
    ```sql
    REVOKE  <privilege_list>
    ON      <relation_name or view_name>
    FROM    <user_list> RESTRICT/CASCADE --后者可缺省      
    ```
  - role 角色
    - `CREATE ROLE role_name`
    - 一个用户（角色）拥有的所有全校包括：
    - 直接授予该用户（角色）的所有权限
    - 授予该用户（角色）所拥有角色的所有权限

### E-R模型和范式
#### 3.1 E-R模型
- E-R模型由 entity 和 relationship 组成
- Entity set 实体集
  - 实体是用属性来描述
  - 同一类实体有相同的属性列表，实体集是同类实体组成的集合
  - 用**长方形**表示，属性写在里面，主键加下划线
- Relationship set 关系集
  - 一条relationship代表几个实体之间的联系，关系集市同类关系构成的集合
  - 一个关系集所关联的实体集个数，称为degree(>=2)
- 复杂属性
  - 简单属性和复合属性
  - 单值，多值属性
  - 派生属性
  > Instructor
      >
      > <u>ID</u> 
      >
      > name
      >
      > ​  first_name
      >
      > ​	 last_name
      >
      > address
      >
      > ​  street
      >
      >     street_number
      >
      > ​    street_name
      >
      > ​	   apt_number
      >
      >   city
      >
      > ​	 state
      >
      > {phone_number}
      > 
      > date_of_birth
      >
      > age()
- E-R model Constraints 
  - mapping cardinality 映射基数
    - 二元映射关系中的映射基数只有一对一，一对多，多对一和多对多
    - 在图里面：箭头表示一，直线表示多
  - 参与度约束
    - 在图里面：单线代表部分，双线代表全部
    - 在横线上可以用`A..B`来实现更复杂的约束
    - A是最小值，B是最大值
  - weak entity set 弱实体集
    - 原本的实体集在联系中会产生冗余，删去冗余部分又无法形成独立主键，形成了**依赖外部**的弱实体集
    - 经常出现在**一对多**的关系中，E-R图中用**双线框**表识，其分辨符属性用**虚线下划线**标识
    - 比如说，群聊和群成员是从属关系，群成员不能脱离群聊ID实现唯一标识，群聊必定包含群聊ID，但是两者重复冗余，故删除群成员实体集的群聊ID属性，做成弱实体集
  - Aggregation 聚合
    - 把一个联系集看成一个同名的高层实体集
    - E-R图中是一个将部分联系集和实体集框起来的大矩形框
  - Specialization 特化
    - 是一个**自上而下**的设计思路
    - 根据实体从属关系分为
      - overlappping specialization
      - disjoint specialization
    - E-R图自上往下，最上面是实体集，下面每一层有空心箭头指向上一层
  - Generalization 概化
    - 刚好和 Specialization 相反

#### 3.2 E-R diagram
- 看书/PPT

#### 3.3 Normal Form 范式
- 数据库设计的目标
  - 减少不必要冗余，提升检索效率
  - 设计通过范式来实现
- First Normal Form 第一范式
  - 关系模式R的所有属性都不可再分，该关系模式R是第一范式
  - problem: 信息冗余; 更新数据繁琐; null value 也不好操作
- Decomposition 分解
  - Lossy Decomposition 有损分解，尝试连接后发现原有关系部分缺失
  - Lossless join 无损分解：
    - R被分解为($R_1,R_2$)并且$R=R_1 \bigcup R_2$
    - 对于任何关系模式R上的关系r有$r=\prod_{R_1}(r)\Join\prod_{R_2}(r)$
- 