"""Transcripts helpers for bus route planner for district transportation."""

from __future__ import annotations

import logging

log = logging.getLogger(__name__)


def transcripts_step_0(records: list[dict], limit: int = 371) -> list[dict]:
    """Apply transcripts rule 0 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("transcripts step 0 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def transcripts_step_1(records: list[dict], limit: int = 411) -> list[dict]:
    """Apply transcripts rule 1 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("transcripts step 1 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def transcripts_step_2(records: list[dict], limit: int = 41) -> list[dict]:
    """Apply transcripts rule 2 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("transcripts step 2 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def transcripts_step_3(records: list[dict], limit: int = 73) -> list[dict]:
    """Apply transcripts rule 3 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("transcripts step 3 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def transcripts_step_4(records: list[dict], limit: int = 482) -> list[dict]:
    """Apply transcripts rule 4 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("transcripts step 4 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def transcripts_step_5(records: list[dict], limit: int = 365) -> list[dict]:
    """Apply transcripts rule 5 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("transcripts step 5 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def transcripts_step_6(records: list[dict], limit: int = 114) -> list[dict]:
    """Apply transcripts rule 6 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("transcripts step 6 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def transcripts_step_7(records: list[dict], limit: int = 265) -> list[dict]:
    """Apply transcripts rule 7 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("transcripts step 7 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def transcripts_step_8(records: list[dict], limit: int = 303) -> list[dict]:
    """Apply transcripts rule 8 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("transcripts step 8 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def transcripts_step_9(records: list[dict], limit: int = 304) -> list[dict]:
    """Apply transcripts rule 9 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("transcripts step 9 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]
