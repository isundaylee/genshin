# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/SeaLampContributeItemReq.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import ItemParam_pb2 as genshin_dot_packet_dot_proto_dot_ItemParam__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3genshin/packet/proto/SeaLampContributeItemReq.proto\x1a$genshin/packet/proto/ItemParam.proto\"N\n\x18SeaLampContributeItemReq\x12\x13\n\x0b\x61\x63tivity_id\x18\x08 \x01(\r\x12\x1d\n\titem_list\x18\x01 \x03(\x0b\x32\n.ItemParamB\x16\n\x14org.sorapointa.protob\x06proto3')



_SEALAMPCONTRIBUTEITEMREQ = DESCRIPTOR.message_types_by_name['SeaLampContributeItemReq']
SeaLampContributeItemReq = _reflection.GeneratedProtocolMessageType('SeaLampContributeItemReq', (_message.Message,), {
  'DESCRIPTOR' : _SEALAMPCONTRIBUTEITEMREQ,
  '__module__' : 'genshin.packet.proto.SeaLampContributeItemReq_pb2'
  # @@protoc_insertion_point(class_scope:SeaLampContributeItemReq)
  })
_sym_db.RegisterMessage(SeaLampContributeItemReq)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _SEALAMPCONTRIBUTEITEMREQ._serialized_start=93
  _SEALAMPCONTRIBUTEITEMREQ._serialized_end=171
# @@protoc_insertion_point(module_scope)
