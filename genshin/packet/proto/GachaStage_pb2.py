# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/GachaStage.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%genshin/packet/proto/GachaStage.proto\"\xac\x01\n\nGachaStage\x12\x10\n\x08stage_id\x18\x0f \x01(\r\x12@\n\x13Unk2700_DNMNEMKIELD\x18\x0e \x03(\x0b\x32#.GachaStage.Unk2700DNMNEMKIELDEntry\x12\x0f\n\x07is_open\x18\r \x01(\x08\x1a\x39\n\x17Unk2700DNMNEMKIELDEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_GACHASTAGE = DESCRIPTOR.message_types_by_name['GachaStage']
_GACHASTAGE_UNK2700DNMNEMKIELDENTRY = _GACHASTAGE.nested_types_by_name['Unk2700DNMNEMKIELDEntry']
GachaStage = _reflection.GeneratedProtocolMessageType('GachaStage', (_message.Message,), {

  'Unk2700DNMNEMKIELDEntry' : _reflection.GeneratedProtocolMessageType('Unk2700DNMNEMKIELDEntry', (_message.Message,), {
    'DESCRIPTOR' : _GACHASTAGE_UNK2700DNMNEMKIELDENTRY,
    '__module__' : 'genshin.packet.proto.GachaStage_pb2'
    # @@protoc_insertion_point(class_scope:GachaStage.Unk2700DNMNEMKIELDEntry)
    })
  ,
  'DESCRIPTOR' : _GACHASTAGE,
  '__module__' : 'genshin.packet.proto.GachaStage_pb2'
  # @@protoc_insertion_point(class_scope:GachaStage)
  })
_sym_db.RegisterMessage(GachaStage)
_sym_db.RegisterMessage(GachaStage.Unk2700DNMNEMKIELDEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _GACHASTAGE_UNK2700DNMNEMKIELDENTRY._options = None
  _GACHASTAGE_UNK2700DNMNEMKIELDENTRY._serialized_options = b'8\001'
  _GACHASTAGE._serialized_start=42
  _GACHASTAGE._serialized_end=214
  _GACHASTAGE_UNK2700DNMNEMKIELDENTRY._serialized_start=157
  _GACHASTAGE_UNK2700DNMNEMKIELDENTRY._serialized_end=214
# @@protoc_insertion_point(module_scope)
