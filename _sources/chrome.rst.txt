======================================================================
Chrome DevTools 利用ノート
======================================================================

Web ブラウザー Google Chrome に付属している `Chrome DevTools <https://developer.chrome.com/docs/devtools/>`__ の利用に関するノート。
その機能のうち容易に利用できるものについて記す。

何はさておき、開発ツールを有効にする方法を習得する。次にコンソールに関する機能を習得するといいだろう。
それからスタイルシート、スクリプト、イベント、デバッグ、等々と手を広げる。

.. contents:: ノート目次

開発ツールを起動する
======================================================================

正規版の Chrome では次のようにして開発ツールを開くらしい：

* ショートカットキー :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`I` を押す。
* ブラウザーで適当な HTML ページを開いて、右クリックメニューから「検証」を選択する。

私が利用している Sleipnir では右クリックメニューからしか起動できないらしい。

開発ツール専用のビューが出現する。上部にメニューがあるので、そこから項目を選んで後述する各ビューを表示させる。

コンソール
======================================================================

開発ツールメニューの Console を選択すると JavaScript が動くコンソールが出現する。
各種シェルやプログラミング言語の対話的モードと同様のものだ。

コンテキストメニュー
----------------------------------------------------------------------

右クリックメニューはシンプルなときとそうでないときがある。

.. csv-table::
   :delim: |
   :header: コマンド, 動作

   :guilabel:`Clear Console` | コンソールの入出力表示をすべて消去する。
   :guilabel:`Clear Console History` | コンソールでの実行履歴を消去する。
   :guilabel:`Save as...` | 実行ログをテキストファイルに保存する。

対象の HTML ページに対して JavaScript で何からのスクレイピングを行い、
ログファイルを保存してテキストエディターで出力部分を取り出すという用途が考えられる。

出力が DOM ノードであって、そこでマウスの右クリックメニューを表示すると細かいメニューが現れる。

オブジェクト ``console``
----------------------------------------------------------------------

オブジェクト ``console`` が最初から利用可能だ。組み込みオブジェクトとでも言えるだろうか。
これは次のようなメソッドを備えている。出力先はすべてコンソールとする。

.. csv-table::
   :delim: |
   :header: メソッド, レベル, 動作

   ``.assert(expression, object)`` | Error | 式が ``false`` のときに限りエラー出力をする。
   ``.clear()`` | n/a | コンソールを消去する。
   ``.count([label])`` | Info | このメソッドが呼び出された回数を出力する。
   ``.countReset([label])`` | n/a | 上述の回数をリセットする。
   ``.debug(object [, object, ...])`` | Verbose | ログレベルを除いて ``.log()`` と同じ。
   ``.dir(object)`` | Info | オブジェクトの内容を JSON 書式で出力する。
   ``.dirxml(node)`` | Info | ノードの（その子孫を含む）内容を XML 書式で出力する。
   ``.error(object [, object, ...])`` | Error | オブジェクトをエラー書式で出力する。スタックトレースも出力する。
   ``.group(label)`` | n/a | 以降の出力をグループ化するように指示する。
   ``.groupCollapsed(label)`` | n/a | ``.group()`` と同じだが、初期表示を折り畳むものとする。
   ``.groupEnd(label)`` | n/a | 出力のグループ化を終了する。
   ``.info(object [, object, ...])`` | Info | ``.log()`` と同じ。
   ``.log(object [, object, ...])`` | Info | オブジェクトをここに出力する。
   ``.table(array)`` | Info | オブジェクトからなる配列を表の形式で出力する。
   ``.time([label])`` | n/a | タイマーを開始する。
   ``.timeEnd([label])`` | Info | タイマーを終了して経過時間を出力する。
   ``.trace()`` | Info | スタックトレースを出力する。
   ``.warn(object [, object, ...])`` | Warning | 警告を出力する。

スクリプトから ``console`` を利用するときに便利であるものが多く含まれる。

コンソール API
----------------------------------------------------------------------

Chrome DevTool が提供するコンソール用オブジェクトと関数を記す。有用なものが多い。

.. csv-table::
   :delim: |
   :header: 機能, 意味

   ``$_`` | 直前に評価された式。シェルや IPython の ``_`` と同じ。
   ``$0``, ..., ``$4`` | 開発ツール内で評価された DOM 要素で直近の五個を参照する。
   ``$(selector, [startNode])`` | CSS セレクターにマッチする DOM 要素を一つ返す。
   ``$$(selector, [startNode])`` | CSS セレクターにマッチする DOM 要素を配列で返す。
   ``$x(path, [startNode])`` | XPath 式にマッチする DOM 要素を配列で返す。
   ``clear()`` | ``console.log()`` と同じ。
   ``copy(object)`` | 対象オブジェクトをクリップボードにコピーする。
   ``debug(function)`` | 関数にデバッガーのブレイクポイントをセットする。
   ``dir(object)`` | ``console.dir(object)`` と同じ。
   ``dirxml(object)`` | ``console.dirxml(object)`` と同じ。
   ``inspect(object/function)`` | 対象に関する情報を専用ビューに表示する。
   ``getEventListeners(object)`` | 対象オブジェクトのイベントリスナーを配列で返す。
   ``keys(object)`` | 対象オブジェクトのメンバー名を配列で返す。
   ``monitor(function)`` | 関数の呼び出しを監視するように指定する。
   ``monitorEvents(object[, events])`` | イベントをログ出力させる。
   ``profile([name])`` | CPU プロファイルセッションを開始する。
   ``profileEnd([name])`` | ``profile([name])`` を終了して結果を専用ビューに表示する。
   ``queryObjects(Constructor)`` | 指定のコンストラクターがここまでに生成したオブジェクトすべてを配列で返す。
   ``table(data[, columns])`` | ``console.table(data[, columns])`` と同じ。
   ``undebug(function)`` | ``debug(function)`` を解除する。
   ``unmonitor(function)`` | ``monitor(function)`` を解除する。
   ``unmonitorEvents(object[, events])`` | ``monitorEvents(object[, events])`` を解除する。
   ``values(object)`` | 対象オブジェクトのメンバー値を配列で返す。

``$_`` は矢印キーの↑で代替するのがふつうだろう。

スクレイピング作業については関数 ``$``, ``$$``, ``$x`` がもっとも有用だ。
これに対してログ保存機能や関数 ``copy()`` を併用するというパターンが多い。

あとは JavaScript コードのデバッグや、DOM の変更をするのに有用な機能となっている。
