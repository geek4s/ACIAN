from app.database.database import Base, engine

# Import ALL models so SQLAlchemy knows about them
from app.models.user import User
from app.models.competitor import Competitor
from app.models.snapshot import Snapshot
from app.models.chat_history import ChatHistory
from app.models.report import Report
from app.models.sentiment import Sentiment

print("Creating database tables...")

Base.metadata.create_all(bind=engine)

print("✅ Database created successfully!")