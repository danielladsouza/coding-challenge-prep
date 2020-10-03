# EPI 18.0
"""
Given a list of outcomes of matches between pairs of teams, with each outcome being a win or a loss,
Can team A beat B i.e. is there a sequence of teams starting with A and ending with B such that each team in the sequence 
has beaten the next team in the sequence?
Graph - A -> C -> D -> E -> F -> B
matches - [(A,C), (C,D), (E,F), (F,B)]

We will implement the graph using adjacency lists.
"""
from collections import namedtuple
from collections import defaultdict

MatchResult = namedtuple('MatchResult',
                                     ('winning_team', 'losing_team'))

def can_team_a_beat_team_b(matches, team_a, team_b):

    # 1 Build the graph using adjacency lists
    def build_graph():
        graph = defaultdict(set)
        for match in matches:
            graph[match.winning_team].add(match.losing_team)
        return graph

    def is_reachable_dfs(graph, curr, dest, visited=set()):
        if curr == dest:
            return True
        # This is a cycle
        # We reached a sink and cannot proceed.. no path forward
        elif curr in visited or curr not in graph:
            return False
        visited.add(curr)
        return any(is_reachable_dfs(graph, team, dest) for team in graph[curr])


    return is_reachable_dfs(build_graph(), team_a, team_b)

matches = []
matches.append(MatchResult('A','C'))
matches.append(MatchResult('C','D'))
matches.append(MatchResult('D','E'))
#matches.append(MatchResult('D','A'))
matches.append(MatchResult('E','F'))
matches.append(MatchResult('F','B'))


result = can_team_a_beat_team_b(matches, 'A', 'B')
print(result)


