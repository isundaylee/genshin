from genshin.packet.proto import ABPKOLENHAP_pb2 as _ABPKOLENHAP_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class APGHFLEELJL(_message.Message):
    __slots__ = ("CKGNIPBIAAI", "CABGDHLNBLK", "HLKDDNGCKJN", "MPNJAOCKMAH", "DHICFGHANOG", "EJNINFFFKJP")
    CKGNIPBIAAI_FIELD_NUMBER: _ClassVar[int]
    CABGDHLNBLK_FIELD_NUMBER: _ClassVar[int]
    HLKDDNGCKJN_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    DHICFGHANOG_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    CKGNIPBIAAI: _containers.RepeatedScalarFieldContainer[int]
    CABGDHLNBLK: _containers.RepeatedScalarFieldContainer[int]
    HLKDDNGCKJN: int
    MPNJAOCKMAH: int
    DHICFGHANOG: _ABPKOLENHAP_pb2.ABPKOLENHAP
    EJNINFFFKJP: int
    def __init__(self, CKGNIPBIAAI: _Optional[_Iterable[int]] = ..., CABGDHLNBLK: _Optional[_Iterable[int]] = ..., HLKDDNGCKJN: _Optional[int] = ..., MPNJAOCKMAH: _Optional[int] = ..., DHICFGHANOG: _Optional[_Union[_ABPKOLENHAP_pb2.ABPKOLENHAP, str]] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
