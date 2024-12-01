from genshin.packet.proto import FGNHPFIDPCB_pb2 as _FGNHPFIDPCB_pb2
from genshin.packet.proto import BHNJIKABAOK_pb2 as _BHNJIKABAOK_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IJFNLMOGGLK(_message.Message):
    __slots__ = ("JMLCDHBKBNG", "IBCGFJEDMFB", "CHHGPNNNNLP", "MBLHCGPHFLE")
    JMLCDHBKBNG_FIELD_NUMBER: _ClassVar[int]
    IBCGFJEDMFB_FIELD_NUMBER: _ClassVar[int]
    CHHGPNNNNLP_FIELD_NUMBER: _ClassVar[int]
    MBLHCGPHFLE_FIELD_NUMBER: _ClassVar[int]
    JMLCDHBKBNG: _FGNHPFIDPCB_pb2.FGNHPFIDPCB
    IBCGFJEDMFB: _containers.RepeatedCompositeFieldContainer[_BHNJIKABAOK_pb2.BHNJIKABAOK]
    CHHGPNNNNLP: _FGNHPFIDPCB_pb2.FGNHPFIDPCB
    MBLHCGPHFLE: int
    def __init__(self, JMLCDHBKBNG: _Optional[_Union[_FGNHPFIDPCB_pb2.FGNHPFIDPCB, _Mapping]] = ..., IBCGFJEDMFB: _Optional[_Iterable[_Union[_BHNJIKABAOK_pb2.BHNJIKABAOK, _Mapping]]] = ..., CHHGPNNNNLP: _Optional[_Union[_FGNHPFIDPCB_pb2.FGNHPFIDPCB, _Mapping]] = ..., MBLHCGPHFLE: _Optional[int] = ...) -> None: ...
