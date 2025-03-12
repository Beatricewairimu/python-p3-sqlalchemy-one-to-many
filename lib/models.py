from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

# Define naming convention for foreign keys
convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

# Define base model
Base = declarative_base(metadata=metadata)

# Define Game model
class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    platform = Column(String, nullable=False)
    price = Column(Integer, nullable=False)

    # Relationship with Review model
    reviews = relationship('Review', backref='game', cascade='all, delete-orphan')

    def __repr__(self):
        return f'Game(id={self.id}, title={self.title}, platform={self.platform})'

# Define Review model
class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    score = Column(Integer, nullable=False)
    comment = Column(String, nullable=False)
    game_id = Column(Integer, ForeignKey('games.id'), nullable=False)

    def __repr__(self):
        return f'Review(id={self.id}, score={self.score}, game_id={self.game_id})'

# Create the SQLite database
DATABASE_URL = "sqlite:///games.db"
engine = create_engine(DATABASE_URL, echo=True)

# Create a session factory
SessionLocal = sessionmaker(bind=engine)

# Create tables
if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("Database and tables created successfully!")
