from typing import List, Tuple, Dict, Set
from collections import defaultdict
from unittest import skip

class ReportChain:
    def __init__(self, relations: List[str]):
        """
        Input example:
            ['A,B,C', 'C,D', 'B,E']

        Each string means:
            manager, employee1, employee2, ...

        Tasks:
            - Build children mapping
            - Build parent mapping
            - Detect root
        """
        # TODO:
        # self.children = ...
        # self.parent = ...
        # self.root = ...
        self.manages=defaultdict(list)
        self.report_to=defaultdict(str)
        for r in relations:
            mgr=r.split(',')[0]
            rep=r.split(',')[1:]
            self.manages[mgr].extend(rep)
            for x in rep:
                self.report_to[x]=mgr

    def dfs(self, x,depth):
        print(depth*"...."+x)
        if not self.manages[x]:
            return
        for r in self.manages[x]:
            self.dfs(r,depth+1)

    def get_ceo(self):
        ceo=next(iter(self.report_to))
        while ceo in self.report_to:
            ceo=self.report_to[ceo]
        return ceo

    # -----------------------------------------------------
    # Part 1 — Print Tree
    # -----------------------------------------------------
    def print_tree(self) -> None:
        """
        Print full hierarchy tree.

        Example output:
            A
            ....B
            ........E
            ....C
            ........D
        """
        # find the ceo
        ceo=self.get_ceo()
        self.dfs(ceo,0)

    # -----------------------------------------------------
    # Part 2 — Skip-Level Pairs
    # -----------------------------------------------------
    def get_skip_level_pairs(self) -> List[Tuple[str, str]]:
        """
        Return all (ancestor, descendant) pairs
        where they are NOT direct manager relationship
        (at least 2 levels apart)

        Example:
            [('A','E'), ('A','D')]
        """
        ceo=self.get_ceo()
        p=ceo
        def skip_level(p):
            if p not in self.manages:
                return
            skip=[]
            for direct in self.manages[p]:
                if direct in self.manages:
                    skip.extend(self.manages[direct])
                skip_level(direct)
            if skip:
                ans[p]=[(p,s) for s in skip]
        ans={}
        skip_level(p)
        # print(ans)
        for _,pair in ans.items():
            print(pair)


    # -----------------------------------------------------
    # Part 3 — Query person's full chain
    # -----------------------------------------------------
    def get_full_chain(self, person: str) -> None:
        """
        Print:
            - All managers above (single chain upward)
            - Full subtree below this person

        Example for B:
            A
            ....B
            ........E
        """
        higher,lower=[],[]
        p=person
        while p in self.report_to:
            p=self.report_to[p]
            higher.append(p)
        for i,p in enumerate(higher[::-1]):
            print(i*"...."+p)
        self.dfs(person,len(higher))

    # -----------------------------------------------------
    # Part 4 — Lowest Common Manager
    # -----------------------------------------------------
    def lowest_common_manager(self, p1: str, p2: str) -> str:
        """
        Return the lowest common ancestor (manager)
        of p1 and p2.

        Example:
            C and E -> A
        """
        pp1,pp2=p1,p2
        while pp1!=pp2:
            pp1=self.report_to[pp1] if pp1 in self.report_to else p2
            pp2=self.report_to[pp2] if pp2 in self.report_to else p1
        return pp1


# =========================================================
#                    TEST CASES
# =========================================================

TEST_CASES = [
    {
        "name": "Basic Tree",
        "relations": ['A,B,C', 'C,D', 'B,E'],
        "query_person": "B",
        "lca_pair": ("C", "E"),
    },
    {
        "name": "Corporate Hierarchy",
        "relations": ['CEO,VP1,VP2', 'VP1,Mgr1,Mgr2', 'Mgr1,Dev1', 'VP2,Mgr3'],
        "query_person": "VP1",
        "lca_pair": ("Dev1", "Mgr2"),
    },
    {
        "name": "Linear Chain",
        "relations": ['A,B', 'B,C', 'C,D', 'D,E'],
        "query_person": "C",
        "lca_pair": ("D", "E"),
    },
]


def run_test(test_case: dict) -> None:
    """Run all tests for a single test case configuration."""
    name = test_case["name"]
    relations = test_case["relations"]
    query_person = test_case["query_person"]
    lca_pair = test_case["lca_pair"]

    print(f"=== {name} ===")
    print(f"Relations: {relations}")
    rc = ReportChain(relations)

    # print("\n--- Print Tree ---")
    # rc.print_tree()

    print("\n--- Skip Level Pairs ---")
    # print()
    rc.get_skip_level_pairs()

    # print(f"\n--- Query {query_person} ---")
    # rc.get_full_chain(query_person)

    # print(f"\n--- LCA of {lca_pair[0]} and {lca_pair[1]} ---")
    # print(rc.lowest_common_manager(lca_pair[0], lca_pair[1]))
    # print()


if __name__ == "__main__":
    for test_case in TEST_CASES:
        run_test(test_case)
        print("-" * 50)
        print()