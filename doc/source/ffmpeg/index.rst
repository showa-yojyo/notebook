======================================================================
FFmpeg 利用ノート
======================================================================

FFmpeg に関するノートだ。利用環境は次のとおりで、新しい環境もこれに準じると想定
する。シェルは Bash とする。

:command:`wsl -v` の出力内容は次のとおり：

:WSL: 1.0.3.0
:Kernel: 5.15.79.1
:WSLg: 1.0.47
:MSRDC: 1.2.3575
:Direct3D: 1.606.4
:DXCore: 10.0.25131.1002-220531-1700.rs-onecore-base2-hyp
:Windows: 10.0.19045.2670

:command:`lsb_release -a` の出力内容は次のとおり：

:Distributor ID: Ubuntu
:Description:    Ubuntu 22.04.1 LTS
:Release:        22.04
:Codename:       jammy

.. toctree::
   :maxdepth: 2

   basic
   ffprobe
   ffplay
   references
