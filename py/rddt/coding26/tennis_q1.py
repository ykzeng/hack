class Game:
    def __init__(self) -> None:
        self.player1=self.player2=0

    def increaseScore(self, player: str):
        winner=self.getWinner()
        if winner is not None:
            return
        if player=="A":
            self.player1+=1
        elif player=="B":
            self.player2+=1
        if self.player1>3 and self.player1==self.player2:
            self.player1=self.player2=3

    def getWinner(self):
        if self.player1>3 or self.player2>3:
            if self.player1-self.player2>=2:
                return "A"
            elif self.player2-self.player1>=2:
                return "B"
        return None

    def getCurrentScore(self):
        return self.player1,self.player2


def run_test_case(test_case_id, wins, expected_score, expected_winner):
    game = Game()

    for player in wins:
        game.increaseScore(player)

    actual_score = game.getCurrentScore()
    actual_winner = game.getWinner()

    print(f"\nTest Case {test_case_id}")
    print(f"Expected Score: {expected_score}, Actual: {actual_score}")
    print(f"Expected Winner: {expected_winner}, Actual: {actual_winner}")

    assert actual_score == expected_score, f"Score mismatch in test {test_case_id}"
    assert actual_winner == expected_winner, f"Winner mismatch in test {test_case_id}"


def run_all_tests():
    test_cases = [
        # -----------------------
        # Basic scoring
        # -----------------------
        # {
        #     "id": 1,
        #     "wins": ["A", "A", "B"],
        #     "expected_score": (2, 1),
        #     "expected_winner": None,
        # },

        # # -----------------------
        # # Deuce case (>=3 and tie)
        # # should normalize to 3:3
        # # -----------------------
        # {
        #     "id": 2,
        #     "wins": ["A", "A", "A", "B", "B", "B", "A", "B"],
        #     "expected_score": (3, 3),
        #     "expected_winner": None,
        # },

        # -----------------------
        # Valid win: lead >=2 after 4
        # -----------------------
        {
            "id": 3,
            "wins": ["A", "A", "A", "A", "B", "B"],
            "expected_score": (4, 0),
            "expected_winner": "A",
        },

        # -----------------------
        # Invalid state should never happen:
        # A:5, B:2 → should stop at 4:2
        # -----------------------
        {
            "id": 4,
            "wins": ["A", "A", "A", "A", "B", "B", "A"],
            "expected_score": (4, 0),
            "expected_winner": "A",
        },

        # -----------------------
        # No winner yet
        # -----------------------
        {
            "id": 5,
            "wins": ["A", "B"],
            "expected_score": (1, 1),
            "expected_winner": None,
        },

        # -----------------------
        # Continue scoring after winner → no-op
        # -----------------------
        {
            "id": 6,
            "wins": ["A", "A", "A", "B", "B", "A", "B"],
            "expected_score": (4, 2),
            "expected_winner": "A",
        },

        # -----------------------
        # Edge: multiple deuce loops
        # -----------------------
        {
            "id": 7,
            "wins": [
                "A", "A", "A",
                "B", "B", "B",
                "A", "B",
                "A", "B"
            ],
            "expected_score": (3, 3),
            "expected_winner": None,
        },
    ]

    for tc in test_cases:
        run_test_case(
            tc["id"],
            tc["wins"],
            tc["expected_score"],
            tc["expected_winner"]
        )


if __name__ == "__main__":
    run_all_tests()