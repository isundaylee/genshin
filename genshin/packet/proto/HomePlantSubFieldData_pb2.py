# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/HomePlantSubFieldData.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import HomePlantFieldStatus_pb2 as genshin_dot_packet_dot_proto_dot_HomePlantFieldStatus__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0genshin/packet/proto/HomePlantSubFieldData.proto\x1a/genshin/packet/proto/HomePlantFieldStatus.proto\"\x97\x01\n\x15HomePlantSubFieldData\x12\x16\n\x0e\x65ntity_id_list\x18\x0f \x03(\r\x12+\n\x0c\x66ield_status\x18\x0e \x01(\x0e\x32\x15.HomePlantFieldStatus\x12\x16\n\x0ehome_gather_id\x18\t \x01(\r\x12\x0f\n\x07seed_id\x18\x08 \x01(\r\x12\x10\n\x08\x65nd_time\x18\x04 \x01(\x07\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_HOMEPLANTSUBFIELDDATA = DESCRIPTOR.message_types_by_name['HomePlantSubFieldData']
HomePlantSubFieldData = _reflection.GeneratedProtocolMessageType('HomePlantSubFieldData', (_message.Message,), {
  'DESCRIPTOR' : _HOMEPLANTSUBFIELDDATA,
  '__module__' : 'genshin.packet.proto.HomePlantSubFieldData_pb2'
  # @@protoc_insertion_point(class_scope:HomePlantSubFieldData)
  })
_sym_db.RegisterMessage(HomePlantSubFieldData)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _HOMEPLANTSUBFIELDDATA._serialized_start=102
  _HOMEPLANTSUBFIELDDATA._serialized_end=253
# @@protoc_insertion_point(module_scope)
