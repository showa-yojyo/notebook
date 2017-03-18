#!/usr/bin/env python
"""eulerian.py: demonstrate NetworkX is_eulerian and eulerian_circuit.

Compute the most efficient career path in DRAGON QUEST 7 (2000).
"""
import networkx as nx

def main():
    """The main function.

    Returns:
      None
    """

    G = nx.Graph()
    G.add_edges_from((
        ('せんし', 'とうぞく', dict(skill='ぬすっと斬り')),
        ('せんし', 'おどりこ', dict(skill='つるぎのまい')),
        ('せんし', 'ぎんゆうしじん', dict(skill='たたかいの歌')),
        ('せんし', 'ふなのり', dict(skill='かもめ返し')),
        ('せんし', 'ひつじかい', dict(skill='みねうち')),
        ('せんし', 'わらわせし', dict(skill='へんてこ斬り')),
        ('ぶとうか', 'まほうつかい', dict(skill='火の息')),
        ('ぶとうか', 'とうぞく', dict(skill='きゅうしょ突き')),
        ('ぶとうか', 'おどりこ', dict(skill='マッスルダンス')),
        ('ぶとうか', 'ぎんゆうしじん', dict(skill='おたけび')),
        ('ぶとうか', 'ふなのり', dict(skill='すいめんげり')),
        ('ぶとうか', 'ひつじかい', dict(skill='マトンアタック')),
        ('ぶとうか', 'わらわせし', dict(skill='しっぺ返し')),
        ('まほうつかい', 'ぶとうか', dict(skill='火の息')),
        ('まほうつかい', 'とうぞく', dict(skill='マホトラ')),
        ('まほうつかい', 'おどりこ', dict(skill='マホキテ')),
        ('まほうつかい', 'ぎんゆうしじん', dict(skill='のろいの歌')),
        ('まほうつかい', 'ふなのり', dict(skill='いなずま')),
        ('まほうつかい', 'ひつじかい', dict(skill='ラリホーマ')),
        ('まほうつかい', 'わらわせし', dict(skill='メダパニ')),
        ('そうりょ', 'おどりこ', dict(skill='死のおどり')),
        ('そうりょ', 'ぎんゆうしじん', dict(skill='やすらぎの歌')),
        ('そうりょ', 'ふなのり', dict(skill='ノアのはこぶね')),
        ('そうりょ', 'ひつじかい', dict(skill='スクルト')),
        ('とうぞく', 'せんし', dict(skill='ぬすっと斬り')),
        ('とうぞく', 'ぶとうか', dict(skill='きゅうしょ突き')),
        ('とうぞく', 'まほうつかい', dict(skill='マホトラ')),
        ('とうぞく', 'おどりこ', dict(skill='マホトラおどり')),
        ('とうぞく', 'わらわせし', dict(skill='しのび笑い')),
        ('おどりこ', 'せんし', dict(skill='つるぎのまい')),
        ('おどりこ', 'ぶとうか', dict(skill='マッスルダンス')),
        ('おどりこ', 'まほうつかい', dict(skill='マホキテ')),
        ('おどりこ', 'そうりょ', dict(skill='死のおどり')),
        ('おどりこ', 'とうぞく', dict(skill='マホトラおどり')),
        ('おどりこ', 'ふなのり', dict(skill='船上ダンス')),
        ('おどりこ', 'ひつじかい', dict(skill='ひつじのダンス')),
        ('おどりこ', 'わらわせし', dict(skill='ステテコダンス')),
        ('ぎんゆうしじん', 'せんし', dict(skill='たたかいの歌')),
        ('ぎんゆうしじん', 'ぶとうか', dict(skill='おたけび')),
        ('ぎんゆうしじん', 'まほうつかい', dict(skill='のろいの歌')),
        ('ぎんゆうしじん', 'そうりょ', dict(skill='やすらぎの歌')),
        ('ぎんゆうしじん', 'ふなのり', dict(skill='さざなみの歌')),
        ('ぎんゆうしじん', 'ひつじかい', dict(skill='ひつじかぞえ歌')),
        ('ぎんゆうしじん', 'わらわせし', dict(skill='コミックソング')),
        ('ふなのり', 'せんし', dict(skill='かもめ返し')),
        ('ふなのり', 'ぶとうか', dict(skill='すいめんげり')),
        ('ふなのり', 'まほうつかい', dict(skill='いなずま')),
        ('ふなのり', 'そうりょ', dict(skill='ノアのはこぶね')),
        ('ふなのり', 'おどりこ', dict(skill='船上ダンス')),
        ('ふなのり', 'ぎんゆうしじん', dict(skill='さざなみの歌')),
        ('ひつじかい', 'せんし', dict(skill='みねうち')),
        ('ひつじかい', 'ぶとうか', dict(skill='マトンアタック')),
        ('ひつじかい', 'まほうつかい', dict(skill='ラリホーマ')),
        ('ひつじかい', 'そうりょ', dict(skill='スクルト')),
        ('ひつじかい', 'おどりこ', dict(skill='ひつじのダンス')),
        ('ひつじかい', 'ぎんゆうしじん', dict(skill='ひつじかぞえ歌')),
        ('わらわせし', 'せんし', dict(skill='へんてこ斬り')),
        ('わらわせし', 'ぶとうか', dict(skill='しっぺ返し')),
        ('わらわせし', 'まほうつかい', dict(skill='メダパニ')),
        ('わらわせし', 'とうぞく', dict(skill='しのび笑い')),
        ('わらわせし', 'おどりこ', dict(skill='ステテコダンス')),
        ('わらわせし', 'ぎんゆうしじん', dict(skill='コミックソング')),
        #('けんじゃ', 'スーパースター', dict(skill='メガザルダンス')),
        ))

    if nx.is_eulerian(G):
        print_cycle(G)

    G.remove_edge('ぎんゆうしじん', 'ぶとうか')
    G.remove_edge('まほうつかい', 'とうぞく')
    print_cycle(G, source='まほうつかい')

def print_cycle(G, source=None):
    """Print an Eulerian cycle in G.

    Args:
      G: A Graph.
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
    except nx.NetworkXError as ex:
        print(ex)

if __name__ == '__main__':
    main()
