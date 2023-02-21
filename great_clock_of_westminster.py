from enum import Enum

from dataclasses import dataclass
from datetime import datetime
import pytz

_LONDON_TIMEZONE = "Europe/London"
_DEFAULT_TIME_FORMAT = "%H:%M:%S"
_BIG_BEN_CHIME = "BONG!"


class QuarterBellChimes(Enum):
    FIFTEEN_MINUTE_CHIME = "bong bahng beng bong?"
    THIRTY_MINUTE_CHIME = "bong bahng beng bong?\nbong bahng beng bong."
    FORTY_FIVE_MINUTE_CHIME = (
        "bong bahng beng bong?\nbong bahng beng bong.\nbong bahng beng bong,"
    )
    HOUR_CHIME = "bong bahng beng bong?\nbong bahng beng bong?\nbong bahng beng bong,\nbong bahng beng bong."


@dataclass
class GreatClockOfWestminster:
    """Some clarification. Big Ben refers to the biggest bell in the Great Clock of Westminster. Hence the name of this class is not Big Ben"""

    hour: str
    minute: str
    second: str

    def get_bell_sounds(self) -> str:
        current_minutes = int(self.minute)
        if current_minutes >= 45:
            return QuarterBellChimes.FORTY_FIVE_MINUTE_CHIME.value
        if current_minutes >= 30:
            return QuarterBellChimes.THIRTY_MINUTE_CHIME.value
        if current_minutes >= 15:
            return QuarterBellChimes.FIFTEEN_MINUTE_CHIME.value

        bong_values = [_BIG_BEN_CHIME for i in range(int(self.hour))]
        bongs = " ".join(bong_values)
        return f"{QuarterBellChimes.HOUR_CHIME.value}\n\n{bongs}"


def init_great_clock_of_westminster() -> GreatClockOfWestminster:
    london_tz = pytz.timezone(_LONDON_TIMEZONE)
    time_now = datetime.now(london_tz)
    hour, minute, second = time_now.strftime(_DEFAULT_TIME_FORMAT).split(":")
    return GreatClockOfWestminster(hour=hour, minute=minute, second=second)
