======================================================================
ORACLE MASTER Bronze 11g SQL 基礎 I 必修教本 読書ノート
======================================================================

近所の図書館のリサイクルワゴンに本書が突っ込まれていたので回収した。内容はきわめ
て初歩的なのだが、データベースを仕事でほとんど使わなかったのでノートをとることに
する。

:著者: 小野寺智子
:出版社: 株式会社アスキー・メディアワークス
:ISBN: 978-4-04-868132-2

.. contents:: ノート目次
   :depth: 3

序章 データベースと SQL
======================================================================

このへんは今はどうでもいい。後で効いてくるものだから。

* DBMS
* データベースモデル

  * 階層型
  * ネットワーク型
  * リレーショナル型

    * 表計算ソフトのスプレッドシートのような二次元の表を使用して情報を格納する。
    * 複数の表の間に何らかの関係を定義する。表の間というより、表に含まれているレ
      コード（本書ではエンティティと呼んでいるが）とレコードの間に関係がある。

* RDBMS

  * Oracle Database は RDBMS の一つ。

* SQL

  * RDB 操作のためのプログラミング言語。
  * Oracle Database 版 SQL は標準仕様とは少々異なる。
  * SQL 文は次の 4 つに分類される（ことが多い）：

    * データ操作言語 DML 文
    * データ定義言語 DDL 文
    * データ制御言語 DCL 文
    * トランザクション制御文

* 1970 年に IBM の E. F. Codd 博士が RDB を考案したとある。当初は理論だけで実装
  はまだなかった。
* 階層型やネットワーク型のデータベースは現在ほとんど存在しない。

第 1 章 基本的なデータ検索
======================================================================

本章では ``SELECT`` 文を学習する。ここは理解に問題はない。例だけを書いてあとで補
足する。

.. code:: plpgsql

   SELECT employee_id, first_name FROM employees;

   SELECT employee_id, first_name, last_name, email,
          phone_number, hire_date, job_id, salary,
          commission_pct, manager_id, department_id FROM employees;

   SELECT * from employees;

   SELECT employee_id, last_name, salary + 500 FROM employees;
   SELECT employee_id, last_name, 12 * salary + 500 FROM employees;
   SELECT employee_id, last_name, 12 * (salary + 500) FROM employees;

   SELECT last_name 500 + salary * 12 yearsal FROM employees;
   SELECT last_name 500 + salary * 12 AS yearsal FROM employees;
   SELECT last_name 500 + salary * 12 "yearsal" FROM employees;

   SELECT employee_id, first_name || last_name FROM employees;
   SELECT employee_id, 'name is ' || last_name FROM employees;

   SELECT q'[It's ]' || last_name FROM employees;

   SELECT DISTINCT department_id FROM employees;

.. warning::

   コードハイライトが Pygments の ``sql`` でうまくいかない。暫定的に ``plpgsql``
   にしておく。欲を言えば Oracle もサポートして欲しい。

* キーワード、表名、列名、関数名、等々、大文字と小文字はまったく区別されない。
* 文末には ``;`` を付けるほうが無難。特に SQL*Plus 環境では実行に要る。
* 型によっては列に対して算術演算 ``+``, ``-``, ``*``, ``/`` を適用できる。
* ``NULL``

  * 未確定の状態を表す特別な値である。
  * 数 0 や空白文字とは異なる。

    * 列の型が文字列ならば空文字列とは同じ概念なのかもしれない。

  * ``NULL`` に対してどのような算術演算を施しても結果は ``NULL`` となる。重要。

* ``SELECT`` 文の列見出しは通常大文字で表示される。小文字がよければ ``"`` で囲
  む。
* 演算子 ``||`` は文字列の連結を行う。こちらは ``NULL`` を空文字列として処理す
  る。
* 演算子 ``q`` は C++11 の ``R`` 文字列に似ている。
* 選択結果から重複データを除外して表示するのに ``DISTINCT`` を用いる。
* ``DESCRIBE`` コマンドは表の定義を出力するものだが、Oracle Database 独自のもの
  だ。

第 2 章 データ検索における制限とソート
======================================================================

言い忘れたが SQL 文の出力はここには書かない。

.. code:: plpgsql

   -- それぞれ数値、文字列、日付を検索条件にする
   SELECT employee_id, last_name, department_id FROM employees
       WHERE department_id = 50;
   SELECT employee_id, last_name, department_id FROM employees
       WHERE last_name = 'Grant';
   SELECT employee_id, last_name, hire_date FROM employees
       WHERE hire_date = '00-JAN-13';

   -- 比較演算子
   SELECT employee_id, last_name, department_id FROM employees
       WHERE department_id > 50;
   SELECT employee_id, last_name, department_id FROM employees
       WHERE department_id >= 50;
   SELECT employee_id, last_name, department_id FROM employees
       WHERE department_id < 50;
   SELECT employee_id, last_name, department_id FROM employees
       WHERE department_id <= 50;
   SELECT employee_id, last_name, department_id FROM employees
       WHERE department_id <> 50;

   -- BETWEEN x AND y の例
   SELECT employee_id, last_name, department_id FROM employees
       WHERE department_id BETWEEN 50 AND 90;

   -- IN 演算子の例
   SELECT employee_id, last_name, department_id FROM employees
       WHERE department_id IN (40, 60, 80);

   -- ワイルドカードの例
   SELECT employee_id, last_name FROM employees
       WHERE last_name LIKE 'A%';
   SELECT employee_id, last_name, jpb_id FROM employees
       WHERE job_id LIKE 'SA\_%' ESCAPE '\';

   -- NULL をテストする例
   SELECT employee_id, last_name, manager_id FROM employees
       WHERE manager_id IS NULL;

   -- AND, OR, NOT の例
   SELECT employee_id, last_name, salary, department_id FROM employees
       WHERE salary >= 2500
           AND department_id = 50;
   SELECT employee_id, last_name, salary, department_id FROM employees
       WHERE salary >= 2500
           OR department_id = 50;
   SELECT employee_id, last_name, salary, department_id FROM employees
       WHERE department_id NOT IN (50, 80);

* ``WHERE`` 句を付すことで検索条件を定義する。両辺が等しいかどうかは比較演算子の
  一つ ``=`` を用いる。
* 条件式に関しては大文字と小文字は区別される。
* 日付の指定は書式がどうなっているのかを把握する必要があるのでミスが多いのでは？

    * デフォルトの日付書式は `DD-MON-RR`
    * 日付については後述

* 二項比較演算子は常識的なものが使える。not equal は ``<>``, ``!=`` の他に
  ``^=`` というものがある。
* ``BETWEEN ... AND ...`` と ``IN (...)`` という構文もある。
* 文字列条件の指定にはワイルドカードが存在する。

  * ``%``: 任意の文字 0 文字以上
  * ``_``: 任意の 1 文字

* ワイルドカードをリテラルに指定したい場合には他のプログラミング言語のようにエス
  ケープをするわけだが、キーワード ``ESCAPE`` を用いてエスケープ文字を明示する必
  要がある。
* 列が ``NULL`` かどうかは ``IS NULL``, ``IS NOT NULL`` を用いる。
* 論理演算子 ``AND``, ``OR``, ``NOT`` を条件式に使える。
* 演算子の優先順位は次のように憶える:

  * 比較演算子のほうが論理演算子より高い
  * 論理演算子では ``NOT``, ``AND``, ``OR`` の順に高い

* 演算の優先度を調節するときは、他のプログラミング言語のように丸括弧を用いる。

ソート
----------------------------------------------------------------------

.. code:: plpgsql

   SELECT employee_id, last_name, department_id FROM employees
       ORDER BY department_id;
   SELECT employee_id, last_name, department_id FROM employees
       ORDER BY department_id DESC;
   SELECT employee_id, last_name, department_id FROM employees
       ORDER BY department_id, last_name DESC;
   SELECT employee_id, last_name, salary + commission_pct annsal FROM employees
       ORDER BY annsal;
   SELECT employee_id, last_name, department_id FROM employees
       ORDER BY department_id NULLS FIRST;

* ``ORDER BY`` 句はレコードをソートして出力する。``ORDER BY`` 句のオプションとし
  て次のものがある：

  * ``ASC``: 行を昇順にソートする。デフォルト。
  * ``DESC``: 行を降順にソートする。
  * ``NULLS FIRST`` : ``NULL`` が存在する場合には先頭に出力する。
  * ``NULLS LAST``: ``NULL`` が存在する場合には末尾に出力する。

* 順序の定義は数、文字列、日付それぞれで自然に考える。

あとはプレースホルダー機能のようなものが SQL*Plus にあることが紹介されている。

第 3 章 単一行関数
======================================================================

Oracle Database で使用する SQL 関数のほとんどが本製品固有のものだ。したがって
SQL Server なと他社製品では使用できない。

つぶしが効かないとわかっているので、ここに時間を割かない。

.. code:: plpgsql

   SELECT LOWER(last_name) FROM employees;
   SELECT last_name FROM employees
       WHERE LOWER(last_name) = 'abel';
   SELECT CONCAT('a', 'b') FROM dual;
   SELECT SUBSTR('ORACLE', 4, 3) FROM dual;
   SELECT LENGTH('ORACLE') FROM dual;
   SELECT LPAD('ORACLE', 10, '#') FROM dual;
   SELECT RPAD('ORACLE', 10, '#') FROM dual;
   SELECT REPLACE('ORACLE', 'O', 'MI') FROM dual;
   SELECT REPLACE('ORACLE', 'O') FROM dual;
   SELECT ROUND(98.765, 1) FROM dual;
   SELECT ROUND(98.765) FROM dual;
   SELECT ROUND(98.765, -1) FROM dual;
   SELECT TRUNC(98.765, 1) FROM dual;
   SELECT TRUNC(98.765) FROM dual;
   SELECT TRUNC(98.765, -1) FROM dual;

* ``dual`` はダミー表。
* 関数 ``LENGTH`` については ``LENGTHB`` も併せて取得すること。
* 関数 ``TRIM`` は癖が強すぎるのであえて憶えない。
* 関数 ``ROUND``, ``TRUNC`` は第二引数に注意。小数点の左、つまり桁が大きくなるほ
  うに行くのが負。

.. code:: plpgsql

   SELECT SYSDATE FROM dual;
   SELECT MONTHS_BETWEEN('15-AUG-09', '15-MAY-09') FROM dual;
   SELECT MONTHS_BETWEEN('15-MAY-09', '15-AUG-09') FROM dual;
   SELECT ADD_MONTHS('15-AUG-09', 5) FROM dual;
   SELECT ADD_MONTHS('15-AUG-09', -3) FROM dual;
   SELECT NEXT_DAY('15-AUG-09', 'FRI') FROM dual;
   SELECT NEXT_DAY('15-AUG-09', 6) FROM dual;
   SELECT LAST_DAY('15-AUG-09') FROM dual;
   SELECT ROUND(SYSDATE, 'MONTH') FROM dual;
   SELECT TRUNC(SYSDATE, 'MONTH') FROM dual;

日付操作が豊富。

第 4 章 変換関数と条件式の使用方法
======================================================================

データの型変換は代入演算と比較演算で発生しうる。

型変換には暗黙的なものと明示的なものに分類できる。暗黙的なものは文字列型系
(``VARCHAR2``, ``CHAR``) を数値型系 (``NUMBER``, ``DATE``) に、またはその反対に
数値型系から文字列型系に変換したりする。

明示的な変換は関数を呼び出すことで行う。

.. code:: plpgsql

   SELECT TO_CHAR(SYSDATE, 'yyyy-mm-dd hh24:mi:ss') today FROM dual;
   SELECT TO_CHAR(123456, '999,999') counts FROM dual;

``TO_DATE`` と ``TO_NUMBER`` の例文がない。

.. code:: plpgsql

   SELECT last_name NVL(commission_pct, 0) comm_pct FROM employees;
   SELECT last_name NVL2(commission_pct, 'Sales', 'No Sales') comm_pct FROM employees;
   SELECT first_name, last_name, NULLIF(first_name, last_name) FROM employees;
   SELECT last_name, COALESCE(commission_pct, salary, 0) FROM employees;

   SELECT last_name, job_id, salary,
   CASE
       WHEN salary BETWEEN 2500 AND 5000 THEN 'Grade C'
       WHEN salary BETWEEN 5001 AND 10000 THEN 'Grade B'
       ...
       ELSE 'No grade'
   END "Sal_Grade"
   FROM employees;

* 関数 ``NULLIF`` は二引数が等しければ ``NULL`` を返すという妙なものに見えるが、
  これを用いて条件分岐をすることができる。
* 関数 ``COALESCE`` は最初の非 ``NULL`` 要素を返す。Oracle 固有。
* 関数 ``CASE`` の劣化版として ``DECODE`` という Oracle 固有のものがある。

第 5 章 グループ関数
======================================================================

グループ関数は表内のレコードを何らかの基準でグループ化したのち、何らかの集計を行
う関数だ。したがって、入力が複数で出力が一つだ。

集計関数は値が ``NULL`` であるものを無視する。ただし ``COUNT(*)`` は ``NULL`` を
含むものも拾い上げる。そもそも ``COUNT(*)`` は使うべきではない。

.. code:: plpgsql

   SELECT AVG(salary), SUM(salary), MIN(salary), MAX(salary), COUNT(salary)
       FROM employees;
   SELECT MAX(first_name), MIN(first_name), COUNT(first_name) FROM employees;

``GROUP BY`` に対する集計
----------------------------------------------------------------------

次にグループを定義してから集計する方法を記す。``GROUP BY`` 句で列名を指定するこ
とでそうなる。

.. code:: plpgsql

   SELECT department_id, AVG(salary) FROM employees
       GROUP BY department_id;
   SELECT job_id, AVG(salary) FROM employees
       GROUP BY job_id;
   SELECT job_id, COUNT(job_id) FROM employees
       GROUP BY job_id;
   SELECT department_id, job_id, COUNT(job_id) FROM employees
       GROUP BY department_id, job_id;

* ``GROUP BY`` 句には ``SELECT`` 句に列挙した（集計以外の）列名をすべて列挙する
  必要がある。気が利かない。
* ``GROUP BY`` 句には列の別名を指定できない。気が利かない。

``HAVING`` 句の用途
----------------------------------------------------------------------

.. code:: plpgsql

   SELECT department_id, AVG(salary) FROM employees
       GROUP BY department_id
       HAVING AVG(salary);
   SELECT department_id, job_id, AVG(salary) FROM employees
       WHERE job_id LIKE 'SA\_%' ESCAPE '\'
       GROUP BY department_id, job_id
       HAVING AVG(salary) >= 3500;
   SELECT department_id, AVG(salary) FROM employees
       GROUP BY department_id
       HAVING COUNT(1) > 10;

* ``HAVING`` 句はグループ関数を問い合わせ条件に指定する。
* ``HAVING`` 句にも列の別名を指定できない。これはわかる。

第 6 章 表の結合
======================================================================

表の定義を示さないと SQL 文の読解ができないのだが、そうしない。

.. code:: plpgsql

   -- 同じデータ型および同じ列名の列同士で表を結合する
   SELECT employee_id, last_name, department_name
       FROM employees
           NATURAL JOIN departments;

   -- 結合する列を限定する
   SELECT employee_id, last_name, department_name
       FROM employees
       JOIN departments
           USING department_id;

   -- ``ON`` 句では列名が異なっていてもよい
   SELECT employee_id, last_name, department_name
       FROM employees emp
       JOIN departments dept
           ON emp.department_id = dept.department_id;

   SELECT employee_id, last_name, department_name, city
       FROM employees emp
       JOIN departments dept
           ON emp.department_id = dept.department_id
       JOIN locations loc
           ON dept.location_id = loc.location_id;

   SELECT e.employee_id emp_id, e.last_name emp_name,
          m.employee_id mgr_id, m.last_name mgr_name
       FROM employees e
       JOIN employees m
           ON e.manager_id = m.manager_id;

``NATURAL JOIN`` は同じデータ型および同じ列名の列同士で表を結合する。本書の例で
は、この二つの表では列 ``manager_id`` と列 ``department_id`` が共通している。

``USING`` 句の文は同じようなことをしているが、結合する列を一つに限定する。

``INNER JOIN`` の ``ON`` 句では列名が異なっていてもよい。

自己結合の場合には表に別名を二つつけて、列がどちらのものなのか表名を明示する必要
がある。

.. code:: plpgsql

   SELECT e.employee_id, e.last_name, e.salary, j.grade_level
       FROM employees e
       JOIN job_grades j
           ON e.salary BETWEEN j.lowest_sal AND j.highest_sal;

``=`` に基づかない結合は非等価結合と呼ばれる。

外部結合
----------------------------------------------------------------------

.. code::plpgsql

   -- d が残る
   SELECT e.employee_id, e.last_name, d.department_name
       FROM employees e RIGHT OUTER JOIN departments d
       ON e.department_id = d.department_id;

   -- e が残る
   SELECT e.employee_id, e.last_name, d.department_name
       FROM employees e LEFT OUTER JOIN departments d
       ON e.department_id = d.department_id;

   -- e も d も残る
   SELECT e.employee_id, e.last_name, d.department_name
       FROM employees e FULL OUTER JOIN departments d
       ON e.department_id = d.department_id;

結合後、条件を満たさないレコードを出力する場合には外部結合を行う。外部結合はどち
らのレコードを出力するのかで三通りに分類される。

* ``JOIN`` 句の右側に置いた表のレコードを残すのならば ``RIGHT OUTER JOIN``
* ``JOIN`` 句の左側に置いた表のレコードを残すのならば ``LEFT OUTER JOIN``
* 両側とも残すならば ``FULL OUTER JOIN`` とする。
* いずれの場合にも結合条件から漏れたレコードは当該列が ``NULL`` として出力され
  る。
* このときの ``RIGHT``, ``LEFT``, ``FULL`` は省略可。

表の直積
----------------------------------------------------------------------

.. code:: plpgsql

   SELECT last_name, department_name
       FROM employees CROSS JOIN departments;

``CROSS JOIN`` 句は表の直積を出力する。

第 7 章 副問い合わせ
======================================================================

副問い合わせは ``WHERE``, ``HAVING``, ``FROM``, ``SET`` 句などに含まれる
``SELECT`` 文のことをいう。

.. code:: plpgsql

   SELECT last_name FROM employees
       WHERE salary > (SELECT AVG(salary) FROM employees);

   SELECT last_name, job_id
       FROM employees
       WHERE job_id IN (
           SELECT job_id FROM employees WHERE last_name = 'King');

   SELECT last_name, job_id, salary, department_id
       FROM employees
       WHERE salary < ANY(
           SELECT salary FROM employees WHERE department_id = 60)
           AND department_id <> 60
       ORDER BY department_id;

   SELECT last_name, job_id, salary, department_id
       FROM employees
       WHERE salary < ALL(
           SELECT salary FROM employees WHERE department_id = 60)
           AND department_id <> 60
       ORDER BY department_id;

   SELECT department_id, MIN(salary)
       FROM employees
       GROUP BY department_id
       HAVING MIN(salary) > (
           SELECT MIN(salary) FROM employees WHERE department_id = 50);

不等号と ``ANY`` または ``ALL`` を使った例は妙な感じがする。``MIN``, ``MAX`` と
比較したらどうだろう。

.. code::plpgsql

   -- 良い副問い合わせ
   SELECT emp.last_name, emp.job_id
       FROM employees emp
       WHERE emp.employee_id IN (
           SELECT mgr.manager_id FROM employees mgr);

   -- 良い副問い合わせ
   SELECT last_name, job_id
       FROM employees
       WHERE employee_id NOT IN (
           SELECT manager_id FROM employees
           WHERE manager_id IS NOT NULL);

副問い合わせでは特に ``NULL`` の取り扱いに注意を要する。そういう問い合わせ結果が
含まれているときには ``IN``, ``ANY``, ``ALL`` を利用すると妙なことになる。

第 8 章 集合演算子
======================================================================

* ``UNION``, ``UNION ALL``, ``INTERSECT``, ``MINUS`` を集合演算子という。
* 集合演算子を使う問い合わせを複合問い合わせという。
* 集合演算子は同じレコードセット型同士にしか作用しない。
* 集合演算では文字型を除いて暗黙の型変換は一切行われない。

  * したがって ``NULL`` を扱うときには変換関数で明示的に型変換を指定する必要があ
    る。

* ``UNION`` と ``UNION ALL`` の違いは C++ でいうと ``std::set`` と
  ``std::multiset`` の違いに相当するだろう。

.. code:: plpgsql

   SELECT employee_id, last_name FROM employees
   UNION
   SELECT employee_id, last_name FROM managers;

   SELECT employee_id, last_name FROM employees
   UNION ALL
   SELECT employee_id, last_name FROM managers
   ORDER BY employee_id;

   SELECT employee_id, last_name FROM employees
   INTERSECT
   SELECT employee_id, last_name FROM managers;

   SELECT employee_id, last_name FROM employees
   MINUS
   SELECT employee_id, last_name FROM managers;

第 9 章 DML 文（データ操作言語）
======================================================================

最初に ``INSERT``, ``UPDATE``, ``DELETE`` 文を習う。その次にトランザクションを習
う。

レコードの追加・更新・削除
----------------------------------------------------------------------

.. code:: plpgsql

   INSERT INTO countries (country_id, country_name, region_id)
       VALUES ('KR', 'Korea', 3);
   INSERT INTO countries
       VALUES ('KR', 'Korea', 3);

   INSERT INTO countries (country_id, region_id)
       VALUES ('MO', 3);
   INSERT INTO countries
       VALUES ('MO', NULL, 3);

   INSERT INTO it_employees
       SELECT employee_id, first_name, last_name, job_id
           FROM employees
           WHERE job_id LIKE 'IT%';

   UPDATE employees
       SET department_id = 120;
       WHERE department_id = 60;

   UPDATE it_employees
       SET last_name = 'Scott';

   UPDATE it_employees
       SET job_id = NULL
       WHERE employee_id = 103;

   UPDATE employees
       SET department_id = (
               SELECT department_id FROM employees WHERE employee_id = 107),
           salary = (
               SELECT MAX(salary) FROM employees WHERE job_id = 'IT_PROG')
       WHERE last_name = 'Scott';

   DELETE FROM it_employees;

   DELETE employees
       WHERE department_id = (
           SELECT department_id
               FROM employees WHERE employee_id = 107)
           AND salary = (
           SELECT MAX(salary)
               FROM employees WHERE job_id = 'IT_PROG');

* ``NULL`` を明示的に挿入・更新することができる
* ``INSERT`` 文によるデータのコピー方法を習得すること
* ``UPDATE`` および ``DELETE`` 文は条件を指定しないと全レコードが処理対象となる。

トランザクション
----------------------------------------------------------------------

トランザクションとは連続する DML 文を一体化したものとしてみなすものだ。

* ``COMMIT`` 文はこれまでのトランザクションを終了することを確定する。データベー
  スの状態が変更される。
* ``ROLLBACK`` 文はこれまでのトランザクションを取り消す。データベースの状態はト
  ランザクション開始直前まで戻る。
* Oracle にはセーブポイントという機能があるが、標準規格ではないので学習しないこ
  とにする。

トランザクションも明示的なものと暗黙的なものがある。上記の ``COMMIT``,
``ROLLBACK`` によるものは明示的だ。暗黙的なものは：

* DDL 文を実行したときに確定
* SQL*Plus などのツールを正常に ``EXIT`` したときに確定
* トランザクション実行中に障害が発生したときにキャンセル
* SQL*Plus などのツールを異常終了したときにキャンセル

読み取り一貫性
----------------------------------------------------------------------

読み取り一貫性とは、あるユーザーがデータを更新中でも、他のユーザーがデータを問い
合わせられる性質だ。あるユーザーのトランザクション開始時の状態を他のユーザーが問
い合わせることになる。

ロック
----------------------------------------------------------------------

ロックとは、同一データの同時更新を防止することだ。ふつうは行単位での暗黙的なロッ
クが有効に機能する。

.. code:: plpgsql

   SELECT employee_id, last_name FROM employees FOR UPDATE;

   UPDATE employees SET employee_id = 1000 WHERE employee_id = 197;

   ...

   COMMIT;

上のように順次実行すると、別のユーザーは ``employees`` テーブルを更新するときに
待たされる。

``FOR UPDATE`` にはオプションとして ``WAIT`` または ``NOWAIT`` を指定してもよい。
他ユーザーの更新をブロックするか即時エラーを戻すかという選択だ。

``TRUNCATE`` 文
----------------------------------------------------------------------

.. code:: plpgsql

   TRUNCATE TABLE it_employees;

``TRUNCATE`` 文は表の全レコードを削除する。表の定義自体は生きている。全削除専用
コマンドなので高速に処理される。ロールバック不可。

第 10 章 DDL 文（データ定義文）
======================================================================

RDB は表だけで構成されているわけではなく、次のような構成要素がある（他にもある）：

* ビュー
* 順序
* 索引
* シノニム

スキーマとは、データベースの構成要素それぞれのオーナーが誰であるのかという概念だ。
Oracle Database はデータベース構成要素を ``schema_name.object_name`` のような形
式で管理している。本文ではそういう言い回しをしていないが、ユーザー名を名前空間と
して扱うようだ。

データ型について説明がある。``CHAR`` と ``VARCHAR2`` の違いは固定長かそうでないか。

表の作成・変更・削除
----------------------------------------------------------------------

.. code:: plpgsql

   CREATE TABLE emp(
       emp_no NUMBER,
       emp_name VARCHAR2(25),
       email VARCHAR2(30),
       dept_no NUMBER);

   CREATE TABLE copy_emp(emp_no, emp_name, email, dept_no)
       AS SELECT employee_id, last_name, email, department_id
           FROM employees;

   CREATE TABLE emp_def(
       emp_no NUMBER,
       emp_name VARCHAR2(25),
       hire_date DATE DEFAULT SYSDATE,
       dept_no NUMBER);

* ``CREATE TABLE`` 文を実行するにはその権限が付与されている必要がある。
* 副問い合わせを用いて表を作成するときは、表の定義とあわせてテータのコピーもなさ
  れる。特に、値と制約をコピーする。
* 列の既定値をキーワード ``DEFAULT`` に続けて指定してもよい。これは ``INSERT``
  処理で対応する列に値が指定されないときに意味がある。

.. code:: plpgsql

   ALTER TABLE departments READ ONLY;

``ALTER TABLE`` 文で表の何かを変更することができる。

* 列を追加することができる。
* 既存の列の属性を変更することができる。
  ただし、データのある列のデータ型変更やサイズ変更には一部制限がある。
* 既存の列を削除することができる。
* 表の状態を読み取り専用にすることができる。

``DROP TABLE`` 文で表全体を削除することができる。表そのものが存在しなくなる。

制約
----------------------------------------------------------------------

最後に制約について見ていく。

* ``NOT NULL``
* ``UNIQUE``
* ``PRIMARY KEY``
* ``FOREIGN KEY``
* ``CHECK``

.. code:: plpgsql

   CREATE TABLE employees(
       employee_id NUMBER,
       last_name VARCHAR2(25) NOT NULL, -- 名なしで NOT NULL 制約を付与
       commission_pct NUMBER(2, 2),
       manager_id NUMBER,
       job_id VARCHAR2(10) CONSTRAINT emp_job_nn NOT NULL, -- NOT NULL 制約を付与
       department_id NUMBER);

* ``NOT NULL`` 制約を設定すると、その列に ``NULL`` を格納することが許されない。
* ``NOT NULL`` 制約を設定するのは列とする。

.. code:: plpgsql

   CREATE TABLE employees(
       employee_id NUMBER,
       last_name VARCHAR2(25),
       email VARCHAR2(30) CONSTRAINT emp_ema_uk UNIQUE, -- 列定義で設定
       commission_pct NUMBER(2, 2),
       manager_id NUMBER,
       job_id VARCHAR2(10),
       department_id NUMBER);

   CREATE TABLE employees(
       employee_id NUMBER,
       last_name VARCHAR2(25),
       email VARCHAR2(30),
       commission_pct NUMBER(2, 2),
       manager_id NUMBER,
       job_id VARCHAR2(10),
       department_id NUMBER,
       CONSTRAINT emp_ema_uk UNIQUE(email)); -- 表定義で設定

* ``UNIQUE`` 制約を設定すると、その列に重複値を格納することが許されない。ただし
  ``NULL`` は許される。
* ``UNIQUE`` 制約は上のように列に書く方法と表に書く方法がある。どちらも同じこと
  になる。
* ``UNIQUE`` 制約のある列には自動的に索引がつけられる。

.. code::plpgsql

   CREATE TABLE employees(
       employee_id NUMBER CONSTRAINT emp_pk PRIMARY KEY, -- 列定義で設定
       last_name VARCHAR2(25),
       email VARCHAR2(30),
       commission_pct NUMBER(2, 2),
       manager_id NUMBER,
       job_id VARCHAR2(10),
       department_id NUMBER);

   CREATE TABLE employees(
       employee_id NUMBER,
       last_name VARCHAR2(25),
       email VARCHAR2(30),
       commission_pct NUMBER(2, 2),
       manager_id NUMBER,
       job_id VARCHAR2(10),
       department_id NUMBER,
       CONSTRAINT emp_pk PRIMARY KEY(employee_id)); -- 表定義で設定

``PRIMARY KEY`` 制約は ``UNIQUE`` 制約であって ``NULL`` の値を許さないものとみな
せる。

.. code:: plpgsql

   CREATE TABLE employees(
       employee_id NUMBER,
       last_name VARCHAR2(25),
       email VARCHAR2(30),
       commission_pct NUMBER(2, 2),
       manager_id NUMBER,
       job_id VARCHAR2(10),
       department_id NUMBER REFERENCES departments(department_id));

   CREATE TABLE employees(
       employee_id NUMBER,
       last_name VARCHAR2(25),
       email VARCHAR2(30),
       commission_pct NUMBER(2, 2),
       manager_id NUMBER,
       job_id VARCHAR2(10),
       department_id NUMBER,
       CONSTRAINT emp_fk FOREIGN KEY department_id
           REFERENCES departments(department_id));

* ``FOREIGN KEY`` 制約は表の参照関係を定義する制約だ。これを付与することで関連表
  の関連レコードに対する追加・変更・削除に一定の制限がつく。
* ``FOREIGN KEY`` 制約は上のように列に書く方法と表に書く方法がある。どちらも同じ
  ことになる。
* ``FOREIGN KEY`` 制約のオプションには次のものがある：

  * ``ON DELETE CASCADE``: 参照されているデータを削除するときに、参照するデータ
    も削除される。
  * ``ON DELETE SET NULL``: 参照されているデータを削除するときに、参照するデータ
    の値を ``NULL`` にする。

.. code:: plpgsql

   CREATE TABLE employees(
       employee_id NUMBER,
       last_name VARCHAR2(25),
       email VARCHAR2(30),
       salary NUMBER CONSTRAINT emp_sal_ck CHECK (salary > 0), --
       commission_pct NUMBER(2, 2),
       manager_id NUMBER,
       job_id VARCHAR2(10),
       department_id NUMBER);

   CREATE TABLE employees(
       employee_id NUMBER,
       last_name VARCHAR2(25),
       email VARCHAR2(30),
       salary NUMBER,
       commission_pct NUMBER(2, 2),
       manager_id NUMBER,
       job_id VARCHAR2(10),
       department_id NUMBER,
       CONSTRAINT emp_sal_ck CHECK (salary > 0));

* ``CHECK`` 制約は列の値に条件を定義する。この条件を満たさない値を格納することは
  許されない。
* ``CHECK`` 制約は上のように列に書く方法と表に書く方法がある。どちらも同じことに
  なる。

.. code:: plpgsql

   ALTER TABLE on_master MODIFY id NUMBER(6) PRIMARY KEY;
   ALTER TABLE on_master ADD CONSTRAINT on_m_pk PRIMARY KEY(id);

既存の表に制約を定義することもできる。

第 11 章 その他のオブジェクト
======================================================================

最終章はビュー、順序、索引、シノニムについて学習する。

ビュー
----------------------------------------------------------------------

ビューとは既存の表の問い合わせ結果を表のように扱えるようにしたものと考えられる。
ビューをうまく利用すれば、ある種の処理を簡略化することができる。

.. code:: plpgsql

   -- いちばん普通のビューの作成方法
   CREATE VIEW emp_v
       AS SELECT employee_id, last_name, email, hire_date, department_id
           FROM employees WHERE job_id = 'IT_PROG';

   -- ビューを変更する。
   -- この例は列名を変更する。
   CREATE OR REPLACE VIEW emp_v(
       emp_no, name, email, h_date, dept_no)
       AS SELECT employee_id, last_name, email, hire_date, department_id
           FROM employees WHERE job_id = 'IT_PROG';

   -- 複数テーブルからビューを定義する
   CREATE OR REPLACE VIEW dept_v(
       dept_name, maxsal)
       AS SELECT d.department_name, MAX(e.salary)
           FROM employees e JOIN department d
           ON e.department_id = d.department_id
           GROUP BY d.department_name;

ビューを通して DML 文を実行することができる場合がある。このとき、元テーブルが変
更されることに注意する。本文にあるように相当な制限がある。例えば ``GROUP BY`` を
用いたビューに対しては DML 文を何もできない。

.. code:: plpgsql

   CREATE OR REPLACE VIEW empdept30_v
       AS SELECT employee_id, last_name, department_id
           FROM employees e
           WHERE department_id = 30
       WITH CHECK OPTION CONSTRAINT empdept30_v_ck;

``WITH CHECK OPTION`` 句でビューを定義すると、``WHERE`` 句の条件を満たさないよう
な DML 文による処理を許さない。

.. code:: plpgsql

   -- WITH READ ONLY 句を使うことでビューを読み取り専用にする
   CREATE OR REPLACE VIEW emp50_v
       AS SELECT employee_id, last_name, department_id
           FROM employees
           WHERE department_id = 50
       WITH READ ONLY;

   DROP VIEW emp_v;

``DROP VIEW`` 文でビューを削除する。元テーブルは保たれる。

順序
----------------------------------------------------------------------

順序とは、一意的な番号を自動的に生成するデータベースオブジェクトだ。一般的には主
キーの値を作成するのに用いる。

順序オブジェクトには ``nextval`` および ``currval`` という名前の「列」が存在す
る。

.. code:: plpgsql

   CREATE SEQUENCE emp_cp_seq
       INCREMENT BY 1 -- 増分間隔を明示的に指示する（おそらくデフォルト値）
       MAXVALUE 100 -- 発番される最大値
       CYCLE -- 発番を最大値まで尽くすと、また初期値から発番する
       CACHE 10; -- メモリーに保持する番号の個数

``CREATE SEQUENCE`` 文は順序オブジェクトを作成する。

* ``INCREMENT BY`` は整数値をとる。
* この例では用いていないが ``START WITH`` オプションで発番の初期値を指定可能。
* ``MAXVALUE`` を指定する場合は、その値が ``START WITH`` のそれより大きい必要が
  ある。``MINVALUE`` オプションでは、順序オブジェクトが発番する番号の最小値を指
  定できる。
* ``CYCLE`` オプションを指定するときは ``MAXVALUE`` の明示的な指定が必要。
  ``NOCYCLE`` オプションを指定すると、発番は最大値に達すると終了する。

.. code:: plpgsql

   -- 最大値が 200 に達すると発番を最初から戻すオプションをやめてみる。
   -- これは上の定義に矛盾するので失敗する。
   ALTER SEQUENCE emp_cp_seq
       MAXVALUE 200
       NOCYCLE;

``ALTER SEQUENCE`` 文は既存の順序オブジェクトの属性を変更する。

* ``START WITH`` の値を変更することはできない。
* 発番に矛盾を生じるような変更は許されない。
* ``ALTER SEQUENCE`` 文では変更したい性質だけを命令すればよい。

.. code:: plpgsql

   DROP SEQUENCE emp_cp_seq;

``DROP SEQUENCE`` 文は順序オブジェクトを削除する。オプションはない。

索引
----------------------------------------------------------------------

索引オブジェクトとは、表のデータの位置情報を保持するものだ。これがあると、その表
に対する問い合わせが高速化されると一般には期待される。

.. code:: plpgsql

   -- 表 emp_copy の列 employee_id に対して索引を作成する
   CREATE INDEX empid_cp_idx ON emp_copy (employee_id);

   -- 索引 empid_cp_idx を削除する
   DROP INDEX empid_cp_idx;

索引を作成すると効果的な場合は次の通り：

* 列にさまざまな種類の値が含まれる
* 列に多数の ``NULL`` がある
* 列が ``WHERE`` 句の条件に頻繁に用いられる
* 表が巨大であり、問い合わせがそのうちの 4% 程度しか返さないことがわかっている

効果的でない場合は、上の否定に加えて：

* 表が頻繁に更新される
* 列が式の一部として参照される

シノニム
----------------------------------------------------------------------

シノニムすなわち別名だ。これまでのデータベースオブジェクトには別名を付けることが
できる。プログラミングでは別名をつけることは基本的な考え方だ。

シノニムには public と private の二種類が存在する。それらの意味はオブジェクト指
向プログラミング用語のそれとほぼ同じ。

.. code:: plpgsql

   -- ユーザー scott が所有する employees 表に対して emp という別名をつける
   CREATE SYNONYM emp FOR scott.employees;

   -- その別名を unalias する
   DROP SYNONYM emp;

手許に SQL 環境がないから試していないが、同じオブジェクトに対して複数の別名を付
けることができると思う。

付録 SQL 構文一覧
======================================================================

本書で扱われなかった構文だけ列挙しておく。

.. code:: plpgsql

   ALTER FUNCTION
   ALTER INDEX
   ALTER PACKAGE
   ALTER PROCEDURE
   ALTER PROFILE
   ALTER ROLE
   ALTER SESSION
   ALTER SYSTEM
   ALTER TABLESPACE
   ALTER TRIGGER
   ALTER USER
   AUDIT
   COMMENT
   CREATE DATABASE
   CREATE OR REPLACE DIRECTORY
   CREATE FUNCTION
   CREATE PFILE
   CREATE PROCEDURE
   CREATE PROFILE
   CREATE ROLE
   CREATE SPFILE
   CREATE TABLESPACE
   CREATE TRIGGER
   CREATE USER
   DROP DIRECTORY
   DROP PROCEDURE
   DROP PROFILE
   DROP ROLE
   DROP TABLESPACE
   DROP TRIGGER
   DROP USER
   FLASHBACK DATABASE
   FLASHBACK TABLE
   LOCK TABLE
   NOAUDIT
   PURGE
   RENAME
   SET CONSTRAINTS
   SET ROLE

   GRANT
   REVOKE
