# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/FJKNAAMGEMM.proto
# Protobuf Python Version: 5.27.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    3,
    '',
    'genshin/packet/proto/FJKNAAMGEMM.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&genshin/packet/proto/FJKNAAMGEMM.proto*\xdc\"\n\x0b\x46JKNAAMGEMM\x12\x1c\n\x18\x46JKNAAMGEMM_ABILITY_NONE\x10\x00\x12,\n(FJKNAAMGEMM_ABILITY_META_MODIFIER_CHANGE\x10\x01\x12<\n8FJKNAAMGEMM_ABILITY_META_COMMAND_MODIFIER_CHANGE_REQUEST\x10\x02\x12\x33\n/FJKNAAMGEMM_ABILITY_META_SPECIAL_FLOAT_ARGUMENT\x10\x03\x12+\n\'FJKNAAMGEMM_ABILITY_META_OVERRIDE_PARAM\x10\x04\x12\x31\n-FJKNAAMGEMM_ABILITY_META_CLEAR_OVERRIDE_PARAM\x10\x05\x12/\n+FJKNAAMGEMM_ABILITY_META_REINIT_OVERRIDEMAP\x10\x06\x12/\n+FJKNAAMGEMM_ABILITY_META_GLOBAL_FLOAT_VALUE\x10\x07\x12\x35\n1FJKNAAMGEMM_ABILITY_META_CLEAR_GLOBAL_FLOAT_VALUE\x10\x08\x12\x35\n1FJKNAAMGEMM_ABILITY_META_ABILITY_ELEMENT_STRENGTH\x10\t\x12;\n7FJKNAAMGEMM_ABILITY_META_ADD_OR_GET_ABILITY_AND_TRIGGER\x10\n\x12.\n*FJKNAAMGEMM_ABILITY_META_SET_KILLED_SETATE\x10\x0b\x12\x30\n,FJKNAAMGEMM_ABILITY_META_SET_ABILITY_TRIGGER\x10\x0c\x12,\n(FJKNAAMGEMM_ABILITY_META_ADD_NEW_ABILITY\x10\r\x12+\n\'FJKNAAMGEMM_ABILITY_META_REMOVE_ABILITY\x10\x0e\x12\x36\n2FJKNAAMGEMM_ABILITY_META_SET_MODIFIER_APPLY_ENTITY\x10\x0f\x12\x37\n3FJKNAAMGEMM_ABILITY_META_MODIFIER_DURABILITY_CHANGE\x10\x10\x12\x34\n0FJKNAAMGEMM_ABILITY_META_ELEMENT_REACTION_VISUAL\x10\x11\x12/\n+FJKNAAMGEMM_ABILITY_META_SET_POSE_PARAMETER\x10\x12\x12\x38\n4FJKNAAMGEMM_ABILITY_META_UPDATE_BASE_REACTION_DAMAGE\x10\x13\x12\x35\n1FJKNAAMGEMM_ABILITY_META_TRIGGER_ELEMENT_REACTION\x10\x14\x12$\n FJKNAAMGEMM_ABILITY_META_LOSE_HP\x10\x15\x12/\n+FJKNAAMGEMM_ABILITY_META_DURABILITY_IS_ZERO\x10\x16\x12\x33\n/FJKNAAMGEMM_ABILITY_META_TRIGGER_ARKHE_REACTION\x10\x17\x12-\n)FJKNAAMGEMM_ABILITY_META_CHANGE_NYX_VALUE\x10\x18\x12.\n*FJKNAAMGEMM_ABILITY_ACTION_TRIGGER_ABILITY\x10\x32\x12/\n+FJKNAAMGEMM_ABILITY_ACTION_SET_CRASH_DAMAGE\x10\x33\x12%\n!FJKNAAMGEMM_ABILITY_ACTION_EFFECT\x10\x34\x12%\n!FJKNAAMGEMM_ABILITY_ACTION_SUMMON\x10\x35\x12$\n FJKNAAMGEMM_ABILITY_ACTION_BLINK\x10\x36\x12,\n(FJKNAAMGEMM_ABILITY_ACTION_CREATE_GADGET\x10\x37\x12\x33\n/FJKNAAMGEMM_ABILITY_ACTION_APPLY_LEVEL_MODIFIER\x10\x38\x12\x31\n-FJKNAAMGEMM_ABILITY_ACTION_GENERATE_ELEM_BALL\x10\x39\x12<\n8FJKNAAMGEMM_ABILITY_ACTION_SET_RANDOM_OVERRIDE_MAP_VALUE\x10:\x12\x31\n-FJKNAAMGEMM_ABILITY_ACTION_SERVER_MONSTER_LOG\x10;\x12*\n&FJKNAAMGEMM_ABILITY_ACTION_CREATE_TILE\x10<\x12+\n\'FJKNAAMGEMM_ABILITY_ACTION_DESTROY_TILE\x10=\x12/\n+FJKNAAMGEMM_ABILITY_ACTION_FIRE_AFTER_IMAGE\x10>\x12-\n)FJKNAAMGEMM_ABILITY_ACTION_DEDUCT_STAMINA\x10?\x12)\n%FJKNAAMGEMM_ABILITY_ACTION_HIT_EFFECT\x10@\x12\x36\n2FJKNAAMGEMM_ABILITY_ACTION_SET_BULLET_TRACK_TARGET\x10\x41\x12.\n*FJKNAAMGEMM_ABILITY_ACTION_FIREWORK_EFFECT\x10\x42\x12\x33\n/FJKNAAMGEMM_ABILITY_ACTION_LEVEL_BANK_ADD_STUFF\x10\x43\x12\x37\n3FJKNAAMGEMM_ABILITY_ACTION_GET_MATERIAL_PARAM_FLOAT\x10\x44\x12\x38\n4FJKNAAMGEMM_ABILITY_ACTION_GET_MATERIAL_PARAM_VECTOR\x10\x45\x12>\n:FJKNAAMGEMM_ABILITY_ACTION_SPECTACLE_BUILD_RECREATE_GADGET\x10\x46\x12\x34\n0FJKNAAMGEMM_ABILITY_MIXIN_AVATAR_STEER_BY_CAMERA\x10\x64\x12,\n(FJKNAAMGEMM_ABILITY_MIXIN_MONSTER_DEFEND\x10\x65\x12\'\n#FJKNAAMGEMM_ABILITY_MIXIN_WIND_ZONE\x10\x66\x12*\n&FJKNAAMGEMM_ABILITY_MIXIN_COST_STAMINA\x10g\x12*\n&FJKNAAMGEMM_ABILITY_MIXIN_ELITE_SHIELD\x10h\x12,\n(FJKNAAMGEMM_ABILITY_MIXIN_ELEMENT_SHIELD\x10i\x12+\n\'FJKNAAMGEMM_ABILITY_MIXIN_GLOBAL_SHIELD\x10j\x12(\n$FJKNAAMGEMM_ABILITY_MIXIN_SHIELD_BAR\x10k\x12/\n+FJKNAAMGEMM_ABILITY_MIXIN_WIND_SEED_SPAWNER\x10l\x12;\n7FJKNAAMGEMM_ABILITY_MIXIN_DO_ACTION_BY_ELEMENT_REACTION\x10m\x12\x37\n3FJKNAAMGEMM_ABILITY_MIXIN_FIELD_ENTITY_COUNT_CHANGE\x10n\x12-\n)FJKNAAMGEMM_ABILITY_MIXIN_SCENE_PROP_SYNC\x10o\x12/\n+FJKNAAMGEMM_ABILITY_MIXIN_WIDGET_MP_SUPPORT\x10p\x12Q\nMFJKNAAMGEMM_ABILITY_MIXIN_DO_ACTION_BY_SELF_MODIFIER_ELEMENT_DURABILITY_RATIO\x10q\x12\x30\n,FJKNAAMGEMM_ABILITY_MIXIN_FIREWORKS_LAUNCHER\x10r\x12\x38\n4FJKNAAMGEMM_ABILITY_MIXIN_ATTACK_RESULT_CREATE_COUNT\x10s\x12.\n*FJKNAAMGEMM_ABILITY_MIXIN_UGC_TIME_CONTROL\x10t\x12+\n\'FJKNAAMGEMM_ABILITY_MIXIN_AVATAR_COMBAT\x10u\x12<\n8FJKNAAMGEMM_ABILITY_MIXIN_DEATH_ZONE_REGIONAL_PLAY_MIXIN\x10v\x12)\n%FJKNAAMGEMM_ABILITY_MIXIN_UI_INTERACT\x10w\x12/\n+FJKNAAMGEMM_ABILITY_MIXIN_SHOOT_FROM_CAMERA\x10x\x12\x32\n.FJKNAAMGEMM_ABILITY_MIXIN_ERASE_BRICK_ACTIVITY\x10y\x12&\n\"FJKNAAMGEMM_ABILITY_MIXIN_BREAKOUT\x10z\x12)\n%FJKNAAMGEMM_ABILITY_MIXIN_DAMAGE_LOAN\x10{\x12*\n&FJKNAAMGEMM_ABILITY_MIXIN_BROADCAST_GV\x10|\x12(\n$FJKNAAMGEMM_ABILITY_MIXIN_RECEIVE_GV\x10}\x12\x33\n/FJKNAAMGEMM_ABILITY_MIXIN_RAYCAST_SELECT_TARGET\x10~\x12\x33\n/FJKNAAMGEMM_ABILITY_MIXIN_ENERGY_CRYSTAL_TARGET\x10\x7f\x12\x35\n0FJKNAAMGEMM_ABILITY_MIXIN_ROTATION_FOLLOW_CAMERA\x10\x80\x01\x12,\n\'FJKNAAMGEMM_ABILITY_MIXIN_BUOYANT_FORCE\x10\x81\x01\x12\x31\n,FJKNAAMGEMM_ABILITY_MIXIN_FILMFEST_BALL_GAME\x10\x82\x01\x12\x30\n+FJKNAAMGEMM_ABILITY_MIXIN_CHECK_SCAN_ENTITY\x10\x83\x01\x12\x30\n+FJKNAAMGEMM_ABILITY_MIXIN_TIME_TRACK_PLAYER\x10\x85\x01\x12*\n%FJKNAAMGEMM_ABILITY_MIXIN_PART_FOLLOW\x10\x86\x01\x12\x30\n+FJKNAAMGEMM_ABILITY_MIXIN_CHANGE_PHLOGISTON\x10\x87\x01\x12G\nBFJKNAAMGEMM_ABILITY_MIXIN_HUMAN_DRAGON_COLLAB_PICK_PHLOGISTON_BALL\x10\x88\x01\x12\x33\n.FJKNAAMGEMM_ABILITY_MIXIN_FREQUENCY_SHIELD_BAR\x10\x89\x01\x12\x31\n,FJKNAAMGEMM_ABILITY_MIXIN_SHAMAN_VIEW_TARGET\x10\x8a\x01\x12>\n9FJKNAAMGEMM_ABILITY_MIXIN_ATTACH_MODIFIER_TO_GLOBAL_VALUE\x10\x8b\x01\x12+\n&FJKNAAMGEMM_ABILITY_MIXIN_BRICK_MATRIX\x10\x8c\x01\x12\x36\n1FJKNAAMGEMM_ABILITY_MIXIN_VEHICLE_STEER_BY_CAMERA\x10\x8d\x01\x12\x32\n-FJKNAAMGEMM_ABILITY_MIXIN_AVATAR_SPECIAL_MOVE\x10\x8f\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.FJKNAAMGEMM_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_FJKNAAMGEMM']._serialized_start=43
  _globals['_FJKNAAMGEMM']._serialized_end=4487
# @@protoc_insertion_point(module_scope)
