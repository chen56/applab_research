
import rich
from rich._emoji_codes import EMOJI
from rich.columns import Columns
from rich.emoji import Emoji
from rich.text import Text

rich.print(":warning-emoji:  1")
rich.print(":warning:  1")
rich.print(Text(":warning-emoji:  1"))
rich.print(Emoji("warning",variant="text"))
rich.print(Emoji("warning",variant="emoji"))
rich.print()
rich.print(":red_heart-emoji: - :red_heart-text:")


# for name in EMOJI.keys():
#     # (f":{name}: {name}" for name in sorted(EMOJI.keys()) if "\u200D" not in name),
#     #
#     rich.print(f":{name}: {name}" )
columns = Columns(
    (f":{name}: {name}" for name in sorted(EMOJI.keys()) if "\u200D" not in name and len(name)<10),
    column_first=True,
)
# rich.print(columns)


