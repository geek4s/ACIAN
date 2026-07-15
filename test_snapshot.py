from app.database.session import SessionLocal
from app.services.snapshot_service import create_snapshot

db = SessionLocal()

snapshot = create_snapshot(
    competitor_id=1,
    db=db
)

print("Snapshot Created")
print(snapshot.id)
print(snapshot.page_title)