from genshin.packet.proto import LCPDOPFDNDG_pb2 as _LCPDOPFDNDG_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PCBHODHCAIJ(_message.Message):
    __slots__ = ("LCONAHLDEJJ", "NIALFJMGPPH")
    LCONAHLDEJJ_FIELD_NUMBER: _ClassVar[int]
    NIALFJMGPPH_FIELD_NUMBER: _ClassVar[int]
    LCONAHLDEJJ: _containers.RepeatedCompositeFieldContainer[_LCPDOPFDNDG_pb2.LCPDOPFDNDG]
    NIALFJMGPPH: int
    def __init__(self, LCONAHLDEJJ: _Optional[_Iterable[_Union[_LCPDOPFDNDG_pb2.LCPDOPFDNDG, _Mapping]]] = ..., NIALFJMGPPH: _Optional[int] = ...) -> None: ...
