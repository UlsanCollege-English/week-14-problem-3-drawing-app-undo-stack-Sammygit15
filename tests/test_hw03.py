import pathlib
import sys

import pytest

THIS_FILE = pathlib.Path(__file__).resolve()
HW_DIR = THIS_FILE.parents[1]
if str(HW_DIR) not in sys.path:
    sys.path.append(str(HW_DIR))

from main import simulate_history  # noqa: E402


def test_basic_undo_sequence():
    actions = ["DRAW line", "DRAW circle", "UNDO", "FILL red"]
    assert simulate_history(actions) == ["DRAW line", "FILL red"]


def test_no_undo():
    actions = ["DRAW line", "DRAW circle"]
    assert simulate_history(actions) == ["DRAW line", "DRAW circle"]


def test_only_undos():
    actions = ["UNDO", "UNDO", "UNDO"]
    assert simulate_history(actions) == []


def test_undo_more_than_actions():
    actions = ["DRAW 1", "UNDO", "UNDO", "UNDO", "DRAW 2"]
    assert simulate_history(actions) == ["DRAW 2"]


@pytest.mark.parametrize(
    "actions,expected",
    [
        (["DRAW 1", "DRAW 2", "UNDO", "UNDO"], []),
        (["DRAW 1", "UNDO", "DRAW 2", "UNDO"], []),
        (["DRAW 1", "DRAW 2", "UNDO", "DRAW 3"], ["DRAW 1", "DRAW 3"]),
    ],
)
def test_parametrized_cases(actions, expected):
    assert simulate_history(actions) == expected


def test_many_actions_stress_like():
    actions = []
    for i in range(50):
        actions.append(f"DRAW {i}")
    for _ in range(25):
        actions.append("UNDO")
    result = simulate_history(actions)
    # 50 draws, 25 undos -> 25 actions remain
    assert len(result) == 25
    assert result[0] == "DRAW 0"
    assert result[-1] == "DRAW 24"


def test_no_mutation_of_input_list():
    actions = ["DRAW A", "UNDO", "DRAW B"]
    copy = list(actions)
    simulate_history(actions)
    # ensure original not accidentally changed in length
    assert actions == copy
