from genshin.packet.proto import AGFMPDBGLOP_pb2 as _AGFMPDBGLOP_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IAHNFAGHCKK(_message.Message):
    __slots__ = ("BBHIOHPMBML", "EJNINFFFKJP", "FCFOPOLHLOF", "FNKMGAGEDAH")
    BBHIOHPMBML_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    FCFOPOLHLOF_FIELD_NUMBER: _ClassVar[int]
    FNKMGAGEDAH_FIELD_NUMBER: _ClassVar[int]
    BBHIOHPMBML: _containers.RepeatedCompositeFieldContainer[_AGFMPDBGLOP_pb2.AGFMPDBGLOP]
    EJNINFFFKJP: int
    FCFOPOLHLOF: int
    FNKMGAGEDAH: int
    def __init__(self, BBHIOHPMBML: _Optional[_Iterable[_Union[_AGFMPDBGLOP_pb2.AGFMPDBGLOP, _Mapping]]] = ..., EJNINFFFKJP: _Optional[int] = ..., FCFOPOLHLOF: _Optional[int] = ..., FNKMGAGEDAH: _Optional[int] = ...) -> None: ...
