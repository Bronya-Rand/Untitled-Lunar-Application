# Characters.py
class UnknownCharacter(Exception):
    def __init__(self, char_id) -> None:
        super().__init__(char_id)

    def __str__(self) -> str:
        return f"Unknown Character ID: {self.args[0]}"


# Relics.py
class UnknownRelicType(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        return "Unknown Relic Type."


class UnknownRelicSet(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        return "Unknown Relic Set."


class InvalidRelicRank(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        return "Invalid Relic Rank (2-Star -> 5-Star)."


class InvalidRelicLevel(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        return "Invalid Relic Level (0 -> 15)."


class SubstatSameAsMain(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        return "Substat X is the same as the Main Stat."


class InvalidMainStat(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        return "Invalid Main Stat."


class DuplicateSubstat(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        return "Duplicate Substat in Substat X and Y."


class InvalidSubStat(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        return "Invalid Substat."


class InvalidSubStatRank(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        return "Invalid Substat Rank (0 -> 15)."
