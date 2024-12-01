from genshin.packet.proto import MLECMFLLOGC_pb2 as _MLECMFLLOGC_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NFIGJIKIAPK(_message.Message):
    __slots__ = ("MDKPLBDANEF", "ALPFBHGHFHK", "KOGMMCNPJLL", "LLADMBNFOAM")
    MDKPLBDANEF_FIELD_NUMBER: _ClassVar[int]
    ALPFBHGHFHK_FIELD_NUMBER: _ClassVar[int]
    KOGMMCNPJLL_FIELD_NUMBER: _ClassVar[int]
    LLADMBNFOAM_FIELD_NUMBER: _ClassVar[int]
    MDKPLBDANEF: _containers.RepeatedCompositeFieldContainer[_MLECMFLLOGC_pb2.MLECMFLLOGC]
    ALPFBHGHFHK: _containers.RepeatedScalarFieldContainer[int]
    KOGMMCNPJLL: _containers.RepeatedScalarFieldContainer[int]
    LLADMBNFOAM: int
    def __init__(self, MDKPLBDANEF: _Optional[_Iterable[_Union[_MLECMFLLOGC_pb2.MLECMFLLOGC, _Mapping]]] = ..., ALPFBHGHFHK: _Optional[_Iterable[int]] = ..., KOGMMCNPJLL: _Optional[_Iterable[int]] = ..., LLADMBNFOAM: _Optional[int] = ...) -> None: ...
