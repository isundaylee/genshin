# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genshin/packet/proto/GadgetChainLevelChangeNotify.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7genshin/packet/proto/GadgetChainLevelChangeNotify.proto\"\xb2\x01\n\x1cGadgetChainLevelChangeNotify\x12V\n\x16gadget_chain_level_map\x18\x02 \x03(\x0b\x32\x36.GadgetChainLevelChangeNotify.GadgetChainLevelMapEntry\x1a:\n\x18GadgetChainLevelMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x42\x16\n\x14org.sorapointa.protob\x06proto3')



_GADGETCHAINLEVELCHANGENOTIFY = DESCRIPTOR.message_types_by_name['GadgetChainLevelChangeNotify']
_GADGETCHAINLEVELCHANGENOTIFY_GADGETCHAINLEVELMAPENTRY = _GADGETCHAINLEVELCHANGENOTIFY.nested_types_by_name['GadgetChainLevelMapEntry']
GadgetChainLevelChangeNotify = _reflection.GeneratedProtocolMessageType('GadgetChainLevelChangeNotify', (_message.Message,), {

  'GadgetChainLevelMapEntry' : _reflection.GeneratedProtocolMessageType('GadgetChainLevelMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _GADGETCHAINLEVELCHANGENOTIFY_GADGETCHAINLEVELMAPENTRY,
    '__module__' : 'genshin.packet.proto.GadgetChainLevelChangeNotify_pb2'
    # @@protoc_insertion_point(class_scope:GadgetChainLevelChangeNotify.GadgetChainLevelMapEntry)
    })
  ,
  'DESCRIPTOR' : _GADGETCHAINLEVELCHANGENOTIFY,
  '__module__' : 'genshin.packet.proto.GadgetChainLevelChangeNotify_pb2'
  # @@protoc_insertion_point(class_scope:GadgetChainLevelChangeNotify)
  })
_sym_db.RegisterMessage(GadgetChainLevelChangeNotify)
_sym_db.RegisterMessage(GadgetChainLevelChangeNotify.GadgetChainLevelMapEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.sorapointa.proto'
  _GADGETCHAINLEVELCHANGENOTIFY_GADGETCHAINLEVELMAPENTRY._options = None
  _GADGETCHAINLEVELCHANGENOTIFY_GADGETCHAINLEVELMAPENTRY._serialized_options = b'8\001'
  _GADGETCHAINLEVELCHANGENOTIFY._serialized_start=60
  _GADGETCHAINLEVELCHANGENOTIFY._serialized_end=238
  _GADGETCHAINLEVELCHANGENOTIFY_GADGETCHAINLEVELMAPENTRY._serialized_start=180
  _GADGETCHAINLEVELCHANGENOTIFY_GADGETCHAINLEVELMAPENTRY._serialized_end=238
# @@protoc_insertion_point(module_scope)