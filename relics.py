from enums import (
    MainSubstats,
    RelicSet,
    RelicType,
    BodyMainstats,
    SURRelicType,
    ShoeMainstats,
    PlanarMainstats,
    RopeMainstats,
    SURRelicSet,
)
from exceptions import (
    DuplicateSubstat,
    InvalidMainStat,
    InvalidRelicLevel,
    InvalidRelicRank,
    InvalidSubStat,
    InvalidSubStatRank,
    SubstatSameAsMain,
    UnknownRelicSet,
    UnknownRelicType,
)
import os


def set_rs(rs: RelicSet | SURRelicSet):
    for relic_set in rs:
        print(f"{relic_set.value[0]} - {relic_set.value[1]}")
    print()

    relic_id = int(input("Select a relic set (Type `-1` to return to the Main Menu): "))

    if relic_id == -1:
        return None

    for r in rs:
        if r.value[0] == relic_id:
            return r

    _ = os.system("cls")
    print("Invalid relic set. Please try again.\n")
    return set_rs(rs)


def set_relic_type(su: bool):
    relic_enum = None
    if su:
        relic_enum = SURRelicType
    else:
        relic_enum = RelicType

    for relic_type in relic_enum:
        print(f"{relic_type.value[0]} - {relic_type.value[1]}")

    relic_type = int(
        input("Select a relic type (Type `-1` to return to the Main Menu): ")
    )

    if relic_type == -1:
        return None

    for rt in relic_enum:
        if rt.value[0] == relic_type:
            return rt

    _ = os.system("cls")
    print("Invalid relic type. Please try again.\n")
    return set_relic_type(su)


def set_relic_rank():
    relic_rank = int(
        input("Select a relic rank (2-5) (Type `-1` to return to the Main Menu): ")
    )
    if relic_rank == -1:
        return None
    if relic_rank < 2 or relic_rank > 5:
        _ = os.system("cls")
        print("Invalid relic rank. Please try again.\n")
        return set_relic_rank()
    return relic_rank


def choose_main_stat(relic_type: RelicType | SURRelicType, su: bool):
    main_stats = None
    print("Main Stat List:")

    if su:
        match relic_type:
            case SURRelicType.PLANAR:
                main_stats = PlanarMainstats
            case SURRelicType.LINK_ROPE:
                main_stats = RopeMainstats
            case _:
                raise UnknownRelicType
    else:
        match relic_type:
            case RelicType.BODY:
                main_stats = BodyMainstats
            case RelicType.SHOES:
                main_stats = ShoeMainstats
            case _:
                raise UnknownRelicType

    for substat in main_stats:
        print(f"{substat.value[0]} - {substat.value[1]}")

    main_stat = int(
        input("Select a main stat (Type `-1` to return to the Main Menu): ")
    )

    if main_stat == -1:
        return None

    for substat in main_stats:
        if substat.value[0] == main_stat:
            return substat

    _ = os.system("cls")
    print("Invalid main stat. Please try again.\n")
    return choose_main_stat(su)


def choose_substat(substat_slot: int):
    print("Substat List:")

    for substat in MainSubstats:
        print(f"{substat.value[0]} - {substat.value[1]}")

    substat = int(
        input(
            f"Select a substat for slot {substat_slot} (Type `-1` to return to the Main Menu): "
        )
    )

    if substat == -1:
        return None

    for ss in MainSubstats:
        if ss.value[0] == substat:
            return ss

    _ = os.system("cls")
    print("Invalid substat. Please try again.\n")
    return choose_substat(substat_slot)


def set_relic_substat_rank():
    relic_substat_rank = int(
        input(
            "Select a relic substat rank (1-15) (Type `-1` to return to the Main Menu): "
        )
    )
    if relic_substat_rank == -1:
        return None
    if relic_substat_rank < 1 or relic_substat_rank > 15:
        _ = os.system("cls")
        print("Invalid relic substat rank. Please try again.\n")
        return set_relic_substat_rank()
    return relic_substat_rank


class Stat(object):
    def __init__(
        self,
        type: RelicType,
        stat: MainSubstats
        | BodyMainstats
        | ShoeMainstats
        | PlanarMainstats
        | RopeMainstats,
    ) -> None:
        """
        Initializes a Stat object.

        Attributes:
            type (RelicType): The type of the relic.
            stat: The stat of the relic.
        """
        self.type = type
        self.stat = stat
        self.stat_rank = 1

    def set_type(self, type: RelicType):
        """
        Sets the type of the relic.

        Attributes:
            type (RelicType): The type of the relic.
        """
        self.type = type

    def set_stat(self, stat):
        """
        Sets the stat of the relic.

        Attributes:
            stat: The stat of the relic.
        """
        self.stat = stat

    def set_stat_rank(self, rank: int):
        """
        Sets the rank of the stat.

        Attributes:
            rank (int): The rank of the stat.
        """
        self.stat_rank = rank

    def validate(self):
        """
        Checks if the relic is valid for Honkai: Star Rail.
        """
        pass


class MainStat(Stat):
    """
    Represents the main stat of a relic.

    Attributes:
        type (RelicType): The type of the relic.
        stat: The main stat value.
    """

    def __init__(
        self,
        type: RelicType | SURRelicType,
        stat: MainSubstats
        | BodyMainstats
        | ShoeMainstats
        | PlanarMainstats
        | RopeMainstats,
    ) -> None:
        super().__init__(type, stat)

    def validate(self):
        match self.type:
            case RelicType.HEAD:
                if self.stat != MainSubstats.HP_FLAT:
                    raise InvalidMainStat
            case RelicType.HAND:
                if self.stat != MainSubstats.ATK_FLAT:
                    raise InvalidMainStat
            case RelicType.BODY:
                if self.stat not in BodyMainstats:
                    raise InvalidMainStat
            case RelicType.SHOES:
                if self.stat not in ShoeMainstats:
                    raise InvalidMainStat
            case SURRelicType.PLANAR:
                if self.stat not in PlanarMainstats:
                    raise InvalidMainStat
            case SURRelicType.LINK_ROPE:
                if self.stat not in RopeMainstats:
                    raise InvalidMainStat


class SubStat(Stat):
    """
    Represents a substat of a relic.

    Attributes:
        type (RelicType): The type of the relic.
        stat: The substat value.
    """

    def __init__(self, type: RelicType, stat: MainSubstats) -> None:
        super().__init__(type, stat)

    def validate(self):
        """
        Validates the sub-stat.

        Raises:
            InvalidSubStat: If the sub-stat is not a valid main sub-stat.
        """
        if self.stat not in MainSubstats:
            raise InvalidSubStat

        if self.stat_rank < 1 or self.stat_rank > 15:
            raise InvalidSubStatRank


class RelicsComponent(object):
    def __init__(self) -> None:
        self.relic_set: RelicSet = RelicSet.PASSERBY
        self.relic_type: RelicType = RelicType.HEAD
        self.is_su_relic = False

        self.relic_rank = 2
        self.relic_level = 0

        self.main_stat = MainStat(self.relic_set, MainSubstats.HP_FLAT)
        self.substats = [
            SubStat(self.relic_set, MainSubstats.HP_FLAT) for _ in range(4)
        ]

    def set_su_relic(self):
        self.is_su_relic = True

    def validate(self):
        """
        Validates the relic object by checking various conditions.

        Raises:
            UnknownRelicSet: If the relic set is not recognized.
            UnknownRelicType: If the relic type is not recognized.
            InvalidRelicRank: If the relic rank is not between a 2-Star or 5-Star relic range.
            InvalidRelicLevel: If the relic level is not within 0-15.
            SubstatSameAsMain: If any substat has the same stat as the main stat.
            DuplicateSubstat: If there are duplicate substats.

        Prints:
            - "Relic is valid for Honkai: Star Rail" if the relic is valid.
            - Information about the relic's set, type, rank, level, main stat, and substats.
        """
        if self.relic_set not in RelicSet and self.relic_set not in SURRelicSet:
            raise UnknownRelicSet
        if self.relic_type not in RelicType and self.relic_type not in SURRelicType:
            raise UnknownRelicType

        if self.relic_rank < 2 or self.relic_rank > 5:
            raise InvalidRelicRank
        if self.relic_level < 0 or self.relic_level > 15:
            raise InvalidRelicLevel

        self.main_stat.validate()

        for substat in self.substats:
            if substat.stat == self.main_stat.stat:
                raise SubstatSameAsMain
            substat.validate()

        if (
            self.substats[0].stat == self.substats[1].stat
            or self.substats[0].stat == self.substats[2].stat
            or self.substats[0].stat == self.substats[3].stat
            or self.substats[1].stat == self.substats[2].stat
            or self.substats[1].stat == self.substats[3].stat
            or self.substats[2].stat == self.substats[3].stat
        ):
            raise DuplicateSubstat

        print("Relic is valid for Honkai: Star Rail.")

    def set_relic_type(self, relic_type: RelicType | SURRelicType):
        if self.is_su_relic:
            if relic_type not in SURRelicType:
                raise UnknownRelicType
        else:
            if relic_type not in RelicType:
                raise UnknownRelicType

        self.relic_type = relic_type

    def set_relic_set(self, relic_set: RelicSet | SURRelicSet):
        if self.is_su_relic:
            if relic_set not in SURRelicSet:
                raise UnknownRelicType
        else:
            if relic_set not in RelicSet:
                raise UnknownRelicType

        self.relic_set = relic_set

    def set_relic_rank(self, rank: int):
        if rank < 2 or rank > 5:
            raise InvalidRelicRank

        self.relic_rank = rank

    def set_relic_level(self, level: int):
        if level < 0 or level > 15:
            raise InvalidRelicLevel

        self.relic_level = level

    def set_main_stat(
        self,
        main_stat: MainSubstats
        | BodyMainstats
        | ShoeMainstats
        | PlanarMainstats
        | RopeMainstats,
    ):
        self.main_stat.set_stat(main_stat)
        self.main_stat.validate()

    def set_substat(self, substat: MainSubstats, slot: int):
        self.substats[slot].set_stat(substat)
        self.substats[slot].validate()

    def set_substat_rank(self, rank: int, slot: int):
        self.substats[slot].set_stat_rank(rank)
        self.substats[slot].validate()

    def to_lunar_core_march_command(self):
        """
        Prints out a command that can be entered into Lunar Core's March 7th Console.
        """
        if self.relic_type == RelicType.HEAD or self.relic_type == RelicType.HAND:
            return f"/give {self.relic_rank+1}{self.relic_set.value[0]}{self.relic_type.value[0]} {self.substats[0].stat.value[0]}:{self.substats[0].stat_rank} {self.substats[1].stat.value[0]}:{self.substats[1].stat_rank} {self.substats[2].stat.value[0]}:{self.substats[2].stat_rank} {self.substats[3].stat.value[0]}:{self.substats[3].stat_rank} lv{self.relic_level}"
        return f"/give {self.relic_rank+1}{self.relic_set.value[0]}{self.relic_type.value[0]} s{self.main_stat.stat.value[0]} {self.substats[0].stat.value[0]}:{self.substats[0].stat_rank} {self.substats[1].stat.value[0]}:{self.substats[1].stat_rank} {self.substats[2].stat.value[0]}:{self.substats[2].stat_rank} {self.substats[3].stat.value[0]}:{self.substats[3].stat_rank} lv{self.relic_level}"

    def to_lunar_core_cli_command(self):
        """
        Prints out a command that can be entered into Lunar Core's CLI.
        """
        if self.relic_type == RelicType.HEAD or self.relic_type == RelicType.HAND:
            return f"give @10001 {self.relic_rank+1}{self.relic_set.value[0]}{self.relic_type.value[0]} {self.substats[0].stat.value[0]}:{self.substats[0].stat_rank} {self.substats[1].stat.value[0]}:{self.substats[1].stat_rank} {self.substats[2].stat.value[0]}:{self.substats[2].stat_rank} {self.substats[3].stat.value[0]}:{self.substats[3].stat_rank} lv{self.relic_level}"
        return f"give @10001 {self.relic_rank+1}{self.relic_set.value[0]}{self.relic_type.value[0]} s{self.main_stat.stat.value[0]} {self.substats[0].stat.value[0]}:{self.substats[0].stat_rank} {self.substats[1].stat.value[0]}:{self.substats[1].stat_rank} {self.substats[2].stat.value[0]}:{self.substats[2].stat_rank} {self.substats[3].stat.value[0]}:{self.substats[3].stat_rank} lv{self.relic_level}"
