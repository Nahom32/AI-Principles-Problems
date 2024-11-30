from collections import defaultdict
def bfs(pattern_graph, begin_word, end_word):
    '''
        This bfs implementation calculates the number of steps required from begin word to end word 
        transformation
    '''
    visited = set()
    queue = [(begin_word,1)]
    while queue:
        curr_word, steps = queue.pop(0)
        for i in range(len(curr_word)):
            pattern = curr_word[:i] + '*' + curr_word[i+1:]
            for neighbor in pattern_graph[pattern]:
                if neighbor == end_word:
                    return steps + 1
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor,steps+1))
    return 0

def perform_word_ladder(begin_word, end_word, word_list):
    '''
    This procedure performs a pattern graph and gives it to the bfs procedure.
    '''
    word_set = set(word_list)
    neighbors = defaultdict(list)
    if end_word not in word_set:
        return 0
    for word in word_set:
        for i in range(len(begin_word)):
            neighbors[word[:i] + '*' + word[i+1:]].append(word)
    result = bfs(neighbors,begin_word,end_word)
    return result
print(perform_word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
    


