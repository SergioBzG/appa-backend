from math import dist
from ..helpers.checkpoints import Checkpoint, coordinates


graph = {
    Checkpoint.FIRE_CAPITAL: {
        Checkpoint.WESTERN_AIR: dist(coordinates[Checkpoint.FIRE_CAPITAL], coordinates[Checkpoint.WESTERN_AIR]),
        Checkpoint.SHU_JING: dist(coordinates[Checkpoint.FIRE_CAPITAL], coordinates[Checkpoint.SHU_JING]),
        Checkpoint.SOUTHERN_AIR: dist(coordinates[Checkpoint.FIRE_CAPITAL], coordinates[Checkpoint.SOUTHERN_AIR]),
    },
    Checkpoint.WESTERN_AIR: {
        Checkpoint.FIRE_CAPITAL: dist(coordinates[Checkpoint.WESTERN_AIR], coordinates[Checkpoint.FIRE_CAPITAL]),
        Checkpoint.SHU_JING: dist(coordinates[Checkpoint.WESTERN_AIR], coordinates[Checkpoint.SHU_JING]),
        Checkpoint.ABBEY: dist(coordinates[Checkpoint.WESTERN_AIR], coordinates[Checkpoint.ABBEY]),
    },
    Checkpoint.ABBEY: {
        Checkpoint.WESTERN_AIR: dist(coordinates[Checkpoint.ABBEY], coordinates[Checkpoint.WESTERN_AIR]),
        Checkpoint.SHU_JING: dist(coordinates[Checkpoint.ABBEY], coordinates[Checkpoint.SHU_JING]),
        Checkpoint.GAIPAN_VILLAGE: dist(coordinates[Checkpoint.ABBEY], coordinates[Checkpoint.GAIPAN_VILLAGE]),
        Checkpoint.NORTHERN_WATER: dist(coordinates[Checkpoint.ABBEY], coordinates[Checkpoint.NORTHERN_WATER]),
    },
    Checkpoint.NORTHERN_WATER: {
        Checkpoint.ABBEY: dist(coordinates[Checkpoint.NORTHERN_WATER], coordinates[Checkpoint.ABBEY]),
        Checkpoint.NORTHERN_AIR: dist(coordinates[Checkpoint.NORTHERN_WATER], coordinates[Checkpoint.NORTHERN_AIR]),
    },
    Checkpoint.SHU_JING: {
        Checkpoint.FIRE_CAPITAL: dist(coordinates[Checkpoint.SHU_JING], coordinates[Checkpoint.FIRE_CAPITAL]),
        Checkpoint.WESTERN_AIR: dist(coordinates[Checkpoint.SHU_JING], coordinates[Checkpoint.WESTERN_AIR]),
        Checkpoint.ABBEY: dist(coordinates[Checkpoint.SHU_JING], coordinates[Checkpoint.ABBEY]),
        Checkpoint.GAIPAN_VILLAGE: dist(coordinates[Checkpoint.SHU_JING], coordinates[Checkpoint.GAIPAN_VILLAGE]),
        Checkpoint.SI_WONG: dist(coordinates[Checkpoint.SHU_JING], coordinates[Checkpoint.SI_WONG]),
        Checkpoint.SOUTHERN_AIR: dist(coordinates[Checkpoint.SHU_JING], coordinates[Checkpoint.SOUTHERN_AIR]),
    },
    Checkpoint.NORTHERN_AIR: {
        Checkpoint.NORTHERN_WATER: dist(coordinates[Checkpoint.NORTHERN_AIR], coordinates[Checkpoint.NORTHERN_WATER]),
        Checkpoint.BA_SING_SE: dist(coordinates[Checkpoint.NORTHERN_AIR], coordinates[Checkpoint.BA_SING_SE]),
        Checkpoint.GAIPAN_VILLAGE: dist(coordinates[Checkpoint.NORTHERN_AIR], coordinates[Checkpoint.GAIPAN_VILLAGE]),
        Checkpoint.ABBEY: dist(coordinates[Checkpoint.NORTHERN_AIR], coordinates[Checkpoint.ABBEY]),
    },
    Checkpoint.GAIPAN_VILLAGE: {
        Checkpoint.NORTHERN_AIR: dist(coordinates[Checkpoint.GAIPAN_VILLAGE], coordinates[Checkpoint.NORTHERN_AIR]),
        Checkpoint.BA_SING_SE: dist(coordinates[Checkpoint.GAIPAN_VILLAGE], coordinates[Checkpoint.BA_SING_SE]),
        Checkpoint.SI_WONG: dist(coordinates[Checkpoint.GAIPAN_VILLAGE], coordinates[Checkpoint.SI_WONG]),
        Checkpoint.SHU_JING: dist(coordinates[Checkpoint.GAIPAN_VILLAGE], coordinates[Checkpoint.SHU_JING]),
        Checkpoint.ABBEY: dist(coordinates[Checkpoint.GAIPAN_VILLAGE], coordinates[Checkpoint.ABBEY]),
    },
    Checkpoint.BA_SING_SE: {
        Checkpoint.NORTHERN_AIR: dist(coordinates[Checkpoint.BA_SING_SE], coordinates[Checkpoint.NORTHERN_AIR]),
        Checkpoint.GAIPAN_VILLAGE: dist(coordinates[Checkpoint.BA_SING_SE], coordinates[Checkpoint.GAIPAN_VILLAGE]),
        Checkpoint.EASTERN_AIR: dist(coordinates[Checkpoint.BA_SING_SE], coordinates[Checkpoint.EASTERN_AIR]),
    },
    Checkpoint.SI_WONG: {
        Checkpoint.GAIPAN_VILLAGE: dist(coordinates[Checkpoint.SI_WONG], coordinates[Checkpoint.GAIPAN_VILLAGE]),
        Checkpoint.SHU_JING: dist(coordinates[Checkpoint.SI_WONG], coordinates[Checkpoint.SHU_JING]),
        Checkpoint.SOUTHERN_AIR: dist(coordinates[Checkpoint.SI_WONG], coordinates[Checkpoint.SOUTHERN_AIR]),
    },
    Checkpoint.SOUTHERN_AIR: {
        Checkpoint.SI_WONG: dist(coordinates[Checkpoint.SOUTHERN_AIR], coordinates[Checkpoint.SI_WONG]),
        Checkpoint.SHU_JING: dist(coordinates[Checkpoint.SOUTHERN_AIR], coordinates[Checkpoint.SHU_JING]),
        Checkpoint.SOUTHERN_WATER: dist(coordinates[Checkpoint.SOUTHERN_AIR], coordinates[Checkpoint.SOUTHERN_WATER]),
        Checkpoint.FIRE_CAPITAL: dist(coordinates[Checkpoint.SOUTHERN_AIR], coordinates[Checkpoint.FIRE_CAPITAL]),
    },
    Checkpoint.SOUTHERN_WATER: {
        Checkpoint.SOUTHERN_AIR: dist(coordinates[Checkpoint.SOUTHERN_WATER], coordinates[Checkpoint.SOUTHERN_AIR]),
    },
    Checkpoint.EASTERN_AIR: {
        Checkpoint.BA_SING_SE: dist(coordinates[Checkpoint.EASTERN_AIR], coordinates[Checkpoint.BA_SING_SE]),
        Checkpoint.SI_WONG: dist(coordinates[Checkpoint.EASTERN_AIR], coordinates[Checkpoint.SI_WONG]),
    },
}
