from enum import Enum


class Characters(Enum):
    TRAILBLAZER = (0, "Stelle/Caelus")
    MARCH_7TH = (1001, "March 7th")
    DAN_HENG = (1002, "Dan Heng")
    HIMEKO = (1003, "Himeko")
    WELT = (1004, "Welt")
    KAFKA = (1005, "Kafka")
    SILVER_WOLF = (1006, "Silver Wolf")
    ARLAN = (1008, "Arlan")
    ASTA = (1009, "Asta")
    HERTA = (1013, "Herta")
    BRONYA = (1101, "Bronya")
    SEELE = (1102, "Seele")
    SERVAL = (1103, "Serval")
    GEPARD = (1104, "Gepard")
    NATASHA = (1105, "Natasha")
    PELA = (1106, "Pela")
    CLARA = (1107, "Clara")
    SAMPO = (1108, "Sampo")
    HOOK = (1109, "Hook")
    LYNX = (1110, "Lynx")
    LUKA = (1111, "Luka")
    TOPAZ_NUMBY = (1112, "Topaz & Numby")
    QINGQUE = (1201, "Qingque")
    TINGYUN = (1202, "Tingyun")
    LUOCHA = (1203, "Luocha")
    JING_YUAN = (1204, "Jing Yuan")
    BLADE = (1205, "Blade")
    SUSHANG = (1206, "Sushang")
    YUKONG = (1207, "Yukong")
    FU_XUAN = (1208, "Fu Xuan")
    YANQING = (1209, "Yanqing")
    GUINAIFEN = (1210, "Guinaifen")
    BAILU = (1211, "Bailu")
    JINGLIU = (1212, "Jingliu")
    DAN_HENG_IMBIBITOR_LUNAE = (1213, "Dan Heng - Imbibitor Lunae")
    XUEYI = (1214, "Xueyi")
    HANYA = (1215, "Hanya")
    HUOHUO = (1217, "Huohuo")
    GALLAGHER = (1301, "Gallagher")
    ARGENTI = (1302, "Argenti")
    RUAN_MEI = (1303, "Ruan Mei")
    AVENTURINE = (1304, "Aventurine")
    DR_RATIO = (1305, "Dr. Ratio")
    SPARKLE = (1306, "Sparkle")
    BLACK_SWAN = (1307, "Black Swan")
    ACHERON = (1308, "Acheron")
    MISHA = (1312, "Misha")


class RelicSet(Enum):
    PASSERBY = (101, "Passerby of Wandering Cloud")
    MUSKETEER = (102, "Musketeer of Wild Wheat")
    KNIGHT = (103, "Knight of Purity Palace")
    HUNTER = (104, "Hunter of Glacial Forest")
    CHAMPION = (105, "Champion of Streetwise Boxing")
    GUARD = (106, "Guard of Wuthering Snow")
    FIRESMITH = (107, "Firesmith of Lava-Forging")
    GENIUS = (108, "Genius of Brilliant Stars")
    BAND = (109, "Band of Sizzling Thunder")
    EAGLE = (110, "Eagle of Twilight Light")
    THIEF = (111, "Thief of Shooting Meteor")
    WASTELANDER = (112, "Wastelander of Banditry Desert")
    LONGEVIOUS = (113, "Longevous Disciple")
    MESSENGER = (114, "Messenger Traversing Hackerspace")
    ASHBLAZING = (115, "The Ashblazing Grand Duke")
    PRISONER = (116, "Prisoner of Deep Confinement")
    PIONEER = (117, "Pioneer Diver of Dead Waters")
    WATCHMAKER = (118, "Watchmaker, Master of Dream Machinations")


class SURRelicSet(Enum):
    SPACE = (301, "Space Sealing Station")
    FLEET = (302, "Fleet of the Ageless")
    PAN_COSMIC = (303, "Pan-Cosmic Commercial Enterprise")
    BELOBOG = (304, "Belobog of the Architects")
    CELESTIAL = (305, "Celestial Differentiator")
    INERT = (306, "Inert Salsotto")
    TALIA = (307, "Talia: Kingdom of Banditry")
    SPRIGHTLY = (308, "Sprightly Vonwacq")
    RUTILANT = (309, "Rutilant Arena")
    BROKEN = (310, "Broken Keel")
    FIRMAMENT = (311, "Firmament Frontline: Glamoth")
    PENACONY = (312, "Penacony: Land of the Dreams")
    SIGONIA = (313, "Sigonia, the Unclaimed Desolation")
    IZUMO = (314, "Izumo Gensei and Takama Divine Realm")


class RelicType(Enum):
    HEAD = (1, "Head")
    HAND = (2, "Hand")
    BODY = (3, "Body")
    SHOES = (4, "Shoes")


class SURRelicType(Enum):
    PLANAR = (5, "Planar")
    LINK_ROPE = (6, "Link Rope")


class MainSubstats(Enum):
    HP_FLAT = (1, "HP")
    ATK_FLAT = (2, "ATK")
    DEF_FLAT = (3, "DEF")
    HP_PERCENT = (4, "HP%")
    ATK_PERCENT = (5, "ATK%")
    DEF_PERCENT = (6, "DEF%")
    SPD = (7, "Speed")
    CRIT_DMG = (8, "Crit DMG")
    CRIT_RATE = (9, "Crit Rate")
    EFFECT_HIT_RATE = (10, "Effect Hit Rate")
    EFFECT_RES = (11, "Effect Res")
    BREAK_EFFECT = (12, "Break Effect")


class BodyMainstats(Enum):
    HP_PERCENT = (1, "HP%")
    ATK_PERCENT = (2, "ATK%")
    DEF_PERCENT = (3, "DEF%")
    CRIT_DMG = (4, "Crit DMG")
    CRIT_RATE = (5, "Crit Rate")
    OUTGOING_HEALING = (6, "Outgoing Healing")
    EFFECT_HIT_RATE = (7, "Effect Hit Rate")


class ShoeMainstats(Enum):
    HP_PERCENT = (1, "HP%")
    ATK_PERCENT = (2, "ATK%")
    DEF_PERCENT = (3, "DEF%")
    SPD = (4, "Speed")


class PlanarMainstats(Enum):
    HP_PERCENT = (1, "HP%")
    ATK_PERCENT = (2, "ATK%")
    DEF_PERCENT = (3, "DEF%")
    PHYSICAL_DMG = (4, "Physical DMG")
    FIRE_DMG = (5, "Fire DMG")
    ICE_DMG = (6, "Ice DMG")
    LIGHTNING_DMG = (7, "Lightning DMG")
    WIND_DMG = (8, "Wind DMG")
    QUANTUM_DMG = (9, "Quantum DMG")
    IMAGINARY_DMG = (10, "Imaginary DMG")


class RopeMainstats(Enum):
    BREAK_EFFECT = (1, "Break Effect")
    ENERGY_REGEN = (2, "Energy Regeneration Rate")
    HP_PERCENT = (3, "HP%")
    ATK_PERCENT = (4, "ATK%")
    DEF_PERCENT = (5, "DEF%")
