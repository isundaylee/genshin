# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: genshin/packet/proto/GetUgcRsp.proto
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
    'genshin/packet/proto/GetUgcRsp.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genshin.packet.proto import RecordUsage_pb2 as genshin_dot_packet_dot_proto_dot_RecordUsage__pb2
from genshin.packet.proto import UgcType_pb2 as genshin_dot_packet_dot_proto_dot_UgcType__pb2
from genshin.packet.proto import UgcMusicRecord_pb2 as genshin_dot_packet_dot_proto_dot_UgcMusicRecord__pb2
from genshin.packet.proto import UgcMusicBriefInfo_pb2 as genshin_dot_packet_dot_proto_dot_UgcMusicBriefInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$genshin/packet/proto/GetUgcRsp.proto\x1a&genshin/packet/proto/RecordUsage.proto\x1a\"genshin/packet/proto/UgcType.proto\x1a)genshin/packet/proto/UgcMusicRecord.proto\x1a,genshin/packet/proto/UgcMusicBriefInfo.proto\"\xf8\x01\n\tGetUgcRsp\x12&\n\x10ugc_record_usage\x18\r \x01(\x0e\x32\x0c.RecordUsage\x12\x10\n\x08ugc_guid\x18\x06 \x01(\x04\x12\x0f\n\x07retcode\x18\t \x01(\x05\x12\x1a\n\x08ugc_type\x18\x0e \x01(\x0e\x32\x08.UgcType\x12*\n\x0cmusic_record\x18\n \x01(\x0b\x32\x0f.UgcMusicRecordH\x00\x88\x01\x01\x12\x32\n\x10music_brief_info\x18\x97\x06 \x01(\x0b\x32\x12.UgcMusicBriefInfoH\x01\x88\x01\x01\x42\x0f\n\r_music_recordB\x13\n\x11_music_brief_infoB\x1b\n\x19\x65mu.grasscutter.net.protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'genshin.packet.proto.GetUgcRsp_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031emu.grasscutter.net.proto'
  _globals['_GETUGCRSP']._serialized_start=206
  _globals['_GETUGCRSP']._serialized_end=454
# @@protoc_insertion_point(module_scope)
