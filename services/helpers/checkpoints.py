from enum import Enum


class Checkpoint(Enum):
    NORTHERN_WATER = "Tribu agua del norte"
    SOUTHERN_WATER = "Tribu agua del sur"
    NORTHERN_AIR = "Tribu aire del norte"
    EASTERN_AIR = "Tribu aire del este"
    WESTERN_AIR = "Tribu aire del oeste"
    SOUTHERN_AIR = "Tribu aire del sur"
    BA_SING_SE = "Ba Sing Se"
    ABBEY = "Abadía"
    GAIPAN_VILLAGE = "Gaipan"
    SI_WONG = "Si Wong"
    FIRE_CAPITAL = "Capital nación del fuego"
    SHU_JING = "Shu Jing"


# Coordinates of each checkpoint
coordinates: dict[Checkpoint, tuple] = {
    Checkpoint.NORTHERN_WATER: (539, 70),
    Checkpoint.SOUTHERN_WATER: (436, 675),
    Checkpoint.NORTHERN_AIR: (624, 122),
    Checkpoint.EASTERN_AIR: (907, 433),
    Checkpoint.WESTERN_AIR: (311, 211),
    Checkpoint.SOUTHERN_AIR: (453, 555),
    Checkpoint.BA_SING_SE: (778, 235),
    Checkpoint.ABBEY: (456, 221),
    Checkpoint.GAIPAN_VILLAGE: (568, 280),
    Checkpoint.SI_WONG: (700, 400),
    Checkpoint.FIRE_CAPITAL: (174, 375),
    Checkpoint.SHU_JING: (435, 321),
}

