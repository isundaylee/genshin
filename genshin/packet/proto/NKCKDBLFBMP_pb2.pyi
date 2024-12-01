from genshin.packet.proto import HCJGIFNJPPJ_pb2 as _HCJGIFNJPPJ_pb2
from genshin.packet.proto import DCHONJFDDDO_pb2 as _DCHONJFDDDO_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NKCKDBLFBMP(_message.Message):
    __slots__ = ("IBEAKHHNOHB", "CDBFPFOJBIJ", "CJOKFLDEFMB")
    IBEAKHHNOHB_FIELD_NUMBER: _ClassVar[int]
    CDBFPFOJBIJ_FIELD_NUMBER: _ClassVar[int]
    CJOKFLDEFMB_FIELD_NUMBER: _ClassVar[int]
    IBEAKHHNOHB: _HCJGIFNJPPJ_pb2.HCJGIFNJPPJ
    CDBFPFOJBIJ: _DCHONJFDDDO_pb2.DCHONJFDDDO
    CJOKFLDEFMB: int
    def __init__(self, IBEAKHHNOHB: _Optional[_Union[_HCJGIFNJPPJ_pb2.HCJGIFNJPPJ, _Mapping]] = ..., CDBFPFOJBIJ: _Optional[_Union[_DCHONJFDDDO_pb2.DCHONJFDDDO, str]] = ..., CJOKFLDEFMB: _Optional[int] = ...) -> None: ...
