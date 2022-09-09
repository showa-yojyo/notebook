======================================================================
プログラミング C# 第 6 版 読書ノート
======================================================================

.. include:: /_include/book-details/griffiths10.txt

本当は自腹で購入して鉛筆片手にメモを書き込みしながら読んでいきたい本。

このメモは第 6 版をほぼ一読した限りでの内容なのだが、
この版は版元のサイトによると絶版済みだそうだ。
今から読むのであれば当然最新版の改訂版を読むべし。
C# 5.0 に対応している。

.. contents:: ノート目次

.. todo::

   以下、書き殴りメモ。いつか整理するはず。

私の参考になった章をいくつか挙げてみると、次のようになる。

* 3 章。クラスにまつわる説明がありがたかった。
  つい私の第一言語である C++ との違いを見つけながら読んでしまうが。
* 5 章。デリゲート関連。
* 8 章。LINQ の基礎概念の記述。

ついていけなかったのは、アセンブリ、スレッド、リフレクションあたり。
WPF, SilverLight, ASP.NET の章は後回しにしたかったので、
未だにまともに読んでいない。

1 章 C# 言語の基礎
======================================================================
ノートなし。

2 章 基本的なプログラミングテクニック
======================================================================
* ``using`` の整理
* George Boole
* 2.8.1 ``for each``

3 章 クラスと構造体によるアイデアの抽象化
======================================================================
C++ との違いに注意しながら読む。

* 3.1.2 Dahl, Nygaard, Simula 67.
* 3.2.1 プロパティ。Pascal 記法と Camel 記法。
* ``public``, constructor, field, ``const``, ``readonly``.
* 3.3 ``enum`` 明示的な値と型 (governing type)
* コラム
* 3.6.1 ``default(...)``
* 3.7 オブジェクト初期化子 ``{ }`` を使うヤツ。
* 3.8 ``this`` の使い方が C++ より多い。
* 3.8.1 ``static``

4 章 拡張性とポリモーフィズム
======================================================================
Firefighter の例。

* 4.3 ``new`` による上書き。隠蔽である。
* 4.3.2 ``virtual`` と ``override`` の違い。
* 4.4 ``protected internal`` アセンブリ内から。
* 4.6 ``sealed class``
* 4.7 ``abstract class`` でメソッド宣言にも ``abstract`` を。
* 4.8.1 ボックス
* 4.10 ``interface``
* 4.12 ``as`` と ``is`` について。
  丸括弧キャストが避けられるときはこれらを用いて避けたい。

5 章 デリゲートによる結合性と拡張性の向上
======================================================================
``delegate void DocumentProcess(Document doc);`` のような構文。

* コラム Multicast Delegate
* 5.2 ``Action<Document>``
* 5.3 ``Predicate<T>`` p: X → { true, false }
* 5.4 匿名メソッド
* 5.5 ラムダ式。記法に慣れること。

  .. code:: c#

     Predicate<Document> pred = doc => !doc.Text.Contains("?");

* 5.7 ``Function<T, TResult>``
* 5.8 ``event EventHandler``

  .. code:: c#

     (sender, e) => ...

* 5.8.1 ``add``, ``remove``

6 章 エラー処理
======================================================================
* 6.2.1 Ctrl+Alt+C でコールスタックウィンドウが出る。
* 6.3.1 ``InnerException``

  * 例外を定義する場合は ``[Serializable]``
  * ``ApplicationException`` は使い物にならない。

7 章 配列とリスト
======================================================================
* 7.1.1.1 ``params`` 例 ``split``
* 7.1.3 配列はクラス ``Array`` のサブクラス。
  ``FindAll``, ``FindIndex``, ``IndexOf``
* 7.1.3.2 ``Array.Sort``
* 7.1.3.3 ``Array.CopyTo``
* 7.2 ``List<T>`` は配列なくしては存在し得ない。
  ``Add``, ``Insert``, ``AddRange``
* 7.2.1 ``public string this[int index]``
* 7.3 ``IEnumerable<T>``, ``IEnumerator<T>``
* 7.3.1 ``yield return``

8 章 LINQ
======================================================================
読むのが初めてならば、内容がなかなか頭に入ってこないと思う。

* 8.1 まずは ``Dictionary.EnumerateFiles`` を利用した例。

  .. code:: c#

     var q = from file in Dictionary.EnumerateFiles(...)
             where new FileInfo(file).Length > 10000000
             select file;

  ``select file`` の部分は、例えば ``select File.ReadAllLines(file).Length`` のようなものでも通じる。

* 8.1.1 そのまま ``.Where(...).Select(...);`` と書き換え可能。
* 8.1.2 拡張メソッド。既存のクラスに対して、メンバーメソッドを追加定義できる。
  だから ``Where`` はこういうモノだ。

  .. code:: c#
  
     public static IEnumerable<TSource> Where<TSource>(
     this IEnumerable<TSource> src,
         Func<TSource, bool> predicate);

* 8.1.3 ``let`` 句。先程の例では ``new FileInfo`` の処理が勿体ない。こうする。

  .. code:: c#

     var q = from file in Dictionary.EnumerateFiles(...)
             let info = new FileInfo(file)
             where info.Length > 10000000
             select file;

* 8.2.3 LINQ クエリーは可能な限り遅延評価となる。
* 8.3.2 ``orderby``, ``thenby``
* 8.3.3 ``concat``
* 8.3.4 ``group ... by [into ...]``
* 8.3.5.1 匿名型

9 章 コレクションクラス
======================================================================
* 9.1 変数宣言のコツとして ``var`` でタイピングの労力を節約する。
* 9.1.2 ``IDictionary<K, V>``
* 9.1.3 LINQ との絡み。
* 9.2 ``HashSet``, ``SortedSet``
* 9.4 ``LinkedList``
* 9.5 ``Stack``

10 章 文字列
======================================================================
* 10.4 ``ToString`` の引数で書式指定。
* 10.4.4 ``Convert.ToInt32(...)`` 等
* 10.4.5 ``String.Format``
* 10.5 ``System.Globalization.CultureInfo``
* 10.15

  * ``Encoding.UTF8.GetBytes(文字列)`` → バイト列
  * ``Encoding.ASCII.GetBytes(文字列)`` → バイト列
  * ``.GetString(バイト列)`` → 文字列
  * charmap.exe
  * Unicode といったら UTF16 らしい。
  * ``Console.WriteLine(string.Format("{0:X2}", バイト列))``

11 章 ファイルおよびストリーム
======================================================================
* 11.3 ファイルパスの操作
* 11.7 特殊フォルダー ``Environment.GetFolderPath``
* 11.8 ``Path.Combine``
* 11.9 フォルダー作成は大変
* 11.11.2 ``using (StreamWriter sw = File.CreateText(path))``
  デフォルトで utf-8
* 11.12.1 ``FilSystemAccessRule`` UAC
* 11.14 ``FileStream``
* 11.17 非同期ファイル操作
  ``FileOptions.Asynchronous``, ``BeginWrite``, ``WaitOne``, ...
* 11.18 分離ストレージ
  ``IsolatedStorageFile.GetUserStorageForAssembly``

12 章 XML
======================================================================
* 12.3 ``XDocument``, ``XElement``, ...
* 12.4 LINQ との絡み。

  .. code:: c#

     from customer in customerXml.Descendants("Customers")
         where customer.Elemen("EmailAddress").Value == "dAdams@....com"
         select customer;

* 12.5 ``XmlSerializer``
* 12.5.1 ``[XmlAttribute]``, ``[XmlIgnore]``

13 章 ネットワーク処理
======================================================================
* 13.3 HTTP

  .. code:: c#
  
     WebClient client = new WebClient();
     string pageContent = client.DownloadString("http://oreilly.com/");
     byte[] data = client.DownloadData(""http://.../oreilly_large.gif");

  * ``DownloadFile`` もある。
  * 非同期版もある。イベントハンドラーを ``add`` してから ``Async`` メソッドで呼び出す。

* 13.3.2 ``WebRequest``, ``WebResponse``

  * コードが長い。
  * ``async`` だから慣れていないとつらい。

* 13.3.2.1 認証の例
* 13.3.2.3 キャッシュ

14 章 データベース
======================================================================
データベースなので読み飛ばす。

15 章 アセンブリ
======================================================================
* 15.2 ``typeof(MyType).AssemblyFullName``
* 15.2.1 strongly named assembly

16 章 スレッドおよび非同期コード
======================================================================
speculation

* 16.1 ``System.Threading``
* 16.1.2 ``Thread th = new Thread(() => Go(result, "One"));``
  よくない。
* 16.1.3 ``ThreadPool.QueueUseWorkItem(Go, "One"));``
  かなり短い作業向け。例えばウェブページを一枚生成する程度の。
* 16.1.4 thread affinity, ``SynchronizationContext``
* 16.1.5.3 ...
* 16.2.1 必要以上にロックオブジェクトを保持するのは避ける。

  .. code:: c#

     lock(lockObject)
         while(!canGo)
             Monitor.Wait(lockObject);

  .. code:: c#

     lock(lockObject)
         canGo = true;
         Monitor.PulseAll(lockObject);

* 16.3 非同期プログラミング
  ``IAsyncResult``, ``AsyncCallback``
* 16.4 タスク並列 TPL

  .. code:: c#

     Task.Factory.StartNew(Go, "One");
     Task.WaitAll(t1, t2);

* 16.4.1.1 親子
* 16.4.1.4 ``ContinueWith``
* 16.4.1.5 ``TaskScheduler``
  ``ContinueWith((task) => UpdateUI(...));`` みたいな。

  * ムダなキャンセル。

* 16.5 データ並列性

  .. code:: c#
  
     Parallel.For(0, pixelHeight, pixelY) =>
     {
         ...
     });

17 章 属性およびリフレクション
======================================================================
``System.Reflection.MemberInfo``

18 章 ダイナミック
======================================================================
昔 VB6 のコードを VB .NET 2005 に書き換える大変な仕事をしたことを思い出した。
Excel のファイルを開いてシートにデータを書き出すだけのものなのに、
コードがえらく冗長になった記憶がある。

* 18.2.1.1 ``dynamic doc = wordApp.Documents.Open("xxx.docx", ReadOnly:=true);``

19 章 COM および Win32 との相互運用
======================================================================
わからん。

* 19.2 Interop Assembly
* 19.4 P/Invoke
* 19.6.2 省略可能な ``ref``

20 章 WPF と Silverlight
======================================================================
ノートなし。

21 章 ASP.NET プログラミング
======================================================================
ノートなし。

22 章 Windows フォーム
======================================================================
ノートなし。ちなみのこの章は次の版ではボツになった？
