from genshin.packet.proto import ABPKOLENHAP_pb2 as _ABPKOLENHAP_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MCOBEJNLKPE(_message.Message):
    __slots__ = ("DHICFGHANOG", "HLKDDNGCKJN", "MPNJAOCKMAH")
    DHICFGHANOG_FIELD_NUMBER: _ClassVar[int]
    HLKDDNGCKJN_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    DHICFGHANOG: _ABPKOLENHAP_pb2.ABPKOLENHAP
    HLKDDNGCKJN: int
    MPNJAOCKMAH: int
    def __init__(self, DHICFGHANOG: _Optional[_Union[_ABPKOLENHAP_pb2.ABPKOLENHAP, str]] = ..., HLKDDNGCKJN: _Optional[int] = ..., MPNJAOCKMAH: _Optional[int] = ...) -> None: ...
