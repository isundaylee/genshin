from genshin.packet.proto import JICKPPDLOHC_pb2 as _JICKPPDLOHC_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JMBGNHCBNMO(_message.Message):
    __slots__ = ("item_list", "PJABEFAJBGB")
    ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    PJABEFAJBGB_FIELD_NUMBER: _ClassVar[int]
    item_list: _containers.RepeatedCompositeFieldContainer[_JICKPPDLOHC_pb2.JICKPPDLOHC]
    PJABEFAJBGB: int
    def __init__(self, item_list: _Optional[_Iterable[_Union[_JICKPPDLOHC_pb2.JICKPPDLOHC, _Mapping]]] = ..., PJABEFAJBGB: _Optional[int] = ...) -> None: ...
