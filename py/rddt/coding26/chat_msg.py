from __future__ import annotations

from dataclasses import dataclass
from typing import List


# =====================================================
# Domain model
# =====================================================

@dataclass(frozen=True)
class ChatMessage:
    """One chat line: stable id plus body text."""

    message_id: int
    content: str


# =====================================================
# Mock Chat Store
# =====================================================

class ChatStore:
    """
    Simple message store (no versioning).
    Messages are sorted by message_id; each row is a ChatMessage.
    """

    def __init__(self, messages: List[ChatMessage]):
        self.messages: List[ChatMessage] = sorted(
            messages, key=lambda m: m.message_id
        )
        self.id_to_index = {
            m.message_id: i for i, m in enumerate(self.messages)
        }

    def get_chat_messages(self, message_id: int) -> List[ChatMessage]:
        """
        Return window of message_id ± 2 (by index in sorted list).
        Each item is a ChatMessage. Sorted by message_id.
        """
        if message_id not in self.id_to_index:
            return []

        idx = self.id_to_index[message_id]
        left = max(0, idx - 2)
        right = min(len(self.messages), idx + 3)

        return self.messages[left:right]


# =====================================================
# YOU IMPLEMENT THIS
# =====================================================

class ChatMerger:

    def __init__(self, store: ChatStore):
        self.store = store

    def merge_messages(self, ids: List[int]) -> List[ChatMessage]:
        """
        Requirements:
            - For each id call get_chat_messages
            - Merge all sorted lists (by message id)
            - Remove duplicates (same id appears once; content must match)
            - Return sorted list of ChatMessage
            - ❗Do NOT use set()

        Hint:
            Merge K sorted lists; deduplicate during merge (e.g. min-heap).
        """
        import heapq
        ans=[]
        heap=[]
        lists=[self.store.get_chat_messages(i) for i in ids]
        cnt=0
        for l in lists:
            first_msg=l[0]
            heapq.heappush(heap,(first_msg.message_id,cnt,0,l))
            cnt+=1
        while heap:
            message_id,cnt,ix,l=heapq.heappop(heap)
            if not ans or message_id!=ans[-1].message_id:
                ans.append(l[ix])
            if ix+1<len(l):
                next_msg=l[ix+1]
                heapq.heappush(heap,(next_msg.message_id,cnt,ix+1,l))
        return ans


# =====================================================
# Human-like conversation (ids 1–20) for tests
# =====================================================

def build_sample_conversation() -> List[ChatMessage]:
    """A short team thread about a PR and follow-up work."""
    lines = [
        (1, "Sam: Hey, did anyone get eyes on the auth PR yet?"),
        (2, "Alex: Started reviewing it this morning."),
        (3, "Sam: Nice — anything blocking you?"),
        (4, "Alex: Just CI; I'll ping if it goes red."),
        (5, "Jordan: I can do a second pass if that helps."),
        (6, "Sam: Yes please, thanks Jordan."),
        (7, "Alex: CI is green now."),
        (8, "Jordan: On it — I'll leave comments on the diff."),
        (9, "Sam: Perfect, appreciate it."),
        (10, "Alex: Left a few nits; nothing major."),
        (11, "Jordan: Replied on the token refresh thread."),
        (12, "Sam: Cool — I'll merge once you two are good."),
        (13, "Alex: Ship it from my side."),
        (14, "Jordan: Same here 👍"),
        (15, "Sam: Merged. Thanks everyone."),
        (16, "Taylor: Just caught up — nice turnaround."),
        (17, "Alex: Haha, we try."),
        (18, "Sam: Next: tighter error handling on login?"),
        (19, "Taylor: I can take that; will spike tomorrow."),
        (20, "Sam: Works for me — let's sync at standup."),
    ]
    return [ChatMessage(mid, text) for mid, text in lines]


def format_messages(msgs: List[ChatMessage]) -> str:
    return "\n".join(f"  [{m.message_id}] {m.content}" for m in msgs)


def _ids(msgs: List[ChatMessage]) -> List[int]:
    return [m.message_id for m in msgs]


# =====================================================
# Generalized Test Runner — exercises ChatMerger.merge_messages
# =====================================================

def run_tests():
    """
    Calls ChatMerger.merge_messages for each case. Implement merge_messages
    to satisfy expected_ids (merge returns None until you add a return value).
    """
    all_messages = build_sample_conversation()

    test_cases = [
        # {
        #     "name": "Single anchor — one window (same as get_chat_messages(10))",
        #     "input_ids": [10],
        #     "expected_ids": [8, 9, 10, 11, 12],
        # },
        {
            "name": "Overlapping anchors — dedupe shared messages",
            "input_ids": [8, 10, 12],
            "expected_ids": list(range(6, 15)),
        },
        {
            "name": "Far apart anchors — stitch three windows in order",
            "input_ids": [3, 10, 18],
            "expected_ids": [
                1, 2, 3, 4, 5,
                8, 9, 10, 11, 12,
                16, 17, 18, 19, 20,
            ],
        },
    ]

    for test in test_cases:
        print("\n==============================")
        print("Test:", test["name"])

        store = ChatStore(all_messages)
        merger = ChatMerger(store)

        result = merger.merge_messages(test["input_ids"])
        if result is None:
            got_ids = None
            print("Input anchor IDs:", test["input_ids"])
            print("merge_messages returned None (implement and return List[ChatMessage])")
        else:
            got_ids = _ids(result)
            print("Input anchor IDs:", test["input_ids"])
            print("merge_messages result:")
            print(format_messages(result))

        expected = test["expected_ids"]
        print("Expected IDs:", expected)
        print("Got IDs:     ", got_ids)
        ok = got_ids == expected
        print("Test result:", "PASS" if ok else "FAIL")


if __name__ == "__main__":
    run_tests()
