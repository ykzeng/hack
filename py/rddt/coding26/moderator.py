import collections
from typing import List, Dict


class ModeratorSystem:
    """
    Coding 3 — Moderator List System

    Requirements:

    Part 1:
        - Parse logs
        - can_remove_mod(user1, user2)
        - get_mod_list()

    Part 2:
        - Support multiple communities

    Part 3:
        - demote(user)

    Logs format (example):
        "community | user1,user2 | added | user3 | 123.0"

    Meaning:
        At timestamp 123.0,
        user3 performed action "added"
        on user1,user2
        inside that community.
    """

    def __init__(self, logs: List[str]):
        """
        Parse logs and build moderator state.

        You likely need:
            self.mods_by_community
        Structure suggestion:
            {
                community: {
                    user: timestamp_joined
                }
            }
        """
        # TODO:
        # self.mods_by_community = ...
        self.mod_list=collections.defaultdict(list)
        self.join_time=collections.defaultdict(dict)
        for line in logs:
            comm,new_mod_list,action,ts=line.split('|')
            ts=float(ts)
            # print(comm,new_mod_list,action,mod,ts)
            if action=="added":
                new_mod_list=new_mod_list.split(',')
                for new_mod in new_mod_list:
                    self.join_time[comm][new_mod]=ts
                    self.mod_list[comm].append((ts,new_mod))
        for comm in self.mod_list:
            self.mod_list[comm]=sorted(self.mod_list[comm],key=lambda x:x[0])
        # self.mod_list=

    # --------------------------------------------------
    # Part 1 — Remove Check
    # --------------------------------------------------
    def can_remove_mod(self,
                       community: str,
                       acting_user: str,
                       target_user: str) -> bool:
        """
        Return True if acting_user can remove target_user.

        Rule:
            target_user must have joined later than acting_user.

        i.e.
            join_time[acting_user] < join_time[target_user]
        """
        # print(self.join_time)
        if self.join_time[community][acting_user]<self.join_time[community][target_user]:
            return True
        else: 
            return False

    # --------------------------------------------------
    # Part 1 — Get Moderator List
    # --------------------------------------------------
    def get_mod_list(self,
                     community: str) -> List[str]:
        """
        Return moderator list ordered by join timestamp ascending.
        """
        return [mod for ts,mod in self.mod_list[community]]

    # --------------------------------------------------
    # Part 3 — Demote
    # --------------------------------------------------
    def demote(self,
               community: str,
               user: str) -> None:
        """
        Demote a moderator.

        Example:
            [u1, u2, u3]
            demote(u1)
            -> [u2, u1, u3]

        Hint:
            You probably need to update priority/timestamp.
        """
        # this should find the first moderator
        # added after the target ts
        def bsearch(community_list,target):
            lo,hi=0,len(community_list)
            while lo<hi:
                mid=(lo+hi)//2
                cur_ts=community_list[mid][0]
                if cur_ts<=target:
                    lo=mid+1
                elif cur_ts>target:
                    hi=mid
            return lo
        community_mod_list=self.mod_list[community]
        community_join_time=self.join_time[community]

        target=community_join_time[user]
        idx=bsearch(community_mod_list,target)
        next_mod=community_mod_list[idx][1]
        next_ts=community_join_time[next_mod]
        next_next_idx=bsearch(community_mod_list,next_ts)
        community_join_time[user]=next_ts+0.1

        community_mod_list=community_mod_list[]
        community_mod_list=community_mod_list[:next_next_idx]
        pass


# Single community "general" only; checks are can_remove and/or get_mod_list.
TEST_CASES = [
    {
        "name": "two-line adds: can_remove u1->u3 + get_mod_list order",
        "logs": [
            "general|u1,u2|added|1.0",
            "general|u3|added|2.0",
        ],
        "checks": [
            ("can_remove", "general", "u1", "u3", True),
            ("get_mod_list", "general", ["u1", "u2", "u3"]),
        ],
    },
    {
        "name": "two-line adds: can_remove u3->u1 + get_mod_list order",
        "logs": [
            "general|u1,u2|added|1.0",
            "general|u3|added|2.0",
        ],
        "checks": [
            ("can_remove", "general", "u3", "u1", False),
            ("get_mod_list", "general", ["u1", "u2", "u3"]),
        ],
    },
    {
        "name": "single-line add: non-mod can_remove + get_mod_list",
        "logs": [
            "general|u1,u2|added|1.0",
        ],
        "checks": [
            ("can_remove", "general", "u3", "u2", KeyError),
            ("get_mod_list", "general", ["u1", "u2"]),
        ],
    },
    {
        "name": "single mod: get_mod_list",
        "logs": [
            "general|only|added|5.0",
        ],
        "checks": [
            ("get_mod_list", "general", ["only"]),
        ],
    },
]

# =====================================================
#                Generalized Test Runner
# =====================================================

# Test logs must match what ModeratorSystem.__init__ parses:
#   community|targets|action|timestamp
# Example: general|u1,u2|added|1.0


def run_tests():
    """
    Builds ModeratorSystem(test['logs']) so __init__ and downstream methods
    are exercised; no injected join_time.

    If can_remove_mod does not treat missing moderators as False, the expected
    value may be an exception type (e.g. KeyError) instead of bool.

    get_mod_list checks compare the returned list to the expected ordering
    (join timestamp ascending per the problem statement).
    """
    test_cases=TEST_CASES

    for test in test_cases:
        print("\n==============================")
        print("Test:", test["name"])

        test_passed = True
        function_stats: Dict[str, Dict[str, int]] = {}

        system = ModeratorSystem(test["logs"])

        for check in test["checks"]:
            action = check[0]
            function_stats.setdefault(action, {"pass": 0, "fail": 0})

            try:
                if action == "can_remove":
                    _, community, acting, target, expected = check
                    if isinstance(expected, type) and issubclass(
                        expected, BaseException
                    ):
                        try:
                            system.can_remove_mod(community, acting, target)
                        except expected:
                            print(
                                f"[PASS] can_remove({acting}->{target}) "
                                f"raised {expected.__name__}"
                            )
                            function_stats[action]["pass"] += 1
                        except Exception as e:
                            test_passed = False
                            function_stats[action]["fail"] += 1
                            print(
                                f"[FAIL] can_remove({acting}->{target}) "
                                f"raised {type(e).__name__}, "
                                f"expected {expected.__name__}"
                            )
                        else:
                            test_passed = False
                            function_stats[action]["fail"] += 1
                            print(
                                f"[FAIL] can_remove({acting}->{target}) "
                                f"did not raise {expected.__name__}"
                            )
                    else:
                        result = system.can_remove_mod(
                            community, acting, target
                        )
                        if result == expected:
                            print(
                                f"[PASS] can_remove({acting}->{target}) = "
                                f"{result}"
                            )
                            function_stats[action]["pass"] += 1
                        else:
                            test_passed = False
                            function_stats[action]["fail"] += 1
                            print(
                                f"[FAIL] can_remove({acting}->{target}) = "
                                f"{result} (expected {expected})"
                            )

                elif action == "get_mod_list":
                    _, community, expected = check
                    result = system.get_mod_list(community)
                    if result == expected:
                        print(f"[PASS] get_mod_list({community}) = {result}")
                        function_stats[action]["pass"] += 1
                    else:
                        test_passed = False
                        function_stats[action]["fail"] += 1
                        print(
                            f"[FAIL] get_mod_list({community}) = {result} "
                            f"(expected {expected})"
                        )

                elif action == "demote":
                    _, community, user = check
                    system.demote(community, user)
                    print(f"[PASS] demote({user}) done")
                    function_stats[action]["pass"] += 1

                else:
                    raise ValueError(f"Unknown action: {action}")
            except Exception as e:
                test_passed = False
                function_stats[action]["fail"] += 1
                print(f"[FAIL] {action}{check[1:]} -> {e}")

        print("Function summary:")
        for func_name, stats in function_stats.items():
            total = stats["pass"] + stats["fail"]
            status = "PASS" if stats["fail"] == 0 else "FAIL"
            print(
                f"  {func_name}: {status} "
                f"({stats['pass']}/{total} passed, {stats['fail']} failed)"
            )

        print(f"Test result: {'PASS' if test_passed else 'FAIL'}")


if __name__ == "__main__":
    run_tests()