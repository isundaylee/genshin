# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/ViewCodexRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import CodexTypeData_pb2 as genshin_dot_packet_dot_proto_dot_CodexTypeData__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'genshin/packet/proto/ViewCodexRsp.proto\x1a(genshin/packet/proto/CodexTypeData.proto\"\x9e\x01\n\x0cViewCodexRsp\x12\x0f\n\x07retcode\x18\x0c \x01(\x05\x12\x1b\n\x13Unk2800_IPOCJIPGNEJ\x18\n \x03(\r\x12\x1b\n\x13Unk2700_DFJJHFHHIHF\x18\x03 \x03(\r\x12&\n\x0etype_data_list\x18\t \x03(\x0b\x32\x0e.CodexTypeData\x12\x1b\n\x13Unk2800_OIPJCEPGJCF\x18\x0f \x03(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_VIEWCODEXRSP = DESCRIPTOR.message_types_by_name['ViewCodexRsp']
ViewCodexRsp = _reflection.GeneratedProtocolMessageType('ViewCodexRsp', (_message.Message,), {
  'DESCRIPTOR' : _VIEWCODEXRSP,
  '__module__' : 'genshin.packet.proto.ViewCodexRsp_pb2'
  # @@protoc_insertion_point(class_scope:ViewCodexRsp)
  })
_sym_db.RegisterMessage(ViewCodexRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _VIEWCODEXRSP._serialized_start=86
  _VIEWCODEXRSP._serialized_end=244
# @@protoc_insertion_point(module_scope)
