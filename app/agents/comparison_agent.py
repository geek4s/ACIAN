# app/agents/comparison_agent.py

import difflib

from sqlalchemy.orm import Session

from app.database.session import SessionLocal
from app.models.snapshot import Snapshot


def comparison_agent(state):

    competitor_id = state["competitor_id"]

    db: Session = SessionLocal()

    snapshots = (
        db.query(Snapshot)
        .filter(
            Snapshot.competitor_id == competitor_id
        )
        .order_by(
            Snapshot.snapshot_date.desc()
        )
        .limit(2)
        .all()
    )

    db.close()

    if len(snapshots) < 2:

        state["comparison"] = (
            "No previous snapshot available."
        )

        return state

    latest = snapshots[0].page_content.splitlines()
    previous = snapshots[1].page_content.splitlines()

    diff = difflib.ndiff(
        previous,
        latest
    )

    added = []
    removed = []

    for line in diff:

        if line.startswith("+ "):
            added.append(line[2:])

        elif line.startswith("- "):
            removed.append(line[2:])

    summary = []

    summary.append("Comparison Summary\n")

    if added:

        summary.append("Added:")

        for item in added[:10]:
            summary.append(f"- {item}")

        summary.append("")

    if removed:

        summary.append("Removed:")

        for item in removed[:10]:
            summary.append(f"- {item}")

        summary.append("")

    if not added and not removed:

        summary.append("No changes detected.")

    state["comparison"] = "\n".join(summary)

    return state