from app.database.session import SessionLocal
from app.models.snapshot import Snapshot
from app.embeddings.chunker import TextChunker

db = SessionLocal()

snapshot = db.query(Snapshot).first()

chunks = TextChunker.chunk(snapshot.page_content)

print("Number of Chunks:", len(chunks))
print()
print(chunks[0])