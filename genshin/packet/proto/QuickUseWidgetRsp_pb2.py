# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/QuickUseWidgetRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import ClientCollectorData_pb2 as genshin_dot_packet_dot_proto_dot_ClientCollectorData__pb2
from genshin.packet.proto import OneofGatherPointDetectorData_pb2 as genshin_dot_packet_dot_proto_dot_OneofGatherPointDetectorData__pb2
from genshin.packet.proto import SkyCrystalDetectorQuickUseResult_pb2 as genshin_dot_packet_dot_proto_dot_SkyCrystalDetectorQuickUseResult__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,genshin/packet/proto/QuickUseWidgetRsp.proto\x1a.genshin/packet/proto/ClientCollectorData.proto\x1a\x37genshin/packet/proto/OneofGatherPointDetectorData.proto\x1a;genshin/packet/proto/SkyCrystalDetectorQuickUseResult.proto\"\x87\x02\n\x11QuickUseWidgetRsp\x12\x13\n\x0bmaterial_id\x18\x06 \x01(\r\x12\x0f\n\x07retcode\x18\x05 \x01(\x05\x12\x36\n\rdetector_data\x18\x03 \x01(\x0b\x32\x1d.OneofGatherPointDetectorDataH\x00\x12\x35\n\x15\x63lient_collector_data\x18\x0f \x01(\x0b\x32\x14.ClientCollectorDataH\x00\x12T\n%sky_crystal_detector_quick_use_result\x18\xda\xa7\n \x01(\x0b\x32!.SkyCrystalDetectorQuickUseResultH\x00\x42\x07\n\x05paramB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')



_QUICKUSEWIDGETRSP = DESCRIPTOR.message_types_by_name['QuickUseWidgetRsp']
QuickUseWidgetRsp = _reflection.GeneratedProtocolMessageType('QuickUseWidgetRsp', (_message.Message,), {
  'DESCRIPTOR' : _QUICKUSEWIDGETRSP,
  '__module__' : 'genshin.packet.proto.QuickUseWidgetRsp_pb2'
  # @@protoc_insertion_point(class_scope:QuickUseWidgetRsp)
  })
_sym_db.RegisterMessage(QuickUseWidgetRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _QUICKUSEWIDGETRSP._serialized_start=215
  _QUICKUSEWIDGETRSP._serialized_end=478
# @@protoc_insertion_point(module_scope)
