======================================================================
ORACLE MASTER Bronze 11g SQL 基礎 I 必修教本 読書ノート
======================================================================

近所の図書館のリサイクルワゴンに本書が突っ込まれていたので回収した。
内容はきわめて初歩的なのだが、データベースを仕事でほとんど使わなかったのでノートをとることにする。

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
    * 複数の表の間に何らかの関係を定義する。表の間というより、表に含まれているレコード
      （本書ではエンティティと呼んでいるが）とレコードの間に関係がある。

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

* 1970 年に IBM の E. F. Codd 博士が RDB を考案したとある。当初は理論だけで実装はまだなかった。
* 階層型やネットワーク型のデータベースは現在ほとんど存在しない。

第 1 章 基本的なデータ検索
======================================================================

本章では ``SELECT`` 文を学習する。ここは理解に問題はない。
例だけを書いてあとで補足する。

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

   コードハイライトが Pygments の ``sql`` でうまくいかない。暫定的に
   ``plpgsql`` にしておく。欲を言えば Oracle もサポートして欲しい。

* キーワード、表名、列名、関数名、等々、大文字と小文字はまったく区別されない。
* 文末には ``;`` を付けるほうが無難。特に SQL*Plus 環境では実行に要る。

* 型によっては列に対して算術演算 ``+``, ``-``, ``*``, ``/`` を適用できる。

* ``NULL``

  * 未確定の状態を表す特別な値である。
  * 数 0 や空白文字とは異なる。

    * 列の型が文字列ならば空文字列とは同じ概念なのかもしれない。

  * ``NULL`` に対してどのような算術演算を施しても結果は ``NULL`` となる。重要。

* ``SELECT`` 文の列見出しは通常大文字で表示される。小文字がよければ ``"`` で囲む。

* 演算子 ``||`` は文字列の連結を行う。こちらは ``NULL`` を空文字列として処理する。
* 演算子 ``q`` は C++11 の ``R`` 文字列に似ている。

* 選択結果から重複データを除外して表示するのに ``DISTINCT`` を用いる。

* ``DESCRIBE`` コマンドは表の定義を出力するものだが、Oracle Database 独自のものだ。

第 2 章 データ検索における制限とソート
======================================================================

言い忘れたが SQL 文の出力はここには書かない。

.. code:: plpgsql

   SELECT employee_id, last_name, department_id FROM employees
       WHERE department_id = 50;
   SELECT employee_id, last_name, department_id FROM employees
       WHERE last_name = 'Grant';
   SELECT employee_id, last_name, hire_date FROM employees
       WHERE hire_date = '00-JAN-13';

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

   SELECT employee_id, last_name, department_id FROM employees
       WHERE department_id BETWEEN 50 AND 90;

   SELECT employee_id, last_name, department_id FROM employees
       WHERE department_id IN (40, 60, 80);

   SELECT employee_id, last_name FROM employees
       WHERE last_name LIKE 'A%';
   SELECT employee_id, last_name, jpb_id FROM employees
       WHERE job_id LIKE 'SA\_%' ESCAPE '\';

   SELECT employee_id, last_name, manager_id FROM employees
       WHERE manager_id IS NULL;

   SELECT employee_id, last_name, salary, department_id FROM employees
       WHERE salary >= 2500
           AND department_id = 50;
   SELECT employee_id, last_name, salary, department_id FROM employees
       WHERE salary >= 2500
           OR department_id = 50;
   SELECT employee_id, last_name, salary, department_id FROM employees
       WHERE department_id NOT IN (50, 80);

* ``WHERE`` 句を付すことで検索条件を定義する。両辺が等しいかどうかは比較演算子の一つ ``=`` を用いる。
* 条件式に関しては大文字と小文字は区別される。
* 日付の指定は書式がどうなっているのかを把握する必要があるのでミスが多いのでは？

    * デフォルトの日付書式は `DD-MON-RR`
    * 日付については後述

* 二項比較演算子は常識的なものが使える。not equal は `<>`, `!=` の他に `^=` というものがある。
* ``BETWEEN ... AND ...`` と ``IN (...)`` という構文もある。
* 文字列条件の指定にはワイルドカードが存在する。

  * ``%``: 任意の文字 0 文字以上
  * ``_``: 任意の 1 文字

* ワイルドカードをリテラルに指定したい場合には他のプログラミング言語のようにエスケープをするわけだが、
  キーワード ``ESCAPE`` を用いてエスケープ文字を明示する必要がある。

* 列が ``NULL`` かどうかは ``IS NULL``, ``IS NOT NULL`` を用いる。
* 論理演算子 ``AND``, ``OR``, ``NOT`` を条件式に使える。
* 演算子の優先順位は次のように憶える:

  * 比較演算子のほうが論理演算子より高い
  * 論理演算子では not, and, or の順に高い

* 演算の優先度を調節するときは、他のプログラミング言語のように丸括弧を用いる。

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

* ``ORDER BY`` 句はレコードをソートして出力する。``ORDER BY`` 句のオプションとして次のものがある：

  * ``ASC``: 行を昇順にソートする。デフォルト。
  * ``DESC``: 行を降順にソートする。
  * ``NULLS FIRST`` : ``NULL`` が存在する場合には先頭に出力する。
  * ``NULLS LAST``: ``NULL`` が存在する場合には末尾に出力する。

* 順序の定義は数、文字列、日付それぞれで自然に考える。

あとはプレースホルダー機能のようなものが SQL*Plus にあることが紹介されている。

第 3 章 単一行関数
======================================================================

Oracle Database で使用する SQL 関数のほとんどが本製品固有のものだ。
したがって SQL Server なと他社製品では使用できない。

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
* 関数 ``ROUND``, ``TRUNC`` は第二引数に注意。小数点の左、つまり桁が大きくなるほうに行くのが負。

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

型変換には暗黙的なものと明示的なものに分類できる。
暗黙的なものは文字列型系 (VARCHAR2, CHAR) を数値型系 (NUMBER, DATE) に、
またはその反対に数値型系から文字列型系に変換したりする。

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

* 関数 ``NULLIF`` は二引数が等しければ NULL を返すという妙なものに見えるが、これを用いて条件分岐をすることができる。
* 関数 ``COALESCE`` は最初の非 NULL 要素を返す。Oracle 固有。
* 関数 ``CASE`` の劣化版として ``DECODE`` という Oracle 固有のものがある。

第 5 章 グループ関数
======================================================================

グループ関数は表内のレコードを何らかの基準でグループ化したのち、何らかの集計を行う関数だ。
したがって、入力が複数で出力が一つだ。

集計関数は値が ``NULL`` であるものを無視する。
ただし ``COUNT(*)`` は ``NULL`` を含むものも拾い上げる。
そもそも ``COUNT(*)`` は使うべきではない。

.. code:: plpgsql

   SELECT AVG(salary), SUM(salary), MIN(salary), MAX(salary), COUNT(salary)
       FROM employees;
   SELECT MAX(first_name), MIN(first_name), COUNT(first_name) FROM employees;

次にグループを定義してから集計する方法を記す。``GROUP BY`` 句で列名を指定することでそうなる。

.. code:: plpgsql

   SELECT department_id, AVG(salary) FROM employees
       GROUP BY department_id;
   SELECT job_id, AVG(salary) FROM employees
       GROUP BY job_id;
   SELECT job_id, COUNT(job_id) FROM employees
       GROUP BY job_id;
   SELECT department_id, job_id, COUNT(job_id) FROM employees
       GROUP BY department_id, job_id;

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

* ``GROUP BY`` 句には ``SELECT`` 句に列挙した（集計以外の）列名をすべて列挙する必要がある。気が利かない。
* ``GROUP BY`` 句には列の別名を指定できない。気が利かない。
* ``HAVING`` 句はグループ関数を問い合わせ条件に指定する。
* ``HAVING`` 句にも列の別名を指定できない。これはわかる。

第 6 章 表の結合
======================================================================

第 7 章 副問い合わせ
======================================================================

第 8 章 集合演算子
======================================================================

第 9 章 DML 文（データ操作言語）
======================================================================

第 10 章 DDL 文（データ定義文）
======================================================================

第 11 章 その他のオブジェクト
======================================================================
