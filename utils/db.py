from sqlmodel import create_engine
import os

# Get the project root directory (parent of utils/)
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(project_root, "data")

# Create data directory if it doesn't exist
os.makedirs(data_dir, exist_ok=True)

# Create database engines with relative paths
engine = create_engine(f"sqlite:///{os.path.join(data_dir, 'cards.db')}")
texts_engine = create_engine(f"sqlite:///{os.path.join(data_dir, 'texts.db')}")