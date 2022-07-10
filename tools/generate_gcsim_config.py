#!/usr/bin/env python3

from genshin import artifact, character, gcsim, weapon
import click


@click.command()
def main():
    wp_widsith = weapon.Weapon(
        name=weapon.WeaponName.TheWidsith,
        ascension=6,
        level=90,
        refinements=5,
    )

    wp_skyward_atlas = weapon.Weapon(
        name=weapon.WeaponName.SkywardAtlas,
        ascension=6,
        level=90,
        refinements=1,
    )

    wp_iron_sting = weapon.Weapon(
        name=weapon.WeaponName.IronSting,
        ascension=5,
        level=80,
        refinements=1,
    )

    wp_favonius_sword = weapon.Weapon(
        name=weapon.WeaponName.FavoniusSword,
        ascension=6,
        level=90,
        refinements=5,
    )

    wp_aquila_favonia = weapon.Weapon(
        name=weapon.WeaponName.AquilaFavonia,
        ascension=6,
        level=90,
        refinements=1,
    )

    wp_sacrificial_sword = weapon.Weapon(
        name=weapon.WeaponName.SacrificialSword,
        ascension=6,
        level=90,
        refinements=5,
    )

    yanfei = character.Character(
        name=character.CharacterName.Yanfei,
        ascension=6,
        level=90,
        constellations=6,
        talent_level_a=10,
        talent_level_e=10,
        talent_level_q=10,
        weapon=wp_skyward_atlas,
        artifacts=tuple(
            artifact.parse_artifact(a)
            for a in (
                "CW@1@20 HP=4780 EM=23 CD%=18.7 ATK=37 CR%=11.7",
                "CW@2@20 ATK=311 CR%=9.7 EM=56 CD%=7.8 ER%=4.5",
                "CW@3@20 EM=187 CR%=12.4 ATK=19 CD%=13.2 ER%=6.5",
                "LW@4@20 EDP%=46.6 CD%=12.4 HP=448 CR%=10.1 EM=23",
                "CW@5@20 CR%=31.1 CD%=33.4 HP=209 ATK=18 DEF%=5.8",
            )
        ),
    )

    kazuha = character.Character(
        name=character.CharacterName.Kazuha,
        ascension=6,
        level=80,
        constellations=0,
        talent_level_a=6,
        talent_level_e=6,
        talent_level_q=6,
        weapon=wp_iron_sting,
        artifacts=tuple(
            artifact.parse_artifact(a)
            for a in (
                "VV@1@20 HP=4780 ATK=35 CR%=15.5 EM=35 DEF=16",
                "VV@2@20 ATK=311 ER%=5.8 CD%=26.4 HP=448 EM=47",
                "VV@3@20 EM=187 ER%=16.2 DEF%=5.1 ATK%=13.4 ATK=16",
                "TF@4@20 EM=187 ATK=47 HP=508 CD%=14.8 ATK%=5.8",
                "VV@5@20 EM=187 DEF%=7.3 CR%=18.8 HP=598 ATK%=11.1",
            )
        ),
    )

    bennett = character.Character(
        name=character.CharacterName.Bennett,
        ascension=6,
        level=80,
        constellations=5,
        talent_level_a=1,
        talent_level_e=1,
        talent_level_q=9,
        weapon=wp_favonius_sword,
        artifacts=tuple(
            artifact.parse_artifact(a)
            for a in (
                "MB@1@20 HP=4780 ER%=11.7 CR%=14 CD%=16.2 EM=16",
                "NO@2@20 ATK=311 DEF=35 CD%=7.0 EM=35 ER%=17.5",
                "NO@3@20 ER%=51.8 CR%=6.2 CD%=17.9 DEF=19 DEF%=13.1",
                "NO@4@20 HP%=46.6 ER%=10.4 ATK=60 CR%=3.1 EM=21",
                "NO@5@20 CR%=31.1 ER%=9.7 EM=40 CD%=11.7 ATK=49",
            )
        ),
    )

    xingqiu = character.Character(
        name=character.CharacterName.Xingqiu,
        ascension=6,
        level=80,
        constellations=6,
        talent_level_a=1,
        talent_level_e=8,
        talent_level_q=8,
        weapon=wp_sacrificial_sword,
        artifacts=tuple(
            artifact.parse_artifact(a)
            for a in (
                "HD@1@20 HP=4780 ATK%=14.0 ER%=11.0 CR%=6.2 ATK=14",
                "NO@2@20 ATK=311 HP%=4.1 CR%=9.7 DEF%=13.9 CD%=15.5",
                "NO@3@20 ATK%=46.6 CR%=9.3 DEF=21 ER%=10.4 DEF%=11.7",
                "CW@4@20 EDH%=46.6 HP%=11.1 CD%=7.0 ATK%=9.9 ER%=20.7",
                "HD@5@20 CR%=31.1 CD%=13.2 DEF=21 ATK%=18.1 HP=269",
            )
        ),
    )

    print(
        gcsim.generate_gcsim_config(
            [xingqiu, yanfei, kazuha, bennett],
            actions=[
                # Options
                "options swap_delay=12 mode=apl duration=70.0;",
                "energy every interval=480,720 amount=1;",
                # General macros
                "xingqiu_eq: xingqiu skill[orbital=1],burst[orbital=1];",
                "xingqiu_e: xingqiu skill[orbital=1];",
                "bennett_ea: bennett skill,attack;",
                "wait_p_xingqiu: wait_for particles value=xingqiu max=200;",
                "wait_p_bennett: wait_for particles value=bennett max=200;",
                "yanfei_swap: yanfei swap;",
                "xingqiu_swap: xingqiu swap;",
                # Xingqiu sac sword woes
                "chain xingqiu_eq,wait_p_xingqiu;",
                "chain xingqiu_e,wait_p_xingqiu +if=.status.xqburst>720;",
                # Bennett + Kazuha setup
                "bennett skill,attack,burst,attack +if=.status.xqburst>300;",
                "kazuha skill[hold=1],high_plunge,attack +if=.status.btburst>0;",
                # Yanfei rotation
                "yanfei_wait_bt: wait_for mods value=.yanfei.bennett-field==1 max=100;",
                "yanfei_q_rotation: yanfei attack,skill,attack,burst,attack,charge,attack:2,charge,attack,charge,attack:2,charge,attack,skill,charge;",
                "yanfei_noq_rotation: yanfei attack,skill,attack,charge,attack:3,charge,attack,charge,attack:3,charge,attack,skill,charge;",
                "chain yanfei_swap,yanfei_wait_bt,yanfei_q_rotation +if=.status.btburst>0&&.status.xqburst>300;",
                "chain yanfei_swap,yanfei_wait_bt,yanfei_noq_rotation +if=.status.btburst>0&&.status.xqburst>300;",
                # Fav Bennett funnel
                "chain bennett_ea,xingqiu_swap,wait_p_bennett +if=.energy.xingqiu<80;",
                "chain bennett_ea,wait_p_bennett +if=.energy.bennett<40;",
                # Gap fill
                "bennett skill;",
                "bennett attack +is_onfield;",
            ],
            target="target lvl=90 resist=0.1;",
        )
    )


if __name__ == "__main__":
    main()
