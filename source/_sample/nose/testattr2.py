# -*- coding: utf-8 -*-
from nose.plugins.attrib import attr

@attr(speed='slow')
def test_load_all_images():
   # 数分かかるテストケース

   # ...
   pass

@attr(online=True)
def test_download_hardcore_images():
   # 何かインターネットに接続しないと意味のないテスト

   # ...
   pass

# その他のテスト
# ...
