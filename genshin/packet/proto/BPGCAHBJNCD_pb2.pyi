from genshin.packet.proto import JDNCHHPCNMD_pb2 as _JDNCHHPCNMD_pb2
from genshin.packet.proto import BOMACPDEPID_pb2 as _BOMACPDEPID_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BPGCAHBJNCD(_message.Message):
    __slots__ = ("KPNDJLKLKFO", "HKPIDJMMCKB")
    KPNDJLKLKFO_FIELD_NUMBER: _ClassVar[int]
    HKPIDJMMCKB_FIELD_NUMBER: _ClassVar[int]
    KPNDJLKLKFO: _JDNCHHPCNMD_pb2.JDNCHHPCNMD
    HKPIDJMMCKB: _BOMACPDEPID_pb2.BOMACPDEPID
    def __init__(self, KPNDJLKLKFO: _Optional[_Union[_JDNCHHPCNMD_pb2.JDNCHHPCNMD, _Mapping]] = ..., HKPIDJMMCKB: _Optional[_Union[_BOMACPDEPID_pb2.BOMACPDEPID, _Mapping]] = ...) -> None: ...
