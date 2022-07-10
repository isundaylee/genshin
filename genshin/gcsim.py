from genshin import artifact, character, weapon
from typing import List


def artifact_stat_type_to_str(stat_type: artifact.ArtifactStatType) -> str:
    return {
        artifact.ArtifactStatType.HP: "hp",
        artifact.ArtifactStatType.EM: "em",
        artifact.ArtifactStatType.CR_PCT: "cr",
        artifact.ArtifactStatType.CD_PCT: "cd",
        artifact.ArtifactStatType.ATK: "atk",
        artifact.ArtifactStatType.DEF_PCT: "def%",
        artifact.ArtifactStatType.ER_PCT: "er",
        artifact.ArtifactStatType.EDP_PCT: "pyro%",
    }[stat_type]


def character_name_to_str(name: character.CharacterName) -> str:
    return {character.CharacterName.Yanfei: "yanfei"}[name]


def weapon_name_to_str(name: weapon.WeaponName) -> str:
    return {weapon.WeaponName.SkywardAtlas: "skywardatlas"}[name]


def generate_gcsim_config(characters: List[character.Character]) -> str:
    lines: List[str] = []

    for c in characters:
        lines.append(
            "{} char lvl={}/{} cons={} talent={},{},{};".format(
                character_name_to_str(c.name),
                c.level,
                c.level_cap,
                c.constellations,
                c.talent_level_a,
                c.talent_level_e,
                c.talent_level_q,
            )
        )

        lines.append(
            '{} add weapon="{}" refine={} lvl={}/{};'.format(
                character_name_to_str(c.name),
                weapon_name_to_str(c.weapon.name),
                c.weapon.refinements,
                c.weapon.level,
                c.weapon.level_cap,
            )
        )

        lines.append(
            "{} add stats {};".format(
                character_name_to_str(c.name),
                " ".join(
                    "{}={}".format(artifact_stat_type_to_str(t), v)
                    for t, v in c.combined_artifact_stats.items()
                ),
            )
        )

    return "\n".join(lines)
