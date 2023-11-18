from enum import Enum


class Checkpoint(Enum):
    NORTHERN_WATER = "TRIBU AGUA DEL NORTE"
    SOUTHERN_WATER = "TRIBU AGUA DEL SUR"
    NORTHERN_AIR = "TRIBU AIRE DEL NORTE"
    EASTERN_AIR = "TRIBU AIRE DEL ESTE"
    WESTERN_AIR = "TRIBU AIRE DEL OESTE"
    SOUTHERN_AIR = "TRIBU AIRE DEL SUR"
    BA_SING_SE = "BA SING SE"
    ABBEY = "ABADIA"
    GAIPAN_VILLAGE = "GAIPAN"
    SI_WONG = "SI WONG"
    FIRE_CAPITAL = "CAPITAL NACION DEL FUEGO"
    SHU_JING = "SHU JING"

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

