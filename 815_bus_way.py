from collections import defaultdict, deque


# BFS
def bus(routes, source, target):
    # 每个车站可以乘坐的公交线路
    sites = defaultdict(set)
    if source == target:
        return 0
    for line, item in enumerate(routes):
        for site in item:
            sites[site].add(line)
    # 每个线路可以去的车站
    routes = [set(x) for x in routes]
    
    q = deque([(source, 0)])
    # 已经乘坐的公交
    buses = set()
    # 已经去过的车站
    targets = {source}
    while q:
        site, changes = q.popleft()
        if site == target:
            return changes
        # 每个车站没有去过的公交车
        for bus in sites[site] - buses:
            # 每个公交车没有去过的车站
            buses.add(bus)
            for new_site in routes[bus] - targets:
                targets.add(new_site)
                q.append((site, changes+1))
    return -1

    
    