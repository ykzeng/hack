def lowestCommonAncestor(self, p: "Node", q: "Node") -> "Node":
    panc = self.findAncestor(p)
    qanc = self.findAncestor(q)
    l = min(len(panc), len(qanc))
    for i in range(l):
        if panc[i].val != qanc[i].val:
            return panc[i - 1]
        elif i == l - 1:
            return panc[i]


def findAncestor(self, node):
    p = node
    res = collections.deque([])
    while p:
        res.appendleft(p)
        p = p.parent
    return res


def lowestCommonAncestor(self, p: "Node", q: "Node") -> "Node":
    tp, tq = p, q
    while tp != tq:
        tp = tp.parent if tp.parent else q
        tq = tq.parent if tq.parent else p
    return tp
