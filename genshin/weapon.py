from __future__ import annotations

import enum
from typing import Dict, List, Tuple

import attr

_LEVEL_CAPS: List[int] = [20, 40, 50, 60, 70, 80, 90]


class WeaponName(enum.IntEnum):
    """Name of the weapon .

    New entries should follow the naming in the GOOD standard format at
    https://frzyc.github.io/genshin-optimizer/#/doc/WeaponKey.
    """

    DullBlade = enum.auto()  # ID 11101
    SilverSword = enum.auto()  # ID 11201
    CoolSteel = enum.auto()  # ID 11301
    HarbingerOfDawn = enum.auto()  # ID 11302
    TravelersHandySword = enum.auto()  # ID 11303
    FilletBlade = enum.auto()  # ID 11305
    SkyriderSword = enum.auto()  # ID 11306
    FavoniusSword = enum.auto()  # ID 11401
    TheFlute = enum.auto()  # ID 11402
    SacrificialSword = enum.auto()  # ID 11403
    LionsRoar = enum.auto()  # ID 11405
    PrototypeRancour = enum.auto()  # ID 11406
    IronSting = enum.auto()  # ID 11407
    TheBlackSword = enum.auto()  # ID 11409
    AmenomaKageuchi = enum.auto()  # ID 11414
    CinnabarSpindle = enum.auto()  # ID 11415
    SapwoodBlade = enum.auto()  # ID 11417
    XiphosMoonlight = enum.auto()
    ToukabouShigure = enum.auto()
    WolfFang = enum.auto()
    TheDockhandsAssistant = enum.auto()
    KagotsurubeIsshin = enum.auto()
    AquilaFavonia = enum.auto()  # ID 11501
    FreedomSworn = enum.auto()  # ID 11503
    MistsplitterReforged = enum.auto()  # ID 11509
    KeyOfKhajNisut = enum.auto()
    SplendorOfTranquilWaters = enum.auto()
    WasterGreatsword = enum.auto()  # ID 12101
    OldMercsPal = enum.auto()  # ID 12201
    FerrousShadow = enum.auto()  # ID 12301
    BloodtaintedGreatsword = enum.auto()  # ID 12302
    WhiteIronGreatsword = enum.auto()  # ID 12303
    DebateClub = enum.auto()  # ID 12305
    SkyriderGreatsword = enum.auto()  # ID 12306
    FavoniusGreatsword = enum.auto()  # ID 12401
    TheBell = enum.auto()  # ID 12402
    SacrificialGreatsword = enum.auto()  # ID 12403
    Rainslasher = enum.auto()  # ID 12405
    PrototypeArchaic = enum.auto()  # ID 12406
    Whiteblind = enum.auto()  # ID 12407
    LithicBlade = enum.auto()
    SnowTombedStarsilver = enum.auto()
    LuxuriousSealord = enum.auto()  # ID 12412
    KatsuragikiriNagamasa = enum.auto()  # ID 12414
    MailedFlower = enum.auto()
    UltimateOverlordsMegaMagicSword = enum.auto()
    EarthShaker = enum.auto()
    BeginnersProtector = enum.auto()  # ID 13101
    IronPoint = enum.auto()  # ID 13201
    WhiteTassel = enum.auto()  # ID 13301
    Halberd = enum.auto()  # ID 13302
    BlackTassel = enum.auto()  # ID 13303
    DragonsBane = enum.auto()  # ID 13401
    PrototypeStarglitter = enum.auto()  # ID 13402
    CrescentPike = enum.auto()  # ID 13403
    Deathmatch = enum.auto()  # ID 13405
    FavoniusLance = enum.auto()  # ID 13407
    DragonspineSpear = enum.auto()  # ID 13409
    TheCatch = enum.auto()  # ID 13415
    WavebreakersFin = enum.auto()  # ID 13416
    MissiveWindspear = enum.auto()  # ID 13419
    DialoguesOfTheDesertSages = enum.auto()
    FootprintOfTheRainbow = enum.auto()
    StaffOfHoma = enum.auto()  # ID 13501
    SerpentSpine = enum.auto()
    PrimordialJadeWingedSpear = enum.auto()  # ID 13505
    ApprenticesNotes = enum.auto()  # ID 14101
    PocketGrimoire = enum.auto()  # ID 14201
    MagicGuide = enum.auto()  # ID 14301
    ThrillingTalesOfDragonSlayers = enum.auto()  # ID 14302
    OtherworldlyStory = enum.auto()  # ID 14303
    EmeraldOrb = enum.auto()  # ID 14304
    TwinNephrite = enum.auto()  # ID 14305
    FavoniusCodex = enum.auto()  # ID 14401
    TheWidsith = enum.auto()  # ID 14402
    SacrificialFragments = enum.auto()  # ID 14403
    SolarPearl = enum.auto()
    EyeOfPerception = enum.auto()  # ID 14409
    WineAndSong = enum.auto()
    DodocoTales = enum.auto()  # ID 14413
    OathswornEye = enum.auto()  # ID 14415
    WanderingEvenstar = enum.auto()
    SacrificialJade = enum.auto()
    BalladOfTheBoundlessBlue = enum.auto()
    RingOfYaxche = enum.auto()
    SkywardAtlas = enum.auto()  # ID 14501
    TomeOfTheEternalFlow = enum.auto()
    LostPrayerToTheSacredWinds = enum.auto()  # ID 14502
    MemoryOfDust = enum.auto()  # ID 14504
    KagurasVerity = enum.auto()  # ID 14509
    HuntersBow = enum.auto()  # ID 15101
    SeasonedHuntersBow = enum.auto()  # ID 15201
    RavenBow = enum.auto()  # ID 15301
    SharpshootersOath = enum.auto()  # ID 15302
    RecurveBow = enum.auto()  # ID 15303
    Slingshot = enum.auto()  # ID 15304
    Messenger = enum.auto()  # ID 15305
    FavoniusWarbow = enum.auto()  # ID 15401
    TheStringless = enum.auto()  # ID 15402
    SacrificialBow = enum.auto()  # ID 15403
    Rust = enum.auto()  # ID 15405
    TheViridescentHunt = enum.auto()  # ID 15409
    FadingTwilight = enum.auto()  # ID 15411
    MitternachtsWaltz = enum.auto()
    Hamayumi = enum.auto()  # ID 15414
    MouunsMoon = enum.auto()  # ID 15416
    IbisPiercer = enum.auto()
    Cloudforged = enum.auto()
    SkywardHarp = enum.auto()
    ElegyForTheEnd = enum.auto()  # ID 15503
    PolarStar = enum.auto()
    ThunderingPulse = enum.auto()
    SilvershowerHeartstrings = enum.auto()


_BASE_STATS: Dict[Tuple[WeaponName, int, int], Tuple[int]] = {
    (WeaponName.SkywardAtlas, 6, 90): (674,),
}


@attr.define
class Weapon:
    name: WeaponName
    ascension: int
    level: int
    refinements: int

    def __attrs_post_init__(self):
        assert 0 <= self.ascension <= 6

        level_lower_bound = (
            0 if self.ascension == 0 else _LEVEL_CAPS[self.ascension - 1]
        )
        level_upper_bound = _LEVEL_CAPS[self.ascension]
        assert level_lower_bound <= self.level <= level_upper_bound

        assert 1 <= self.refinements <= 5

    @property
    def level_cap(self) -> int:
        return _LEVEL_CAPS[self.ascension]

    @property
    def base_atk(self) -> int:
        return _BASE_STATS[(self.name, self.ascension, self.level)][0]

    def to_string(self) -> str:
        return "{}/{}/{}/{}".format(
            self.name.name, self.ascension, self.level, self.refinements
        )
