======================================================================
YAML 学習ノート
======================================================================

Jekyll や GitHub Actions など、構成ファイルを YAML 形式で記述する機会が増えてき
ている。人間が書きやすい書式ということだが、私が最初これを編集したときにコレク
ション値の記述法に混乱して当惑した記憶がある。そこでノートを取ろうとしたのだが、
確認すると世の中にすでに良い記事があり、それらをすぐに参照できるようにしておくの
が最善と判断した。

.. contents::

教材
======================================================================

教材が示す YAML コード片を後述の YAML Viewer に与えながら構文の癖を理解すると良
いようだ。YAML のバージョンがそこそこ重要だ。

`YAML Tutorial <https://www.tutorialspoint.com/yaml/index.htm>`__
   Tutorials Point によるチュートリアル。一部、Viewer を通らないコードがあるが、
   少しの修正で整形式になる場合がある。こういう修正が学習になる。
`YAML Tutorial: Everything You Need to Get Started in Minutes | Cloudbees Blog <https://www.cloudbees.com/blog/yaml-tutorial-everything-you-need-get-started>`__
   Python で YAML を扱う方法を述べている。コードが少々壊れているので読者が直す。
   これも学習だ。

   .. code:: python

      #!/usr/bin/env python

      from yaml import load
      try:
          from yaml import CLoader as Loader
      except ImportError:
          from yaml import Loader

      if __name__ == '__main__':
          with open('foo.yaml', 'r') as stream:
              dictionary = load(stream, Loader)
              for key, value in dictionary.items():
                  print(f"{key}: {value}")

   上位互換スクリプトである二つ目の ``load_all`` のほうも同様に修正すれば動作する。
`YAML Tutorial: A Complete Language Guide with Examples <https://spacelift.io/blog/yaml>`__
   叙述がスマートな感じがして安心して読める。スキーマの概念をよく説明できてい
   る。
`Mastering YAML: A Comprehensive Guide To YAML files <https://saarthakmaini.hashnode.dev/mastering-yaml-a-comprehensive-guide-to-yaml-files>`__
   YAML が簡潔に要約されている。コード例の ``!!`` を含むものを Viewer に通るよう
   に修正する方法がわからない。
`Mastering YAML Files: A Step-by-Step Guide <https://www.noobgeek.in/blogs/mastering-yaml-files-a-step-by-step-guide>`__
   どちらかと言えば文章主体である骨太の記事。

ツール
======================================================================

オンラインツール
----------------------------------------------------------------------

`YAMLlint - The YAML Validator <https://www.yamllint.com/>`__
   入力欄に YAML コードを貼り付けて :guilabel:`Go` ボタンを押すと、内容が valid
   か否かを示すサービスだ。単純にして明瞭だ。
`Best YAML Viewer Online <https://jsonformatter.org/yaml-viewer>`__
   左ペインに YAML を入力すると右ペインにツリーを出力するオンラインサービス。き
   わめて有用。
`json2yaml.com <https://www.json2yaml.com/>`__
   左ペインに JSON を入力すると右ペインに等価 YAML を出力するオンラインサービス。
`Online YAML Parser <https://yaml-online-parser.appspot.com/>`__
   左ペインまたは指定 URL にある YAML コードを入力とし、右ペインにそれと等価な次
   のいずれかのコードを出力するオンラインサービスだ：

   * JSON
   * Python
   * 正典 YAML

`YAMLine.com - The YAML Semantic Comparator <https://yamline.com/compare/>`__
   2つのYAML間の差分を生成するオンラインサービス。

差し当たり上記のものをブックマークしておけば十分だろう。

エディター拡張
----------------------------------------------------------------------

`learn-yaml - Visual Studio Marketplace <https://marketplace.visualstudio.com/items?itemName=docsmsft.docs-yaml>`__
   VS Code 拡張で ``YAML`` を検索すると人気第二位のものだ。編集中に構文・スキー
   マ検査を行うのが便利だ。

コマンドラインインターフェイス
----------------------------------------------------------------------

`mikefarah/yq: yq is a portable command-line YAML, JSON, XML, CSV, TOML and properties processor <https://github.com/mikefarah/yq>`__
   README の記述から :command:`jq` の上位互換を目指すものであることが期待できる。
   インストールには Homebrew が使用可能。

   .. code:: console

      $ yq '.' foo.yaml
      foo: bar
      pleh: help
      stuff:
        foo: bar
        bar: foo
      $ yq '.stuff' foo.yaml
      foo: bar
      bar: foo
      $ yq '.stuff.bar' foo.yaml
      foo
      $ yq '.[] | select(.foo == "bar")' foo.yaml
      foo: bar
      bar: foo
      $ yq '.' documents.yaml
      bar: foo
      foo: bar
      ---
      one: two
      three: four
      $ yq '.one' documents.yaml
      null
      ---
      two

`pyyaml.org <https://pyyaml.org/>`__
   Python で YAML を取り扱うためのパッケージは標準には今のところないので、こうい
   うものを ``pip install`` しておくといい。

仕様
======================================================================

`The Official YAML Web Site <https://yaml.org/>`__
   上述の教科書で正とされている YAML コードが各種ツールで不正とみなされるとき
   に、ここから仕様書を探して確認するのに使う。
