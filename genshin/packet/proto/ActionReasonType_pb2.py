# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/ActionReasonType.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+genshin/packet/proto/ActionReasonType.proto*\x81?\n\x10\x41\x63tionReasonType\x12\x16\n\x12\x41\x43TION_REASON_NONE\x10\x00\x12\x1c\n\x18\x41\x43TION_REASON_QUEST_ITEM\x10\x01\x12\x1e\n\x1a\x41\x43TION_REASON_QUEST_REWARD\x10\x02\x12\x18\n\x14\x41\x43TION_REASON_TRIFLE\x10\x03\x12\x16\n\x12\x41\x43TION_REASON_SHOP\x10\x04\x12\'\n#ACTION_REASON_PLAYER_UPGRADE_REWARD\x10\x05\x12\x1c\n\x18\x41\x43TION_REASON_ADD_AVATAR\x10\x06\x12#\n\x1f\x41\x43TION_REASON_GADGET_ENV_ANIMAL\x10\x07\x12$\n ACTION_REASON_MONSTER_ENV_ANIMAL\x10\x08\x12\x1a\n\x16\x41\x43TION_REASON_COMPOUND\x10\t\x12\x16\n\x12\x41\x43TION_REASON_COOK\x10\n\x12\x18\n\x14\x41\x43TION_REASON_GATHER\x10\x0b\x12!\n\x1d\x41\x43TION_REASON_MAIL_ATTACHMENT\x10\x0c\x12%\n!ACTION_REASON_CITY_LEVELUP_RETURN\x10\x0f\x12%\n!ACTION_REASON_CITY_LEVELUP_REWARD\x10\x11\x12%\n!ACTION_REASON_AREA_EXPLORE_REWARD\x10\x12\x12%\n!ACTION_REASON_UNLOCK_POINT_REWARD\x10\x13\x12$\n ACTION_REASON_DUNGEON_FIRST_PASS\x10\x14\x12\x1e\n\x1a\x41\x43TION_REASON_DUNGEON_PASS\x10\x15\x12\"\n\x1e\x41\x43TION_REASON_CHANGE_ELEM_TYPE\x10\x17\x12\x1d\n\x19\x41\x43TION_REASON_FETTER_OPEN\x10\x19\x12\"\n\x1e\x41\x43TION_REASON_DAILY_TASK_SCORE\x10\x1a\x12!\n\x1d\x41\x43TION_REASON_DAILY_TASK_HOST\x10\x1b\x12 \n\x1c\x41\x43TION_REASON_RAND_TASK_HOST\x10\x1c\x12\x1c\n\x18\x41\x43TION_REASON_EXPEDITION\x10\x1d\x12\x17\n\x13\x41\x43TION_REASON_GACHA\x10\x1e\x12\x19\n\x15\x41\x43TION_REASON_COMBINE\x10\x1f\x12!\n\x1d\x41\x43TION_REASON_RAND_TASK_GUEST\x10 \x12\"\n\x1e\x41\x43TION_REASON_DAILY_TASK_GUEST\x10!\x12\x1e\n\x1a\x41\x43TION_REASON_FORGE_OUTPUT\x10\"\x12\x1e\n\x1a\x41\x43TION_REASON_FORGE_RETURN\x10#\x12\x1d\n\x19\x41\x43TION_REASON_INIT_AVATAR\x10$\x12\x1d\n\x19\x41\x43TION_REASON_MONSTER_DIE\x10%\x12\x14\n\x10\x41\x43TION_REASON_GM\x10&\x12\x1c\n\x18\x41\x43TION_REASON_OPEN_CHEST\x10\'\x12\x1c\n\x18\x41\x43TION_REASON_GADGET_DIE\x10(\x12#\n\x1f\x41\x43TION_REASON_MONSTER_CHANGE_HP\x10)\x12\x1f\n\x1b\x41\x43TION_REASON_SUBFIELD_DROP\x10*\x12\"\n\x1e\x41\x43TION_REASON_PUSH_TIPS_REWARD\x10+\x12\'\n#ACTION_REASON_ACTIVITY_MONSTER_DROP\x10,\x12!\n\x1d\x41\x43TION_REASON_ACTIVITY_GATHER\x10-\x12(\n$ACTION_REASON_ACTIVITY_SUBFIELD_DROP\x10.\x12\'\n#ACTION_REASON_TOWER_SCHEDULE_REWARD\x10/\x12)\n%ACTION_REASON_TOWER_FLOOR_STAR_REWARD\x10\x30\x12)\n%ACTION_REASON_TOWER_FIRST_PASS_REWARD\x10\x31\x12$\n ACTION_REASON_TOWER_DAILY_REWARD\x10\x32\x12+\n\'ACTION_REASON_HIT_CLIENT_TRIVIAL_ENTITY\x10\x33\x12\'\n#ACTION_REASON_OPEN_WORLD_BOSS_CHEST\x10\x34\x12(\n$ACTION_REASON_MATERIAL_DELETE_RETURN\x10\x35\x12 \n\x1c\x41\x43TION_REASON_SIGN_IN_REWARD\x10\x36\x12$\n ACTION_REASON_OPEN_BLOSSOM_CHEST\x10\x37\x12\x1a\n\x16\x41\x43TION_REASON_RECHARGE\x10\x38\x12\'\n#ACTION_REASON_BONUS_ACTIVITY_REWARD\x10\x39\x12,\n(ACTION_REASON_TOWER_COMMEMORATIVE_REWARD\x10:\x12)\n%ACTION_REASON_TOWER_SKIP_FLOOR_REWARD\x10;\x12 \n\x1c\x41\x43TION_REASON_RECHARGE_BONUS\x10<\x12\x1f\n\x1b\x41\x43TION_REASON_RECHARGE_CARD\x10=\x12%\n!ACTION_REASON_RECHARGE_CARD_DAILY\x10>\x12\'\n#ACTION_REASON_RECHARGE_CARD_REPLACE\x10?\x12,\n(ACTION_REASON_RECHARGE_CARD_REPLACE_FREE\x10@\x12\'\n#ACTION_REASON_RECHARGE_PLAY_REPLACE\x10\x41\x12%\n!ACTION_REASON_MP_PLAY_TAKE_REWARD\x10\x42\x12\"\n\x1e\x41\x43TION_REASON_ACTIVITY_WATCHER\x10\x43\x12\'\n#ACTION_REASON_SALESMAN_DELIVER_ITEM\x10\x44\x12!\n\x1d\x41\x43TION_REASON_SALESMAN_REWARD\x10\x45\x12\x18\n\x14\x41\x43TION_REASON_REBATE\x10\x46\x12&\n\"ACTION_REASON_MCOIN_EXCHANGE_HCOIN\x10G\x12\x33\n/ACTION_REASON_DAILY_TASK_EXCHANGE_LEGENDARY_KEY\x10H\x12$\n ACTION_REASON_UNLOCK_PERSON_LINE\x10I\x12%\n!ACTION_REASON_FETTER_LEVEL_REWARD\x10J\x12\x1b\n\x17\x41\x43TION_REASON_BUY_RESIN\x10K\x12\"\n\x1e\x41\x43TION_REASON_RECHARGE_PACKAGE\x10L\x12\'\n#ACTION_REASON_DELIVERY_DAILY_REWARD\x10M\x12\'\n#ACTION_REASON_CITY_REPUTATION_LEVEL\x10N\x12\'\n#ACTION_REASON_CITY_REPUTATION_QUEST\x10O\x12)\n%ACTION_REASON_CITY_REPUTATION_REQUEST\x10P\x12)\n%ACTION_REASON_CITY_REPUTATION_EXPLORE\x10Q\x12!\n\x1d\x41\x43TION_REASON_OFFERGING_LEVEL\x10R\x12\x1e\n\x1a\x41\x43TION_REASON_ROUTINE_HOST\x10S\x12\x1f\n\x1b\x41\x43TION_REASON_ROUTINE_GUEST\x10T\x12)\n%ACTION_REASON_TREASURE_MAP_SPOT_TOKEN\x10Y\x12\x31\n-ACTION_REASON_TREASURE_MAP_BONUS_LEVEL_REWARD\x10Z\x12(\n$ACTION_REASON_TREASURE_MAP_MP_REWARD\x10[\x12\x19\n\x15\x41\x43TION_REASON_CONVERT\x10\\\x12$\n ACTION_REASON_OVERFLOW_TRANSFORM\x10]\x12\x32\n.ACTION_REASON_ACTIVITY_AVATAR_SELECTION_REWARD\x10`\x12(\n$ACTION_REASON_ACTIVITY_WATCHER_BATCH\x10\x61\x12\x1f\n\x1b\x41\x43TION_REASON_HIT_TREE_DROP\x10\x62\x12)\n%ACTION_REASON_GET_HOME_LEVELUP_REWARD\x10\x63\x12(\n$ACTION_REASON_HOME_DEFAULT_FURNITURE\x10\x64\x12\x1f\n\x1b\x41\x43TION_REASON_ACTIVITY_COND\x10\x65\x12$\n ACTION_REASON_BATTLE_PASS_NOTIFY\x10\x66\x12%\n!ACTION_REASON_RELIQUARY_DECOMPOSE\x10g\x12+\n\'ACTION_REASON_RECHARGE_GOOGLE_GIFT_GARD\x10h\x12*\n&ACTION_REASON_RECHARGE_CONCERT_PRODUCT\x10i\x12\x32\n.ACTION_REASON_RECHARGE_CONCERT_PRODUCT_REPLACE\x10j\x12.\n*ACTION_REASON_SEND_CONCERT_PRODUCT_BY_MUIP\x10k\x12*\n&ACTION_REASON_RECHARGE_APPLE_GIFT_GARD\x10l\x12\"\n\x1d\x41\x43TION_REASON_PLAYER_USE_ITEM\x10\xe9\x07\x12\x1c\n\x17\x41\x43TION_REASON_DROP_ITEM\x10\xea\x07\x12!\n\x1c\x41\x43TION_REASON_WEAPON_UPGRADE\x10\xf3\x07\x12!\n\x1c\x41\x43TION_REASON_WEAPON_PROMOTE\x10\xf4\x07\x12 \n\x1b\x41\x43TION_REASON_WEAPON_AWAKEN\x10\xf5\x07\x12 \n\x1b\x41\x43TION_REASON_RELIC_UPGRADE\x10\xf6\x07\x12\x1a\n\x15\x41\x43TION_REASON_ABILITY\x10\xf7\x07\x12&\n!ACTION_REASON_DUNGEON_STATUE_DROP\x10\xf8\x07\x12\x1e\n\x19\x41\x43TION_REASON_OFFLINE_MSG\x10\xf9\x07\x12!\n\x1c\x41\x43TION_REASON_AVATAR_UPGRADE\x10\xfa\x07\x12!\n\x1c\x41\x43TION_REASON_AVATAR_PROMOTE\x10\xfb\x07\x12\x1f\n\x1a\x41\x43TION_REASON_QUEST_ACTION\x10\xfd\x07\x12\x1f\n\x1a\x41\x43TION_REASON_CITY_LEVELUP\x10\xfe\x07\x12 \n\x1b\x41\x43TION_REASON_UPGRADE_SKILL\x10\x80\x08\x12 \n\x1b\x41\x43TION_REASON_UNLOCK_TALENT\x10\x81\x08\x12&\n!ACTION_REASON_UPGRADE_PROUD_SKILL\x10\x82\x08\x12(\n#ACTION_REASON_PLAYER_LEVEL_LIMIT_UP\x10\x83\x08\x12 \n\x1b\x41\x43TION_REASON_DUNGEON_DAILY\x10\x84\x08\x12\x1e\n\x19\x41\x43TION_REASON_ITEM_GIVING\x10\x86\x08\x12\x1d\n\x18\x41\x43TION_REASON_FORGE_COST\x10\x87\x08\x12\'\n\"ACTION_REASON_INVESTIGATION_REWARD\x10\x88\x08\x12.\n)ACTION_REASON_INVESTIGATION_TARGET_REWARD\x10\x89\x08\x12\"\n\x1d\x41\x43TION_REASON_GADGET_INTERACT\x10\x8a\x08\x12\'\n\"ACTION_REASON_SEA_LAMP_CI_MATERIAL\x10\x8c\x08\x12/\n*ACTION_REASON_SEA_LAMP_CONTRIBUTION_REWARD\x10\x8d\x08\x12(\n#ACTION_REASON_SEA_LAMP_PHASE_REWARD\x10\x8e\x08\x12$\n\x1f\x41\x43TION_REASON_SEA_LAMP_FLY_LAMP\x10\x8f\x08\x12\x1f\n\x1a\x41\x43TION_REASON_AUTO_RECOVER\x10\x90\x08\x12\'\n\"ACTION_REASON_ACTIVITY_EXPIRE_ITEM\x10\x91\x08\x12$\n\x1f\x41\x43TION_REASON_SUB_COIN_NEGATIVE\x10\x92\x08\x12!\n\x1c\x41\x43TION_REASON_BARGAIN_DEDUCT\x10\x93\x08\x12*\n%ACTION_REASON_BATTLE_PASS_PAID_REWARD\x10\x94\x08\x12+\n&ACTION_REASON_BATTLE_PASS_LEVEL_REWARD\x10\x95\x08\x12:\n5ACTION_REASON_TRIAL_AVATAR_ACTIVITY_FIRST_PASS_REWARD\x10\x96\x08\x12(\n#ACTION_REASON_BUY_BATTLE_PASS_LEVEL\x10\x97\x08\x12)\n$ACTION_REASON_GRANT_BIRTHDAY_BENEFIT\x10\x98\x08\x12%\n ACTION_REASON_ACHIEVEMENT_REWARD\x10\x99\x08\x12*\n%ACTION_REASON_ACHIEVEMENT_GOAL_REWARD\x10\x9a\x08\x12\x30\n+ACTION_REASON_FIRST_SHARE_TO_SOCIAL_NETWORK\x10\x9b\x08\x12#\n\x1e\x41\x43TION_REASON_DESTROY_MATERIAL\x10\x9c\x08\x12\'\n\"ACTION_REASON_CODEX_LEVELUP_REWARD\x10\x9d\x08\x12\'\n\"ACTION_REASON_HUNTING_OFFER_REWARD\x10\x9e\x08\x12*\n%ACTION_REASON_USE_WIDGET_ANCHOR_POINT\x10\x9f\x08\x12%\n ACTION_REASON_USE_WIDGET_BONFIRE\x10\xa0\x08\x12\x31\n,ACTION_REASON_UNGRADE_WEAPON_RETURN_MATERIAL\x10\xa1\x08\x12:\n5ACTION_REASON_USE_WIDGET_ONEOFF_GATHER_POINT_DETECTOR\x10\xa2\x08\x12.\n)ACTION_REASON_USE_WIDGET_CLIENT_COLLECTOR\x10\xa3\x08\x12-\n(ACTION_REASON_USE_WIDGET_CLIENT_DETECTOR\x10\xa4\x08\x12&\n!ACTION_REASON_TAKE_GENERAL_REWARD\x10\xa5\x08\x12,\n\'ACTION_REASON_ASTER_TAKE_SPECIAL_REWARD\x10\xa6\x08\x12$\n\x1f\x41\x43TION_REASON_REMOVE_CODEX_BOOK\x10\xa7\x08\x12 \n\x1b\x41\x43TION_REASON_OFFERING_ITEM\x10\xa8\x08\x12,\n\'ACTION_REASON_USE_WIDGET_GADGET_BUILDER\x10\xa9\x08\x12+\n&ACTION_REASON_EFFIGY_FIRST_PASS_REWARD\x10\xaa\x08\x12 \n\x1b\x41\x43TION_REASON_EFFIGY_REWARD\x10\xab\x08\x12,\n\'ACTION_REASON_REUNION_FIRST_GIFT_REWARD\x10\xac\x08\x12)\n$ACTION_REASON_REUNION_SIGN_IN_REWARD\x10\xad\x08\x12)\n$ACTION_REASON_REUNION_WATCHER_REWARD\x10\xae\x08\x12%\n ACTION_REASON_SALESMAN_MP_REWARD\x10\xaf\x08\x12)\n$ACTION_REASION_AVATAR_PROMOTE_REWARD\x10\xb0\x08\x12)\n$ACTION_REASON_BLESSING_REDEEM_REWARD\x10\xb1\x08\x12\x1f\n\x1a\x41\x43TION_MIRACLE_RING_REWARD\x10\xb2\x08\x12$\n\x1f\x41\x43TION_REASON_EXPEDITION_REWARD\x10\xb3\x08\x12/\n*ACTION_REASON_TREASURE_MAP_REMOVE_DETECTOR\x10\xb4\x08\x12,\n\'ACTION_REASON_MECHANICUS_DUNGEON_TICKET\x10\xb5\x08\x12*\n%ACTION_REASON_MECHANICUS_LEVELUP_GEAR\x10\xb6\x08\x12+\n&ACTION_REASON_MECHANICUS_BATTLE_SETTLE\x10\xb7\x08\x12\'\n\"ACTION_REASON_REGION_SEARCH_REWARD\x10\xb8\x08\x12&\n!ACTION_REASON_UNLOCK_COOP_CHAPTER\x10\xb9\x08\x12#\n\x1e\x41\x43TION_REASON_TAKE_COOP_REWARD\x10\xba\x08\x12,\n\'ACTION_REASON_FLEUR_FAIR_DUNGEON_REWARD\x10\xbb\x08\x12!\n\x1c\x41\x43TION_REASON_ACTIVITY_SCORE\x10\xbc\x08\x12\x38\n3ACTION_REASON_CHANNELLER_SLAB_ONEOFF_DUNGEON_REWARD\x10\xbd\x08\x12\'\n\"ACTION_REASON_FURNITURE_MAKE_START\x10\xbe\x08\x12&\n!ACTION_REASON_FURNITURE_MAKE_TAKE\x10\xbf\x08\x12(\n#ACTION_REASON_FURNITURE_MAKE_CANCEL\x10\xc0\x08\x12-\n(ACTION_REASON_FURNITURE_MAKE_FAST_FINISH\x10\xc1\x08\x12\x41\n<ACTION_REASON_CHANNELLER_SLAB_LOOP_DUNGEON_FIRST_PASS_REWARD\x10\xc2\x08\x12<\n7ACTION_REASON_CHANNELLER_SLAB_LOOP_DUNGEON_SCORE_REWARD\x10\xc3\x08\x12(\n#ACTION_REASON_HOME_LIMITED_SHOP_BUY\x10\xc4\x08\x12$\n\x1f\x41\x43TION_REASON_HOME_COIN_COLLECT\x10\xc5\x08\x12\x32\n-ACTION_REASON_SUMMER_TIME_SENTRY_TOWER_REWARD\x10\xc6\x08\x12\x31\n,ACTION_REASON_SUMMER_TIME_SPRINT_BOAT_REWARD\x10\xc7\x08\x12*\n%ACTION_REASON_SUMMER_TIME_BOSS_REWARD\x10\xc8\x08\x12*\n%ACTION_REASON_SUMMER_TIME_BOMB_REWARD\x10\xc9\x08\x12&\n!ACTION_REASON_HOME_FETTER_COLLECT\x10\xca\x08\x12$\n\x1f\x41\x43TION_REASON_ECHO_SHELL_REWARD\x10\xcb\x08\x12$\n\x1f\x41\x43TION_REASON_HOME_EVENT_REWARD\x10\xcc\x08\x12,\n\'ACTION_REASON_BLITZ_RUSH_DUNGEON_REWARD\x10\xcd\x08\x12(\n#ACTION_REASON_FURNITURE_MAKE_RETURN\x10\xce\x08\x12(\n#ACTION_REASON_HOME_PLANT_BOX_GATHER\x10\xcf\x08\x12\"\n\x1d\x41\x43TION_REASON_HOME_PLANT_SEED\x10\xd0\x08\x12$\n\x1f\x41\x43TION_REASON_HOME_PLANT_GATHER\x10\xd1\x08\x12\'\n\"ACTION_REASON_CHESS_DUNGEON_REWARD\x10\xd2\x08\x12+\n&ACTION_REASON_GROUP_LINK_BUNDLE_FINISH\x10\xd3\x08\x12&\n!ACTION_REASON_LUNA_RITE_SACRIFICE\x10\xd4\x08\x12\x32\n-ACTION_REASON_LUNA_RITE_TAKE_SACRIFICE_REWARD\x10\xd5\x08\x12\x1c\n\x17\x41\x43TION_REASON_FISH_BITE\x10\xd6\x08\x12\x1c\n\x17\x41\x43TION_REASON_FISH_SUCC\x10\xd7\x08\x12&\n!ACTION_REASON_PLANT_FLOWER_REWARD\x10\xd8\x08\x12,\n\'ACTION_REASON_PLANT_FLOWER_DELIVER_ITEM\x10\xd9\x08\x12+\n&ACTION_REASON_PLANT_FLOWER_GIVE_FLOWER\x10\xda\x08\x12+\n&ACTION_REASON_PLANT_FLOWER_RECV_FLOWER\x10\xdb\x08\x12)\n$ACTION_REASON_ROGUE_CHALLENGE_SETTLE\x10\xdc\x08\x12/\n*ACTION_REASON_ROGUE_TAKE_FIRST_PASS_REWARD\x10\xdd\x08\x12*\n%ACTION_REASON_ROGUE_UPGRADE_SHIKIGAMI\x10\xde\x08\x12%\n ACTION_REASON_ROGUE_REFRESH_CARD\x10\xdf\x08\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_ACTIONREASONTYPE = DESCRIPTOR.enum_types_by_name['ActionReasonType']
ActionReasonType = enum_type_wrapper.EnumTypeWrapper(_ACTIONREASONTYPE)
ACTION_REASON_NONE = 0
ACTION_REASON_QUEST_ITEM = 1
ACTION_REASON_QUEST_REWARD = 2
ACTION_REASON_TRIFLE = 3
ACTION_REASON_SHOP = 4
ACTION_REASON_PLAYER_UPGRADE_REWARD = 5
ACTION_REASON_ADD_AVATAR = 6
ACTION_REASON_GADGET_ENV_ANIMAL = 7
ACTION_REASON_MONSTER_ENV_ANIMAL = 8
ACTION_REASON_COMPOUND = 9
ACTION_REASON_COOK = 10
ACTION_REASON_GATHER = 11
ACTION_REASON_MAIL_ATTACHMENT = 12
ACTION_REASON_CITY_LEVELUP_RETURN = 15
ACTION_REASON_CITY_LEVELUP_REWARD = 17
ACTION_REASON_AREA_EXPLORE_REWARD = 18
ACTION_REASON_UNLOCK_POINT_REWARD = 19
ACTION_REASON_DUNGEON_FIRST_PASS = 20
ACTION_REASON_DUNGEON_PASS = 21
ACTION_REASON_CHANGE_ELEM_TYPE = 23
ACTION_REASON_FETTER_OPEN = 25
ACTION_REASON_DAILY_TASK_SCORE = 26
ACTION_REASON_DAILY_TASK_HOST = 27
ACTION_REASON_RAND_TASK_HOST = 28
ACTION_REASON_EXPEDITION = 29
ACTION_REASON_GACHA = 30
ACTION_REASON_COMBINE = 31
ACTION_REASON_RAND_TASK_GUEST = 32
ACTION_REASON_DAILY_TASK_GUEST = 33
ACTION_REASON_FORGE_OUTPUT = 34
ACTION_REASON_FORGE_RETURN = 35
ACTION_REASON_INIT_AVATAR = 36
ACTION_REASON_MONSTER_DIE = 37
ACTION_REASON_GM = 38
ACTION_REASON_OPEN_CHEST = 39
ACTION_REASON_GADGET_DIE = 40
ACTION_REASON_MONSTER_CHANGE_HP = 41
ACTION_REASON_SUBFIELD_DROP = 42
ACTION_REASON_PUSH_TIPS_REWARD = 43
ACTION_REASON_ACTIVITY_MONSTER_DROP = 44
ACTION_REASON_ACTIVITY_GATHER = 45
ACTION_REASON_ACTIVITY_SUBFIELD_DROP = 46
ACTION_REASON_TOWER_SCHEDULE_REWARD = 47
ACTION_REASON_TOWER_FLOOR_STAR_REWARD = 48
ACTION_REASON_TOWER_FIRST_PASS_REWARD = 49
ACTION_REASON_TOWER_DAILY_REWARD = 50
ACTION_REASON_HIT_CLIENT_TRIVIAL_ENTITY = 51
ACTION_REASON_OPEN_WORLD_BOSS_CHEST = 52
ACTION_REASON_MATERIAL_DELETE_RETURN = 53
ACTION_REASON_SIGN_IN_REWARD = 54
ACTION_REASON_OPEN_BLOSSOM_CHEST = 55
ACTION_REASON_RECHARGE = 56
ACTION_REASON_BONUS_ACTIVITY_REWARD = 57
ACTION_REASON_TOWER_COMMEMORATIVE_REWARD = 58
ACTION_REASON_TOWER_SKIP_FLOOR_REWARD = 59
ACTION_REASON_RECHARGE_BONUS = 60
ACTION_REASON_RECHARGE_CARD = 61
ACTION_REASON_RECHARGE_CARD_DAILY = 62
ACTION_REASON_RECHARGE_CARD_REPLACE = 63
ACTION_REASON_RECHARGE_CARD_REPLACE_FREE = 64
ACTION_REASON_RECHARGE_PLAY_REPLACE = 65
ACTION_REASON_MP_PLAY_TAKE_REWARD = 66
ACTION_REASON_ACTIVITY_WATCHER = 67
ACTION_REASON_SALESMAN_DELIVER_ITEM = 68
ACTION_REASON_SALESMAN_REWARD = 69
ACTION_REASON_REBATE = 70
ACTION_REASON_MCOIN_EXCHANGE_HCOIN = 71
ACTION_REASON_DAILY_TASK_EXCHANGE_LEGENDARY_KEY = 72
ACTION_REASON_UNLOCK_PERSON_LINE = 73
ACTION_REASON_FETTER_LEVEL_REWARD = 74
ACTION_REASON_BUY_RESIN = 75
ACTION_REASON_RECHARGE_PACKAGE = 76
ACTION_REASON_DELIVERY_DAILY_REWARD = 77
ACTION_REASON_CITY_REPUTATION_LEVEL = 78
ACTION_REASON_CITY_REPUTATION_QUEST = 79
ACTION_REASON_CITY_REPUTATION_REQUEST = 80
ACTION_REASON_CITY_REPUTATION_EXPLORE = 81
ACTION_REASON_OFFERGING_LEVEL = 82
ACTION_REASON_ROUTINE_HOST = 83
ACTION_REASON_ROUTINE_GUEST = 84
ACTION_REASON_TREASURE_MAP_SPOT_TOKEN = 89
ACTION_REASON_TREASURE_MAP_BONUS_LEVEL_REWARD = 90
ACTION_REASON_TREASURE_MAP_MP_REWARD = 91
ACTION_REASON_CONVERT = 92
ACTION_REASON_OVERFLOW_TRANSFORM = 93
ACTION_REASON_ACTIVITY_AVATAR_SELECTION_REWARD = 96
ACTION_REASON_ACTIVITY_WATCHER_BATCH = 97
ACTION_REASON_HIT_TREE_DROP = 98
ACTION_REASON_GET_HOME_LEVELUP_REWARD = 99
ACTION_REASON_HOME_DEFAULT_FURNITURE = 100
ACTION_REASON_ACTIVITY_COND = 101
ACTION_REASON_BATTLE_PASS_NOTIFY = 102
ACTION_REASON_RELIQUARY_DECOMPOSE = 103
ACTION_REASON_RECHARGE_GOOGLE_GIFT_GARD = 104
ACTION_REASON_RECHARGE_CONCERT_PRODUCT = 105
ACTION_REASON_RECHARGE_CONCERT_PRODUCT_REPLACE = 106
ACTION_REASON_SEND_CONCERT_PRODUCT_BY_MUIP = 107
ACTION_REASON_RECHARGE_APPLE_GIFT_GARD = 108
ACTION_REASON_PLAYER_USE_ITEM = 1001
ACTION_REASON_DROP_ITEM = 1002
ACTION_REASON_WEAPON_UPGRADE = 1011
ACTION_REASON_WEAPON_PROMOTE = 1012
ACTION_REASON_WEAPON_AWAKEN = 1013
ACTION_REASON_RELIC_UPGRADE = 1014
ACTION_REASON_ABILITY = 1015
ACTION_REASON_DUNGEON_STATUE_DROP = 1016
ACTION_REASON_OFFLINE_MSG = 1017
ACTION_REASON_AVATAR_UPGRADE = 1018
ACTION_REASON_AVATAR_PROMOTE = 1019
ACTION_REASON_QUEST_ACTION = 1021
ACTION_REASON_CITY_LEVELUP = 1022
ACTION_REASON_UPGRADE_SKILL = 1024
ACTION_REASON_UNLOCK_TALENT = 1025
ACTION_REASON_UPGRADE_PROUD_SKILL = 1026
ACTION_REASON_PLAYER_LEVEL_LIMIT_UP = 1027
ACTION_REASON_DUNGEON_DAILY = 1028
ACTION_REASON_ITEM_GIVING = 1030
ACTION_REASON_FORGE_COST = 1031
ACTION_REASON_INVESTIGATION_REWARD = 1032
ACTION_REASON_INVESTIGATION_TARGET_REWARD = 1033
ACTION_REASON_GADGET_INTERACT = 1034
ACTION_REASON_SEA_LAMP_CI_MATERIAL = 1036
ACTION_REASON_SEA_LAMP_CONTRIBUTION_REWARD = 1037
ACTION_REASON_SEA_LAMP_PHASE_REWARD = 1038
ACTION_REASON_SEA_LAMP_FLY_LAMP = 1039
ACTION_REASON_AUTO_RECOVER = 1040
ACTION_REASON_ACTIVITY_EXPIRE_ITEM = 1041
ACTION_REASON_SUB_COIN_NEGATIVE = 1042
ACTION_REASON_BARGAIN_DEDUCT = 1043
ACTION_REASON_BATTLE_PASS_PAID_REWARD = 1044
ACTION_REASON_BATTLE_PASS_LEVEL_REWARD = 1045
ACTION_REASON_TRIAL_AVATAR_ACTIVITY_FIRST_PASS_REWARD = 1046
ACTION_REASON_BUY_BATTLE_PASS_LEVEL = 1047
ACTION_REASON_GRANT_BIRTHDAY_BENEFIT = 1048
ACTION_REASON_ACHIEVEMENT_REWARD = 1049
ACTION_REASON_ACHIEVEMENT_GOAL_REWARD = 1050
ACTION_REASON_FIRST_SHARE_TO_SOCIAL_NETWORK = 1051
ACTION_REASON_DESTROY_MATERIAL = 1052
ACTION_REASON_CODEX_LEVELUP_REWARD = 1053
ACTION_REASON_HUNTING_OFFER_REWARD = 1054
ACTION_REASON_USE_WIDGET_ANCHOR_POINT = 1055
ACTION_REASON_USE_WIDGET_BONFIRE = 1056
ACTION_REASON_UNGRADE_WEAPON_RETURN_MATERIAL = 1057
ACTION_REASON_USE_WIDGET_ONEOFF_GATHER_POINT_DETECTOR = 1058
ACTION_REASON_USE_WIDGET_CLIENT_COLLECTOR = 1059
ACTION_REASON_USE_WIDGET_CLIENT_DETECTOR = 1060
ACTION_REASON_TAKE_GENERAL_REWARD = 1061
ACTION_REASON_ASTER_TAKE_SPECIAL_REWARD = 1062
ACTION_REASON_REMOVE_CODEX_BOOK = 1063
ACTION_REASON_OFFERING_ITEM = 1064
ACTION_REASON_USE_WIDGET_GADGET_BUILDER = 1065
ACTION_REASON_EFFIGY_FIRST_PASS_REWARD = 1066
ACTION_REASON_EFFIGY_REWARD = 1067
ACTION_REASON_REUNION_FIRST_GIFT_REWARD = 1068
ACTION_REASON_REUNION_SIGN_IN_REWARD = 1069
ACTION_REASON_REUNION_WATCHER_REWARD = 1070
ACTION_REASON_SALESMAN_MP_REWARD = 1071
ACTION_REASION_AVATAR_PROMOTE_REWARD = 1072
ACTION_REASON_BLESSING_REDEEM_REWARD = 1073
ACTION_MIRACLE_RING_REWARD = 1074
ACTION_REASON_EXPEDITION_REWARD = 1075
ACTION_REASON_TREASURE_MAP_REMOVE_DETECTOR = 1076
ACTION_REASON_MECHANICUS_DUNGEON_TICKET = 1077
ACTION_REASON_MECHANICUS_LEVELUP_GEAR = 1078
ACTION_REASON_MECHANICUS_BATTLE_SETTLE = 1079
ACTION_REASON_REGION_SEARCH_REWARD = 1080
ACTION_REASON_UNLOCK_COOP_CHAPTER = 1081
ACTION_REASON_TAKE_COOP_REWARD = 1082
ACTION_REASON_FLEUR_FAIR_DUNGEON_REWARD = 1083
ACTION_REASON_ACTIVITY_SCORE = 1084
ACTION_REASON_CHANNELLER_SLAB_ONEOFF_DUNGEON_REWARD = 1085
ACTION_REASON_FURNITURE_MAKE_START = 1086
ACTION_REASON_FURNITURE_MAKE_TAKE = 1087
ACTION_REASON_FURNITURE_MAKE_CANCEL = 1088
ACTION_REASON_FURNITURE_MAKE_FAST_FINISH = 1089
ACTION_REASON_CHANNELLER_SLAB_LOOP_DUNGEON_FIRST_PASS_REWARD = 1090
ACTION_REASON_CHANNELLER_SLAB_LOOP_DUNGEON_SCORE_REWARD = 1091
ACTION_REASON_HOME_LIMITED_SHOP_BUY = 1092
ACTION_REASON_HOME_COIN_COLLECT = 1093
ACTION_REASON_SUMMER_TIME_SENTRY_TOWER_REWARD = 1094
ACTION_REASON_SUMMER_TIME_SPRINT_BOAT_REWARD = 1095
ACTION_REASON_SUMMER_TIME_BOSS_REWARD = 1096
ACTION_REASON_SUMMER_TIME_BOMB_REWARD = 1097
ACTION_REASON_HOME_FETTER_COLLECT = 1098
ACTION_REASON_ECHO_SHELL_REWARD = 1099
ACTION_REASON_HOME_EVENT_REWARD = 1100
ACTION_REASON_BLITZ_RUSH_DUNGEON_REWARD = 1101
ACTION_REASON_FURNITURE_MAKE_RETURN = 1102
ACTION_REASON_HOME_PLANT_BOX_GATHER = 1103
ACTION_REASON_HOME_PLANT_SEED = 1104
ACTION_REASON_HOME_PLANT_GATHER = 1105
ACTION_REASON_CHESS_DUNGEON_REWARD = 1106
ACTION_REASON_GROUP_LINK_BUNDLE_FINISH = 1107
ACTION_REASON_LUNA_RITE_SACRIFICE = 1108
ACTION_REASON_LUNA_RITE_TAKE_SACRIFICE_REWARD = 1109
ACTION_REASON_FISH_BITE = 1110
ACTION_REASON_FISH_SUCC = 1111
ACTION_REASON_PLANT_FLOWER_REWARD = 1112
ACTION_REASON_PLANT_FLOWER_DELIVER_ITEM = 1113
ACTION_REASON_PLANT_FLOWER_GIVE_FLOWER = 1114
ACTION_REASON_PLANT_FLOWER_RECV_FLOWER = 1115
ACTION_REASON_ROGUE_CHALLENGE_SETTLE = 1116
ACTION_REASON_ROGUE_TAKE_FIRST_PASS_REWARD = 1117
ACTION_REASON_ROGUE_UPGRADE_SHIKIGAMI = 1118
ACTION_REASON_ROGUE_REFRESH_CARD = 1119


if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _ACTIONREASONTYPE._serialized_start=48
  _ACTIONREASONTYPE._serialized_end=8113
# @@protoc_insertion_point(module_scope)