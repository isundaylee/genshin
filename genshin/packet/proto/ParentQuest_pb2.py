# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/ParentQuest.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import ChildQuest_pb2 as genshin_dot_packet_dot_proto_dot_ChildQuest__pb2
from genshin.packet.proto import ParentQuestRandomInfo_pb2 as genshin_dot_packet_dot_proto_dot_ParentQuestRandomInfo__pb2
from genshin.packet.proto import Unk3000_ENLDIHLGNCK_pb2 as genshin_dot_packet_dot_proto_dot_Unk3000__ENLDIHLGNCK__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&genshin/packet/proto/ParentQuest.proto\x1a%genshin/packet/proto/ChildQuest.proto\x1a\x30genshin/packet/proto/ParentQuestRandomInfo.proto\x1a.genshin/packet/proto/Unk3000_ENLDIHLGNCK.proto\"\x9f\x03\n\x0bParentQuest\x12\x11\n\tquest_var\x18\x0e \x03(\x05\x12\x32\n\x0ctime_var_map\x18\x08 \x03(\x0b\x32\x1c.ParentQuest.TimeVarMapEntry\x12\x1a\n\x12parent_quest_state\x18\x01 \x01(\r\x12\x13\n\x0bis_finished\x18\x07 \x01(\x08\x12\x31\n\x13Unk3000_HLPGILIGGCB\x18\x0f \x03(\x0b\x32\x14.Unk3000_ENLDIHLGNCK\x12+\n\x0brandom_info\x18\x0c \x01(\x0b\x32\x16.ParentQuestRandomInfo\x12\x17\n\x0fparent_quest_id\x18\x03 \x01(\r\x12\x11\n\tis_random\x18\r \x01(\x08\x12\x1b\n\x13Unk2700_KHDDIJNOICK\x18\x06 \x01(\x04\x12\x15\n\rquest_var_seq\x18\x0b \x01(\r\x12%\n\x10\x63hild_quest_list\x18\t \x03(\x0b\x32\x0b.ChildQuest\x1a\x31\n\x0fTimeVarMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_PARENTQUEST = DESCRIPTOR.message_types_by_name['ParentQuest']
_PARENTQUEST_TIMEVARMAPENTRY = _PARENTQUEST.nested_types_by_name['TimeVarMapEntry']
ParentQuest = _reflection.GeneratedProtocolMessageType('ParentQuest', (_message.Message,), {

  'TimeVarMapEntry' : _reflection.GeneratedProtocolMessageType('TimeVarMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _PARENTQUEST_TIMEVARMAPENTRY,
    '__module__' : 'genshin.packet.proto.ParentQuest_pb2'
    # @@protoc_insertion_point(class_scope:ParentQuest.TimeVarMapEntry)
    })
  ,
  'DESCRIPTOR' : _PARENTQUEST,
  '__module__' : 'genshin.packet.proto.ParentQuest_pb2'
  # @@protoc_insertion_point(class_scope:ParentQuest)
  })
_sym_db.RegisterMessage(ParentQuest)
_sym_db.RegisterMessage(ParentQuest.TimeVarMapEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _PARENTQUEST_TIMEVARMAPENTRY._options = None
  _PARENTQUEST_TIMEVARMAPENTRY._serialized_options = b'8\001'
  _PARENTQUEST._serialized_start=180
  _PARENTQUEST._serialized_end=595
  _PARENTQUEST_TIMEVARMAPENTRY._serialized_start=546
  _PARENTQUEST_TIMEVARMAPENTRY._serialized_end=595
# @@protoc_insertion_point(module_scope)
