# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/GadgetInteractReq.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import InterOpType_pb2 as genshin_dot_packet_dot_proto_dot_InterOpType__pb2
from genshin.packet.proto import ResinCostType_pb2 as genshin_dot_packet_dot_proto_dot_ResinCostType__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,genshin/packet/proto/GadgetInteractReq.proto\x1a&genshin/packet/proto/InterOpType.proto\x1a(genshin/packet/proto/ResinCostType.proto\"\xc4\x01\n\x11GadgetInteractReq\x12\x11\n\tgadget_id\x18\x08 \x01(\r\x12\x1d\n\x15is_use_condense_resin\x18\x0f \x01(\x08\x12\x1d\n\x07op_type\x18\x05 \x01(\x0e\x32\x0c.InterOpType\x12\'\n\x0fresin_cost_type\x18\x01 \x01(\x0e\x32\x0e.ResinCostType\x12\x1b\n\x13Unk2700_DCPBGMKCHGJ\x18\x02 \x01(\r\x12\x18\n\x10gadget_entity_id\x18\x04 \x01(\rB\x16\n\x14org.sorapointa.protob\x06proto3')



_GADGETINTERACTREQ = DESCRIPTOR.message_types_by_name['GadgetInteractReq']
GadgetInteractReq = _reflection.GeneratedProtocolMessageType('GadgetInteractReq', (_message.Message,), {
  'DESCRIPTOR' : _GADGETINTERACTREQ,
  '__module__' : 'genshin.packet.proto.GadgetInteractReq_pb2'
  # @@protoc_insertion_point(class_scope:GadgetInteractReq)
  })
_sym_db.RegisterMessage(GadgetInteractReq)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _GADGETINTERACTREQ._serialized_start=131
  _GADGETINTERACTREQ._serialized_end=327
# @@protoc_insertion_point(module_scope)
