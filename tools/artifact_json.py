import enum
import json
from typing import List

from genshin import artifact

import attr


artifacts = [
    artifact.parse_artifact(desc)
    for desc in [
        # BS
        "BS@1@20 HP=4780 ATK%=9.9 ER%=11.0 CR%=5.8 CD%=17.9",
        "BS@2@20 ATK=311 DEF=39 CD%=12.4 CR%=7.4 DEF%=19.0",
        "BS@3@20 ATK%=46.6 DEF=23 ATK=54 DEF%=17.5 CR%=3.9",
        "BS@1@20 HP=4780 ATK=16 CD%=26.4 DEF=19 ER%=10.4",
        "BS@5@20 CD%=62.2 CR%=14.0 DEF=19 EM=21 ATK=35",
        "BS@2@20 ATK=311 CD%=18.7 HP=538 CR%=7.0 DEF=23",
        # TS
        "TS@4@20 EDP%=46.6 DEF=23 DEF%=12.4 CR%=14.4 HP=209",
        # LW
        "LW@3@20 ATK%=46.6 CR%=7.0 CD%=7.0 HP%=5.3 HP=1016",
        "LW@5@20 CR%=31.1 CD%=13.2 ATK%=8.2 HP%=13.4 HP=239",
        "LW@4@20 EDP%=46.6 CD%=12.4 HP=448 CR%=10.1 EM=23",
        "LW@4@20 EDP%=46.6 CD%=12.4 HP=448 CR%=10.1 EM=23",
        # MB
        "MB@4@20 HP%=46.6 EM=65 HP=1135 ATK=19 ATK%=5.8",
        "MB@3@20 HP%=46.6 HP=747 EM=16 ATK%=10.5 DEF=37",
        "MB@1@20 HP=4780 ER%=11.7 CR%=14 CD%=16.2 EM=16",
        "MB@2@20 ATK=311 ER%=11.0 HP%=8.7 EM=23 DEF=60",
        # GF
        "GF@5@20 CD%=62.2 CR%=6.2 HP=717 HP%=14.6 ATK%=5.8",
        "GF@2@20 ATK=311 CD%=14.8 HP=986 CR%=6.2 ER%=6.5",
        "GF@4@20 EDE%=46.6 HP=418 ATK=37 CD%=24.1 ATK%=5.3",
        "GF@4@20 EDC%=46.6 ATK=18 CD%=20.2 HP%=10.5 ATK%=15.2",
        "GF@1@20 HP=4780 ATK=18 CD%=21.0 CR%=6.6 ATK%=11.7",
        "GF@5@20 HP%=46.6 CD%=18.7 CR%=6.2 HP=299 DEF=46",
        "GF@5@20 CR%=31.1 HP=239 DEF%=19.7 HP%=9.3 ATK=33",
        "GF@2@20 ATK=311 ATK%=8.7 HP=209 CR%=6.6 CD%=19.4",
        "GF@2@20 ATK=311 CD%=14.0 DEF=56 ATK%=11.1 CR%=3.9",
        "GF@4@20 PD%=58.3 ATK=56 DEF=35 CD%=7.8 HP%=9.3",
        # VV
        "VV@2@20 ATK=311 ER%=5.8 CD%=26.4 HP=448 EM=47",
        "VV@4@20 EM=187 DEF%=10.9 HP=777 ATK%=5.8 CD%=18.7",
        "VV@3@20 EM=187 ER%=16.2 DEF%=5.1 ATK%=13.4 ATK=16",
        "VV@1@20 HP=4780 EM=23 ER%=10.4 ATK%=10.5 CD%=17.1",
        "VV@1@20 HP=4780 ATK=35 CR%=15.5 EM=35 DEF=16",
        "VV@5@20 EM=187 DEF%=7.3 CR%=18.8 HP=598 ATK%=11.1",
        "VV@2@20 ATK=311 EM=40 ER%=16.2 DEF%=6.6 ATK%=9.9",
        # WT
        "WT@3@20 HP%=46.6 CR%=10.5 ATK%=10.5 CD%=11.7 ATK=33",
        "WT@2@20 ATK=311 CD%=14.8 CR%=6.6 DEF=21 EM=72",
        "WT@4@20 EDG%=46.6 CR%=13.2 CD%=5.4 ATK=37 ATK%=8.7",
        "WT@5@20 CR%=31.1 ATK%=5.8 CD%=7.0 DEF=69 DEF%=17.5",
        "WT@5@20 HP%=46.6 CD%=13.2 DEF%=6.6 ER%=9.7 HP=657",
        # TF
        "TF@4@20 EM=187 ATK=47 HP=508 CD%=14.8 ATK%=5.8",
        # CW
        "CW@3@20 ATK%=46.6 DEF=23 HP=508 EM=40 CD%=26.4",
        "CW@1@20 HP=4780 EM=23 CD%=18.7 ATK=37 CR%=11.7",
        "CW@1@20 HP=4780 ER%=13.0 ATK%=11.7 CD%=12.4 ATK=45",
        "CW@4@20 EDH%=46.6 HP%=11.1 CD%=7.0 ATK%=9.9 ER%=20.7",
        "CW@3@20 EM=187 CR%=12.4 ATK=19 CD%=13.2 ER%=6.5",
        "CW@3@20 HP%=46.6 DEF=37 ATK=19 CD%=19.4 CR%=7.0",
        "CW@3@20 ATK%=46.6 HP%=14.6 CD%=6.2 DEF=19 DEF%=20.4",
        "CW@1@20 HP=4780 ATK%=4.1 CD%=14.0 CR%=7.4 EM=54",
        "CW@5@20 CR%=31.1 CD%=33.4 HP=209 ATK=18 DEF%=5.8",
        "CW@5@20 CR%=31.1 DEF=35 ATK=19 HP=598 DEF%=17.5",
        "CW@2@20 ATK=311 CR%=3.1 ATK%=10.5 EM=40 CD%=19.4",
        "CW@2@20 ATK=311 HP=239 CD%=20.2 CR%=2.7 ATK%=17.5",
        "CW@2@20 ATK=311 CR%=9.7 EM=56 CD%=7.8 ER%=4.5",
        "CW@4@20 EDP%=46.6 CR%=2.7 HP=687 ER%=12.3 CD%=14.8",
        "CW@4@20 EDP%=46.6 ER%=11.7 EM=37 ATK%=12.8 DEF=16",
        # NO
        "NO@3@20 HP%=46.6 ER%=12.3 EM=56 CR%=6.6 DEF%=11.7",
        "NO@4@20 EDG%=46.6 CD%=19.4 ATK%=9.9 CR%=2.7 DEF=58",
        "NO@3@20 ATK%=46.6 ER%=16.2 CD%=5.4 HP=508 DEF=39",
        "NO@3@20 ATK%=46.6 CR%=9.3 DEF=21 ER%=10.4 DEF%=11.7",
        "NO@1@20 HP=4780 ER%=5.2 CD%=14.0 HP%=9.3 CR%=9.3",
        "NO@1@20 HP=4780 HP%=15.7 CR%=7.8 ATK=39 ATK%=5.8",
        "NO@5@20 HP%=46.6 DEF%=10.2 ER%=5.8 CR%=3.5 ATK=64",
        "NO@2@20 ATK=311 HP%=4.1 CR%=9.7 DEF%=13.9 CD%=15.5",
        "NO@2@20 ATK=311 CD%=20.2 HP=508 CR%=3.5 EM=42",
        "NO@2@20 ATK=311 CR%=14.0 HP%=4.1 CD%=5.4 HP=598",
        "NO@4@20 HP%=46.6 ER%=10.4 ATK=60 CR%=3.1 EM=21",
        "NO@4@20 HP%=46.6 ER%=10.4 ATK=60 CR%=3.1 EM=21",
        # AP
        "AP@1@20 HP=4780 EM=19 CD%=14.0 DEF%=12.4 HP%=15.2",
        # HD
        "HD@1@20 HP=4780 ATK%=14.0 ER%=11.0 CR%=6.2 ATK=14",
        "HD@5@20 CR%=31.1 CD%=13.2 DEF=21 ATK%=18.1 HP=269",
        "HD@5@20 CD%=62.2 ATK=18 HP%=18.7 CR%=3.1 HP=568",
        "HD@4@20 EDE%=46.6 CD%=19.4 HP=538 CR%=3.5 DEF=44",
        # SR
        "SR@2@20 ATK=311 CR%=10.5 HP=538 ATK%=9.9 ER%=10.4",
        "SR@3@20 HP%=46.6 ER%=6.5 ATK=16 CD%=14.8 EM=79",
        "SR@3@20 ATK%=46.6 CR%=7.0 ATK=31 EM=68 HP=209",
        "SR@1@20 HP=4780 DEF%=6.6 CR%=6.2 EM=61 ATK%=10.5",
        "SR@1@20 HP=4780 ER%=15.5 CR%=7.0 DEF=39 CD%=5.4",
        "SR@5@20 CR%=31.1 CD%=18.7 DEF=19 ATK=33 HP%=10.5",
        "SR@5@20 CD%=62.2 CR%=9.3 HP=209 ER%=17.5 ATK=18",
        "SR@2@20 ATK=311 CD%=17.1 DEF=21 ATK%=4.7 CR%=10.5",
        "SR@4@20 EDE%=46.6 CD%=13.2 ATK=18 ER%=24.0 DEF=23",
        # ESF
        "ESF@2@20 ATK=311 HP=448 HP%=8.7 CR%=7.4 ER%=14.9",
        "ESF@3@20 ER%=51.8 EM=33 CD%=19.4 DEF%=12.4 HP=299",
        "ESF@3@20 ER%=51.8 ATK=18 CR%=9.7 HP%=9.3 EM=38",
        "ESF@1@20 HP=4780 EM=23 ATK%=9.9 CD%=28.8 DEF=19",
        "ESF@5@20 CR%=31.1 ER%=16.2 CD%=12.4 DEF%=5.1 ATK%=11.7",
    ]
]

print(json.dumps(artifact.to_dict(artifacts)))