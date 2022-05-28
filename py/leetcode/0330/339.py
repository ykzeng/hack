# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class Solution1:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        # print(nestedList)
        # print(type(nestedList))
        # print(type(nestedList[0]))
        # print(nestedList[0].isInteger())
        # print(type(nestedList[0].getList()))
        self.res = 0
        for ni in nestedList:
            self.weightSum(1, ni)
        return self.res

    def weightSum(self, depth, lst):
        # if type(lst) == list:
        #     for ni in lst:
        #         self.weightSum(depth+1, ni)
        if lst.isInteger():
            self.res += lst.getInteger() * depth
        else:
            for ni in lst.getList():
                self.weightSum(depth + 1, ni)


class Solution2:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        queue = nestedList
        res, depth = 0, 1
        while queue:
            res += sum([ni.getInteger() for ni in queue if ni.isInteger()]) * depth
            # efficient
            queue = [x.getList() for x in queue if not x.isInteger()]
            queue = [ni for lst in queue for ni in lst]
            # monoid trick
            # queue = sum([x.getList() for x in queue if not x.isInteger()],[])
            depth += 1
        return res
