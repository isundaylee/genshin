# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/GachaActivityDetailInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import GachaStage_pb2 as genshin_dot_packet_dot_proto_dot_GachaStage__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2genshin/packet/proto/GachaActivityDetailInfo.proto\x1a%genshin/packet/proto/GachaStage.proto\"\xab\x03\n\x17GachaActivityDetailInfo\x12\x1b\n\x13Unk2700_PIDHKNLDALB\x18\x06 \x03(\r\x12%\n\x10gacha_stage_list\x18\x04 \x03(\x0b\x32\x0b.GachaStage\x12M\n\x13Unk2700_KOHKBCABICD\x18\x08 \x03(\x0b\x32\x30.GachaActivityDetailInfo.Unk2700KOHKBCABICDEntry\x12\x1b\n\x13Unk2700_CDPAPBIOPCA\x18\x03 \x01(\r\x12M\n\x13Unk2700_DACHHINLDDJ\x18\x05 \x03(\x0b\x32\x30.GachaActivityDetailInfo.Unk2700DACHHINLDDJEntry\x12\x1b\n\x13Unk2700_FGFGLDIJJEK\x18\x0c \x01(\r\x1a\x39\n\x17Unk2700KOHKBCABICDEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a\x39\n\x17Unk2700DACHHINLDDJEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_GACHAACTIVITYDETAILINFO = DESCRIPTOR.message_types_by_name['GachaActivityDetailInfo']
_GACHAACTIVITYDETAILINFO_UNK2700KOHKBCABICDENTRY = _GACHAACTIVITYDETAILINFO.nested_types_by_name['Unk2700KOHKBCABICDEntry']
_GACHAACTIVITYDETAILINFO_UNK2700DACHHINLDDJENTRY = _GACHAACTIVITYDETAILINFO.nested_types_by_name['Unk2700DACHHINLDDJEntry']
GachaActivityDetailInfo = _reflection.GeneratedProtocolMessageType('GachaActivityDetailInfo', (_message.Message,), {

  'Unk2700KOHKBCABICDEntry' : _reflection.GeneratedProtocolMessageType('Unk2700KOHKBCABICDEntry', (_message.Message,), {
    'DESCRIPTOR' : _GACHAACTIVITYDETAILINFO_UNK2700KOHKBCABICDENTRY,
    '__module__' : 'genshin.packet.proto.GachaActivityDetailInfo_pb2'
    # @@protoc_insertion_point(class_scope:GachaActivityDetailInfo.Unk2700KOHKBCABICDEntry)
    })
  ,

  'Unk2700DACHHINLDDJEntry' : _reflection.GeneratedProtocolMessageType('Unk2700DACHHINLDDJEntry', (_message.Message,), {
    'DESCRIPTOR' : _GACHAACTIVITYDETAILINFO_UNK2700DACHHINLDDJENTRY,
    '__module__' : 'genshin.packet.proto.GachaActivityDetailInfo_pb2'
    # @@protoc_insertion_point(class_scope:GachaActivityDetailInfo.Unk2700DACHHINLDDJEntry)
    })
  ,
  'DESCRIPTOR' : _GACHAACTIVITYDETAILINFO,
  '__module__' : 'genshin.packet.proto.GachaActivityDetailInfo_pb2'
  # @@protoc_insertion_point(class_scope:GachaActivityDetailInfo)
  })
_sym_db.RegisterMessage(GachaActivityDetailInfo)
_sym_db.RegisterMessage(GachaActivityDetailInfo.Unk2700KOHKBCABICDEntry)
_sym_db.RegisterMessage(GachaActivityDetailInfo.Unk2700DACHHINLDDJEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _GACHAACTIVITYDETAILINFO_UNK2700KOHKBCABICDENTRY._options = None
  _GACHAACTIVITYDETAILINFO_UNK2700KOHKBCABICDENTRY._serialized_options = b'8\001'
  _GACHAACTIVITYDETAILINFO_UNK2700DACHHINLDDJENTRY._options = None
  _GACHAACTIVITYDETAILINFO_UNK2700DACHHINLDDJENTRY._serialized_options = b'8\001'
  _GACHAACTIVITYDETAILINFO._serialized_start=94
  _GACHAACTIVITYDETAILINFO._serialized_end=521
  _GACHAACTIVITYDETAILINFO_UNK2700KOHKBCABICDENTRY._serialized_start=405
  _GACHAACTIVITYDETAILINFO_UNK2700KOHKBCABICDENTRY._serialized_end=462
  _GACHAACTIVITYDETAILINFO_UNK2700DACHHINLDDJENTRY._serialized_start=464
  _GACHAACTIVITYDETAILINFO_UNK2700DACHHINLDDJENTRY._serialized_end=521
# @@protoc_insertion_point(module_scope)
