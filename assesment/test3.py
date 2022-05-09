def ShortestPath(strArr):

    va = int(strArr[0])
    v = strArr[1:va+1]
    ed = strArr[va+1:]
    gh = {}

    for node in v:
        gh[node] = set()

    for e in ed:
        v1, v2 = e.split('-')
        gh[v1].add(v2)
        gh[v2].add(v1)

    def deepFirstSearch(g, start, goal):
        res = []
        stk = [(start, [start])]
        while stk:
            (ve, path) = stk.pop()
            if ve in g:
                try:
                    for psn in (g[ve]-set(path)):
                        if psn == goal:
                            res.append("-".join(path + [psn]))
                        else:
                            stk.append((psn, path+[[psn]]))
                except (TypeError):
                    continue
        return res

    out = deepFirstSearch(gh, v[0], v[-1])

    return -1 if out == [] else sorted(out, key=len)[0]


# keep this function call here
print(ShortestPath(["5", "A", "B", "C", "D",
      "F", "A-B", "A-C", "B-C", "C-D", "D-F"]))
