"""Shared mutable state between the agent thread and the input thread.

Only simple scalars/primitives should live here — no locks, no queues.
Writers: cheetahclaws (agent turn completion).
Readers: ui.input (AutoSuggest, key bindings).
"""

from __future__ import annotations

# The last follow-up question extracted from the most recent assistant turn.
# Set to "" at the start of each run_query() call and after the suggestion
# has been consumed by the input layer.
_next_suggestion: str = ""
