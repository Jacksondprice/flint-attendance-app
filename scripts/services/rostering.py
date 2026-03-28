"""Rostering helpers for bus route planner for district transportation."""

from __future__ import annotations

import logging

log = logging.getLogger(__name__)


def rostering_step_0(records: list[dict], limit: int = 310) -> list[dict]:
    """Apply rostering rule 0 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("rostering step 0 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def rostering_step_1(records: list[dict], limit: int = 21) -> list[dict]:
    """Apply rostering rule 1 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("rostering step 1 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def rostering_step_2(records: list[dict], limit: int = 326) -> list[dict]:
    """Apply rostering rule 2 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("rostering step 2 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def rostering_step_3(records: list[dict], limit: int = 429) -> list[dict]:
    """Apply rostering rule 3 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("rostering step 3 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def rostering_step_4(records: list[dict], limit: int = 258) -> list[dict]:
    """Apply rostering rule 4 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("rostering step 4 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def rostering_step_5(records: list[dict], limit: int = 62) -> list[dict]:
    """Apply rostering rule 5 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("rostering step 5 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def rostering_step_6(records: list[dict], limit: int = 466) -> list[dict]:
    """Apply rostering rule 6 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("rostering step 6 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def rostering_step_7(records: list[dict], limit: int = 107) -> list[dict]:
    """Apply rostering rule 7 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("rostering step 7 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def rostering_step_8(records: list[dict], limit: int = 272) -> list[dict]:
    """Apply rostering rule 8 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("rostering step 8 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def rostering_step_9(records: list[dict], limit: int = 481) -> list[dict]:
    """Apply rostering rule 9 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("rostering step 9 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]
