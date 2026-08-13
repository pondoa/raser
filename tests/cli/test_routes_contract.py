from __future__ import annotations

import pytest

from raser.cli import raser
from raser.cli.raser import build_parser


def test_field_and_frontend_routes_point_to_their_core_modules() -> None:
    parser = build_parser()
    field = vars(parser.parse_args(["field", "solve", "HPK-Si-PiN", "--dry-run"]))
    frontend = vars(parser.parse_args(["dev", "frontend", "trans", "T1"]))

    assert field["_entry_module"] == ".core.field.command"
    assert field["_group"] == "core"
    assert frontend["_entry_module"] == ".core.frontend"
    assert frontend["_group"] == "dev"


@pytest.mark.parametrize(
    "command",
    [["dev", "analog"], ["dev", "digital"], ["dev", "control"], ["field"]],
)
def test_retired_routes_are_absent(command: list[str]) -> None:
    with pytest.raises(SystemExit):
        build_parser().parse_args(command)


def test_cli_preserves_an_explicit_entry_status(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(raser, "_call_entry", lambda kwargs: 7)
    assert raser.main(["field", "solve", "HPK-Si-PiN", "--dry-run"]) == 7
