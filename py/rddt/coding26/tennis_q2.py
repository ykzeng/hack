"""
Tennis Q2: single-game logic lives in tennis_q1.Game; this module adds a
tournament layer (first to 3 match wins). Tournament behavior is not
implemented here — only API stubs and tests / runners.

Tournament tests use one flat `wins` list (like Q1). Completed games are
written as mixed rally sequences — not four straight holds (e.g. ABABAA,
BABABB) — whenever a full game is intended.
"""

from __future__ import annotations
from tennis_q1 import Game

from tennis_q1 import run_all_tests as run_game_tests

GAMES_TO_WIN = 3

class Tournament:
    """
    Best-of-match-wins: the player who wins 3 games first wins the tournament.
    Implementation intentionally omitted; methods raise until filled in.
    """

    def __init__(self) -> None:
        """Construct tournament state; subclass / implementation fills fields."""
        self.games=[Game()]
        self.player1=self.player2=0
        self.idx=0

    def record_point(self, player: str) -> str | None:
        """
        Record one point for the current game (same idea as Game.increaseScore).
        When a game completes, count a match win and start the next game until
        the tournament has a winner. Returns match winner if a game just ended,
        else None; may also return early if the tournament was already decided.
        """
        if self.get_tournament_winner() is not None:
            return
        active_game=self.games[self.idx]
        active_game.increaseScore(player)
        winner=active_game.getWinner()
        if winner:
            if winner=="A": self.player1+=1
            elif winner=="B": self.player2+=1
            self.idx+=1
            self.games.append(Game())

    def get_match_wins(self) -> tuple[int, int]:
        """Cumulative match wins (A_wins, B_wins)."""
        return self.player1,self.player2

    def get_tournament_winner(self) -> str | None:
        """Return 'A', 'B', or None if the tournament is still open."""
        if self.player1>=3:
            return "A"
        elif self.player2>=3:
            return "B"
        else:
            return None


def run_tournament_test_case(
    test_case_id: int,
    wins: list[str],
    expected_match_wins: tuple[int, int],
    expected_tournament_winner: str | None,
) -> None:
    tournament = Tournament()

    for player in wins:
        tournament.record_point(player)

    actual_match_wins = tournament.get_match_wins()
    actual_tournament_winner = tournament.get_tournament_winner()

    print(f"\n[Tournament] Test Case {test_case_id}")
    print(f"wins length: {len(wins)}")
    print(f"Expected match wins: {expected_match_wins}, actual: {actual_match_wins}")
    print(
        f"Expected tournament winner: {expected_tournament_winner!r}, "
        f"actual: {actual_tournament_winner!r}"
    )

    assert actual_match_wins == expected_match_wins, (
        f"Match wins mismatch in tournament test {test_case_id}"
    )
    assert actual_tournament_winner == expected_tournament_winner, (
        f"Tournament winner mismatch in tournament test {test_case_id}"
    )


def run_tournament_tests() -> None:
    # Mixed one-game patterns (each ends as soon as Game awards a winner):
    #   ABABAA, A,B,A,A,A  → A wins (not a straight run of four A's)
    #   BABABB, B,A,B,B,B  → B wins
    tournament_test_cases: list[dict] = [
        {
            "id": 1,
            "wins": [
                *list("ABABAA"),
                *["A", "B", "A", "A", "A"],
                *list("ABABAABA"),  # same game as ABABAA; trailing BA are post-game
            ],
            "expected_match_wins": (3, 0),
            "expected_tournament_winner": "A",
        },
        {
            "id": 2,
            "wins": [
                *list("ABABAA"),
                *list("BABABB"),
                *["A", "B", "A", "A", "A"],
                *list("BABABB"),
                *list("ABABAA"),
            ],
            "expected_match_wins": (3, 2),
            "expected_tournament_winner": "A",
        },
        {
            "id": 3,
            "wins": [
                *list("BABABB"),
                *["B", "A", "B", "B", "B"],
                *list("BABABB"),
            ],
            "expected_match_wins": (0, 3),
            "expected_tournament_winner": "B",
        },
        {
            "id": 4,
            "wins": [
                *list("ABABAA"),
                *list("BABABB"),
                *["A", "B", "A", "A", "A"],
                "A",
                "A",
                "B",
            ],
            "expected_match_wins": (2, 1),
            "expected_tournament_winner": None,
        },
        {
            "id": 5,
            "wins": [
                *list("ABABAA"),
                *["A", "B", "A", "A", "A"],
                *list("ABABAA"),
                *list("BABABB"),
            ],
            "expected_match_wins": (3, 0),
            "expected_tournament_winner": "A",
        },
    ]

    for tc in tournament_test_cases:
        run_tournament_test_case(
            tc["id"],
            tc["wins"],
            tc["expected_match_wins"],
            tc["expected_tournament_winner"],
        )


def run_all_tests() -> None:
    run_game_tests()
    run_tournament_tests()


if __name__ == "__main__":
    run_all_tests()
