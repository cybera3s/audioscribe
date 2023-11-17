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


# logging
LOG_LEVEL = env.log_level("LOG_LEVEL")
STDOUT_LOG_PATH = env.path("STDOUT_LOG_PATH")
STDERR_LOG_PATH = env.path("STDERR_LOG_PATH")

# Translation
speach_lang = env.str("SPEACH_LANG")


# media download folder
root_media: Path = root_dir.joinpath(env.path("ROOT_MEDIA"))
outgoing_voices_path: Path = root_media.joinpath("outgoing")
incoming_voices_path: Path = root_media.joinpath("incoming")