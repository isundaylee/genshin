from genshin.packet.proto import LLMLNHCIKCD_pb2 as _LLMLNHCIKCD_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CKNBAOMALOP(_message.Message):
    __slots__ = ("MLNOHNIGCDN", "IFBKFECFPJF", "CGDPDDAENIE", "KKEBKAMLMAM", "EJNINFFFKJP")
    MLNOHNIGCDN_FIELD_NUMBER: _ClassVar[int]
    IFBKFECFPJF_FIELD_NUMBER: _ClassVar[int]
    CGDPDDAENIE_FIELD_NUMBER: _ClassVar[int]
    KKEBKAMLMAM_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    MLNOHNIGCDN: _containers.RepeatedCompositeFieldContainer[_LLMLNHCIKCD_pb2.LLMLNHCIKCD]
    IFBKFECFPJF: bytes
    CGDPDDAENIE: bytes
    KKEBKAMLMAM: bool
    EJNINFFFKJP: int
    def __init__(self, MLNOHNIGCDN: _Optional[_Iterable[_Union[_LLMLNHCIKCD_pb2.LLMLNHCIKCD, _Mapping]]] = ..., IFBKFECFPJF: _Optional[bytes] = ..., CGDPDDAENIE: _Optional[bytes] = ..., KKEBKAMLMAM: bool = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
