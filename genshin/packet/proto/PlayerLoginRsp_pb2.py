# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/PlayerLoginRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import BlockInfo_pb2 as genshin_dot_packet_dot_proto_dot_BlockInfo__pb2
from genshin.packet.proto import FeatureBlockInfo_pb2 as genshin_dot_packet_dot_proto_dot_FeatureBlockInfo__pb2
from genshin.packet.proto import ResVersionConfig_pb2 as genshin_dot_packet_dot_proto_dot_ResVersionConfig__pb2
from genshin.packet.proto import ShortAbilityHashPair_pb2 as genshin_dot_packet_dot_proto_dot_ShortAbilityHashPair__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)genshin/packet/proto/PlayerLoginRsp.proto\x1a$genshin/packet/proto/BlockInfo.proto\x1a+genshin/packet/proto/FeatureBlockInfo.proto\x1a+genshin/packet/proto/ResVersionConfig.proto\x1a/genshin/packet/proto/ShortAbilityHashPair.proto\"\x9e\t\n\x0ePlayerLoginRsp\x12=\n\x10\x61\x62ility_hash_map\x18\x0b \x03(\x0b\x32#.PlayerLoginRsp.AbilityHashMapEntry\x12\x11\n\x08is_audit\x18\x95\r \x01(\x08\x12\x15\n\ris_new_player\x18\x08 \x01(\x08\x12.\n\x12res_version_config\x18\xb1\x0f \x01(\x0b\x32\x11.ResVersionConfig\x12$\n\x1bis_enable_client_hash_debug\x18\xa4\x07 \x01(\x08\x12\x14\n\x0b\x63lient_md_5\x18\xa6\x0e \x01(\t\x12\x1b\n\x13\x63lient_data_version\x18\x01 \x01(\r\x12\x15\n\x0c\x63ountry_code\x18\xec\x0e \x01(\t\x12\x12\n\nis_relogin\x18\n \x01(\x08\x12\x13\n\x0bplayer_data\x18\r \x01(\x0c\x12\x10\n\x08game_biz\x18\x05 \x01(\t\x12:\n\x0e\x62lock_info_map\x18\xbb\x04 \x03(\x0b\x32!.PlayerLoginRsp.BlockInfoMapEntry\x12\x15\n\x0cregister_cps\x18\xf8\x0f \x01(\t\x12\x33\n\x17next_res_version_config\x18\xa5\x0c \x01(\x0b\x32\x11.ResVersionConfig\x12\x14\n\x0bis_transfer\x18\xe2\x0f \x01(\x08\x12\x1e\n\x15target_home_owner_uid\x18\xa9\x04 \x01(\r\x12\x36\n\x16short_ability_hash_map\x18\xfa\x01 \x03(\x0b\x32\x15.ShortAbilityHashPair\x12\x19\n\x11\x61\x62ility_hash_code\x18\x0c \x01(\x05\x12\x13\n\nis_sc_open\x18\x95\x0b \x01(\x08\x12#\n\x1b\x63lient_silence_data_version\x18\x06 \x01(\r\x12\x11\n\x08\x62irthday\x18\xf0\x04 \x01(\t\x12\x1b\n\x13is_use_ability_hash\x18\x02 \x01(\x08\x12&\n\x1d\x63lient_silence_version_suffix\x18\x93\n \x01(\t\x12\x1b\n\x13player_data_version\x18\x07 \x01(\r\x12\x1d\n\x14is_data_need_relogin\x18\xb7\x07 \x01(\x08\x12\x33\n\x17\x66\x65\x61ture_block_info_list\x18\xc8\n \x03(\x0b\x32\x11.FeatureBlockInfo\x12\x1c\n\x13\x63lient_silence_md_5\x18\xd2\r \x01(\t\x12\x12\n\ntarget_uid\x18\x0e \x01(\r\x12\x17\n\x0ftotal_tick_time\x18} \x01(\x01\x12\x12\n\nlogin_rand\x18\x04 \x01(\x04\x12\x10\n\x07sc_info\x18\xe8\x0f \x01(\x0c\x12\x1e\n\x15\x63lient_version_suffix\x18\x97\x08 \x01(\t\x12\x1a\n\x11next_resource_url\x18\xed\x04 \x01(\t\x12\x0f\n\x07retcode\x18\x0f \x01(\x05\x1a\x35\n\x13\x41\x62ilityHashMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a?\n\x11\x42lockInfoMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\x19\n\x05value\x18\x02 \x01(\x0b\x32\n.BlockInfo:\x02\x38\x01\x42\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_PLAYERLOGINRSP = DESCRIPTOR.message_types_by_name['PlayerLoginRsp']
_PLAYERLOGINRSP_ABILITYHASHMAPENTRY = _PLAYERLOGINRSP.nested_types_by_name['AbilityHashMapEntry']
_PLAYERLOGINRSP_BLOCKINFOMAPENTRY = _PLAYERLOGINRSP.nested_types_by_name['BlockInfoMapEntry']
PlayerLoginRsp = _reflection.GeneratedProtocolMessageType('PlayerLoginRsp', (_message.Message,), {

  'AbilityHashMapEntry' : _reflection.GeneratedProtocolMessageType('AbilityHashMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _PLAYERLOGINRSP_ABILITYHASHMAPENTRY,
    '__module__' : 'genshin.packet.proto.PlayerLoginRsp_pb2'
    # @@protoc_insertion_point(class_scope:PlayerLoginRsp.AbilityHashMapEntry)
    })
  ,

  'BlockInfoMapEntry' : _reflection.GeneratedProtocolMessageType('BlockInfoMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _PLAYERLOGINRSP_BLOCKINFOMAPENTRY,
    '__module__' : 'genshin.packet.proto.PlayerLoginRsp_pb2'
    # @@protoc_insertion_point(class_scope:PlayerLoginRsp.BlockInfoMapEntry)
    })
  ,
  'DESCRIPTOR' : _PLAYERLOGINRSP,
  '__module__' : 'genshin.packet.proto.PlayerLoginRsp_pb2'
  # @@protoc_insertion_point(class_scope:PlayerLoginRsp)
  })
_sym_db.RegisterMessage(PlayerLoginRsp)
_sym_db.RegisterMessage(PlayerLoginRsp.AbilityHashMapEntry)
_sym_db.RegisterMessage(PlayerLoginRsp.BlockInfoMapEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _PLAYERLOGINRSP_ABILITYHASHMAPENTRY._options = None
  _PLAYERLOGINRSP_ABILITYHASHMAPENTRY._serialized_options = b'8\001'
  _PLAYERLOGINRSP_BLOCKINFOMAPENTRY._options = None
  _PLAYERLOGINRSP_BLOCKINFOMAPENTRY._serialized_options = b'8\001'
  _PLAYERLOGINRSP._serialized_start=223
  _PLAYERLOGINRSP._serialized_end=1405
  _PLAYERLOGINRSP_ABILITYHASHMAPENTRY._serialized_start=1287
  _PLAYERLOGINRSP_ABILITYHASHMAPENTRY._serialized_end=1340
  _PLAYERLOGINRSP_BLOCKINFOMAPENTRY._serialized_start=1342
  _PLAYERLOGINRSP_BLOCKINFOMAPENTRY._serialized_end=1405
# @@protoc_insertion_point(module_scope)
