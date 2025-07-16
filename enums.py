
from enum  import Enum

class Periodicity(Enum):
    """Represents the frequency with which a habit should be repeated."""
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"