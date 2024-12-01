from genshin.packet.proto import CACGLIBJIIE_pb2 as _CACGLIBJIIE_pb2
from genshin.packet.proto import KPFOBLALBLC_pb2 as _KPFOBLALBLC_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NFLCHLCAFED(_message.Message):
    __slots__ = ("LPAGGIOGCJK", "PKGGNCGLPPN", "DAAKPCOABEP")
    LPAGGIOGCJK_FIELD_NUMBER: _ClassVar[int]
    PKGGNCGLPPN_FIELD_NUMBER: _ClassVar[int]
    DAAKPCOABEP_FIELD_NUMBER: _ClassVar[int]
    LPAGGIOGCJK: _containers.RepeatedCompositeFieldContainer[_CACGLIBJIIE_pb2.CACGLIBJIIE]
    PKGGNCGLPPN: bool
    DAAKPCOABEP: _KPFOBLALBLC_pb2.KPFOBLALBLC
    def __init__(self, LPAGGIOGCJK: _Optional[_Iterable[_Union[_CACGLIBJIIE_pb2.CACGLIBJIIE, _Mapping]]] = ..., PKGGNCGLPPN: bool = ..., DAAKPCOABEP: _Optional[_Union[_KPFOBLALBLC_pb2.KPFOBLALBLC, str]] = ...) -> None: ...