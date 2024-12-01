from genshin.packet.proto import ABPKOLENHAP_pb2 as _ABPKOLENHAP_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GMIBNEEFEJJ(_message.Message):
    __slots__ = ("MPNJAOCKMAH", "HLKDDNGCKJN", "DHICFGHANOG", "EJNINFFFKJP")
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    HLKDDNGCKJN_FIELD_NUMBER: _ClassVar[int]
    DHICFGHANOG_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH: int
    HLKDDNGCKJN: int
    DHICFGHANOG: _ABPKOLENHAP_pb2.ABPKOLENHAP
    EJNINFFFKJP: int
    def __init__(self, MPNJAOCKMAH: _Optional[int] = ..., HLKDDNGCKJN: _Optional[int] = ..., DHICFGHANOG: _Optional[_Union[_ABPKOLENHAP_pb2.ABPKOLENHAP, str]] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
