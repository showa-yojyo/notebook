#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""eulerian.py: demonstrate NetworkX is_eulerian and eulerian_circuit.

Compute the most efficient career path in DRAGON QUEST 7 (2000).
"""
import networkx as nx
import pprint

def main():
    """The main function.

    Returns:
      None
    """

    G = nx.Graph()
    G.add_edge('せんし', 'とうぞく', skill='ぬすっと斬り')
    G.add_edge('せんし', 'おどりこ', skill='つるぎのまい')
    G.add_edge('せんし', 'ぎんゆうしじん', skill='たたかいの歌')
    G.add_edge('せんし', 'ふなのり', skill='かもめ返し')
    G.add_edge('せんし', 'ひつじかい', skill='みねうち')
    G.add_edge('せんし', 'わらわせし', skill='へんてこ斬り')
    G.add_edge('ぶとうか', 'まほうつかい', skill='火の息')
    G.add_edge('ぶとうか', 'とうぞく', skill='きゅうしょ突き')
    G.add_edge('ぶとうか', 'おどりこ', skill='マッスルダンス')
    G.add_edge('ぶとうか', 'ぎんゆうしじん', skill='おたけび')
    G.add_edge('ぶとうか', 'ふなのり', skill='すいめんげり')
    G.add_edge('ぶとうか', 'ひつじかい', skill='マトンアタック')
    G.add_edge('ぶとうか', 'わらわせし', skill='しっぺ返し')
    G.add_edge('まほうつかい', 'ぶとうか', skill='火の息')
    G.add_edge('まほうつかい', 'とうぞく', skill='マホトラ')
    G.add_edge('まほうつかい', 'おどりこ', skill='マホキテ')
    G.add_edge('まほうつかい', 'ぎんゆうしじん', skill='のろいの歌')
    G.add_edge('まほうつかい', 'ふなのり', skill='いなずま')
    G.add_edge('まほうつかい', 'ひつじかい', skill='ラリホーマ')
    G.add_edge('まほうつかい', 'わらわせし', skill='メダパニ')
    G.add_edge('そうりょ', 'おどりこ', skill='死のおどり')
    G.add_edge('そうりょ', 'ぎんゆうしじん', skill='やすらぎの歌')
    G.add_edge('そうりょ', 'ふなのり', skill='ノアのはこぶね')
    G.add_edge('そうりょ', 'ひつじかい', skill='スクルト')
    G.add_edge('とうぞく', 'せんし', skill='ぬすっと斬り')
    G.add_edge('とうぞく', 'ぶとうか', skill='きゅうしょ突き')
    G.add_edge('とうぞく', 'まほうつかい', skill='マホトラ')
    G.add_edge('とうぞく', 'おどりこ', skill='マホトラおどり')
    G.add_edge('とうぞく', 'わらわせし', skill='しのび笑い')
    G.add_edge('おどりこ', 'せんし', skill='つるぎのまい')
    G.add_edge('おどりこ', 'ぶとうか', skill='マッスルダンス')
    G.add_edge('おどりこ', 'まほうつかい', skill='マホキテ')
    G.add_edge('おどりこ', 'そうりょ', skill='死のおどり')
    G.add_edge('おどりこ', 'とうぞく', skill='マホトラおどり')
    G.add_edge('おどりこ', 'ふなのり', skill='船上ダンス')
    G.add_edge('おどりこ', 'ひつじかい', skill='ひつじのダンス')
    G.add_edge('おどりこ', 'わらわせし', skill='ステテコダンス')
    G.add_edge('ぎんゆうしじん', 'せんし', skill='たたかいの歌')
    G.add_edge('ぎんゆうしじん', 'ぶとうか', skill='おたけび')
    G.add_edge('ぎんゆうしじん', 'まほうつかい', skill='のろいの歌')
    G.add_edge('ぎんゆうしじん', 'そうりょ', skill='やすらぎの歌')
    G.add_edge('ぎんゆうしじん', 'ふなのり', skill='さざなみの歌')
    G.add_edge('ぎんゆうしじん', 'ひつじかい', skill='ひつじかぞえ歌')
    G.add_edge('ぎんゆうしじん', 'わらわせし', skill='コミックソング')
    G.add_edge('ふなのり', 'せんし', skill='かもめ返し')
    G.add_edge('ふなのり', 'ぶとうか', skill='すいめんげり')
    G.add_edge('ふなのり', 'まほうつかい', skill='いなずま')
    G.add_edge('ふなのり', 'そうりょ', skill='ノアのはこぶね')
    G.add_edge('ふなのり', 'おどりこ', skill='船上ダンス')
    G.add_edge('ふなのり', 'ぎんゆうしじん', skill='さざなみの歌')
    G.add_edge('ひつじかい', 'せんし', skill='みねうち')
    G.add_edge('ひつじかい', 'ぶとうか', skill='マトンアタック')
    G.add_edge('ひつじかい', 'まほうつかい', skill='ラリホーマ')
    G.add_edge('ひつじかい', 'そうりょ', skill='スクルト')
    G.add_edge('ひつじかい', 'おどりこ', skill='ひつじのダンス')
    G.add_edge('ひつじかい', 'ぎんゆうしじん', skill='ひつじかぞえ歌')
    G.add_edge('わらわせし', 'せんし', skill='へんてこ斬り')
    G.add_edge('わらわせし', 'ぶとうか', skill='しっぺ返し')
    G.add_edge('わらわせし', 'まほうつかい', skill='メダパニ')
    G.add_edge('わらわせし', 'とうぞく', skill='しのび笑い')
    G.add_edge('わらわせし', 'おどりこ', skill='ステテコダンス')
    G.add_edge('わらわせし', 'ぎんゆうしじん', skill='コミックソング')
    #G.add_edge('けんじゃ', 'スーパースター', skill='メガザルダンス')

    if nx.is_eulerian(G):
        print_cycle(G)

    G.remove_edge('ぎんゆうしじん', 'ぶとうか')
    G.remove_edge('まほうつかい', 'とうぞく')
    print_cycle(G, source='まほうつかい')

def print_cycle(G, source=None):
    """Print an Eulerian cycle in G.

    Args:
      source: Starting node for circuit.

    Returns:
      None
    """

    skills = nx.get_edge_attributes(G, 'skill')
    try:
        for i in nx.eulerian_circuit(G, source):
            if i in skills:
                skill = skills[i]
            else:
                skill = skills[(i[1], i[0])]
            print('{} {}'.format(i, skill))
    except nx.NetworkXError as e:
        print(e)

if __name__ == '__main__':
    main()
