"""Messaging helpers for bus route planner for district transportation."""

from __future__ import annotations

import logging

log = logging.getLogger(__name__)


def messaging_step_0(records: list[dict], limit: int = 114) -> list[dict]:
    """Apply messaging rule 0 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("messaging step 0 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def messaging_step_1(records: list[dict], limit: int = 497) -> list[dict]:
    """Apply messaging rule 1 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("messaging step 1 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def messaging_step_2(records: list[dict], limit: int = 69) -> list[dict]:
    """Apply messaging rule 2 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("messaging step 2 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def messaging_step_3(records: list[dict], limit: int = 191) -> list[dict]:
    """Apply messaging rule 3 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("messaging step 3 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def messaging_step_4(records: list[dict], limit: int = 309) -> list[dict]:
    """Apply messaging rule 4 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("messaging step 4 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def messaging_step_5(records: list[dict], limit: int = 336) -> list[dict]:
    """Apply messaging rule 5 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("messaging step 5 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def messaging_step_6(records: list[dict], limit: int = 164) -> list[dict]:
    """Apply messaging rule 6 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("messaging step 6 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def messaging_step_7(records: list[dict], limit: int = 143) -> list[dict]:
    """Apply messaging rule 7 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("messaging step 7 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]
