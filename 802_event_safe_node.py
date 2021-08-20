from collections import defaultdict


def eventualSafeNodes(graph):
    reachs = defaultdict(list)
    empty = list()
    for index, item in enumerate(graph):
        if not item:
            empty.append(index)
            continue
        for i in item:
            reachs[i].append(index)
    resp = list()
    for i in range(len(graph)):
        seen = set()
        
    
            


if __name__ == '__main__':
    print(eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))
    