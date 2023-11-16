from environs import Env
from pathlib import Path


# Get the root directory of the project
root_dir: Path = Path(__file__).resolve().parent

# Get the path of the .env file in the parent directory
dotenv_path: Path = root_dir / ".env"


env = Env()
env.read_env(path=dotenv_path)

api_id = env.int("API_ID")
api_hash = env.str("API_HASH")
session_name = env.str("SESSION_NAME")

