======================================================================
Python 移行ノート
======================================================================

.. contents:: ノート目次

.. note::

   * OS: Windows XP Home Edition SP 3

2.6 から 2.7 への移行計画
======================================================================

Python 2.7 本体をインストール
----------------------------------------------------------------------

Python 2.6 フォルダーから一部のファイルをコピーする
----------------------------------------------------------------------
* site.py
* sitecustomize.py

最初に手動で準備するもの
----------------------------------------------------------------------
* setuptools
* easy-install
* pip

Windows インストーラーを利用するもの
----------------------------------------------------------------------

* PIL_: 公式サイトに 2.7 用のものがある。
* NumPy_: 2.7 OK
* SciPy_: 2.7 OK
* Matplotlib_: 2.7 OK
* Pygame_: 2.7 OK
* Py2exe_: 公式にはない。追記参照。
* PyQt4_: 2.7 OK

旧環境での pip --freeze の出力を利用するもの
----------------------------------------------------------------------
2.6 環境で ``pip --freeze`` することで、利用中の ``site-packages`` パッケージが得られる。
これを 2.7 環境の ``pip`` に食わせて様子見とする。
もちろん 2.7 に対応しているものだけを残して、あとは全部カットしておく。

Python 2.7 における各パッケージをいちいち調べるのは面倒なので、
先にインストールを try してみて、ログで成否を判断する作戦だ。

* actdiag -- OK
* apgl -- OK
* Babel -- ?
* BeautifulSoup -- ?
* blockdiag -- OK
* coverage -- OK
* dateutil -- ?
* docutils -- OK
* funcparserlib -- OK
* Genshi -- ?
* httplib2 -- ?
* jinja2 -- ?
* nose -- ?
* nwdiag -- OK
* oauth2
* OpenGLContext -- ?
* OpenGLContext_full -- ?
* ordereddict
* pep8
* pygments
* PyOpenGL
* pyopengl_demo
* Pyrex
* pysparse
* python_dateutil -- ?
* pytz
* PyVRML97
* rackdiag -- OK
* reportlab
* rst2pdf
* seqdiag -- OK
* simplejson
* six
* Sphinx
* Trac
* twitter
* unittest2
* vrml
* webcolors

特殊なもの
----------------------------------------------------------------------

* libsvn
* svn_python

3.x 系最高バージョンへの移行
======================================================================
まだ先の話。

.. _Python: http://www.python.org/
.. _PyPI: http://pypi.python.org/pypi

.. _easy_install: http://peak.telecommunity.com/DevCenter/EasyInstall
.. _pip: http://pypi.python.org/pypi/pip
.. _setuptools: http://peak.telecommunity.com/DevCenter/setuptools
.. _distribute: http://pypi.python.org/pypi/distribute
.. _Python Extension Packages for Windows - Christoph Gohlke: http://www.lfd.uci.edu/~gohlke/pythonlibs/

.. _Nose: http://somethingaboutorange.com/mrl/projects/nose/
.. _NumPy: http://scipy.org/NumPy/
.. _SciPy: http://www.scipy.org/
.. _Matplotlib: http://matplotlib.sourceforge.net/
.. _PIL: http://www.pythonware.com/products/pil
.. _Pygments: http://pygments.org/
.. _Jinja2: http://jinja.pocoo.org/
.. _Sphinx: http://sphinx.pocoo.org/
.. _PyQt4: http://www.riverbankcomputing.com/software/pyqt/intro
.. _coverage: http://nedbatchelder.com/code/coverage
.. _PyOpenGL: http://pyopengl.sourceforge.net/
.. _Py2exe: http://www.py2exe.org/
.. _Pygame: http://www.pygame.org/
.. _Python Twitter Tools: http://mike.verdone.ca/twitter/
