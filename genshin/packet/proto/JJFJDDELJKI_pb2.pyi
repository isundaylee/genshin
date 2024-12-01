from genshin.packet.proto import BNIJMEIKNIJ_pb2 as _BNIJMEIKNIJ_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JJFJDDELJKI(_message.Message):
    __slots__ = ("item_list",)
    ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    item_list: _containers.RepeatedCompositeFieldContainer[_BNIJMEIKNIJ_pb2.BNIJMEIKNIJ]
    def __init__(self, item_list: _Optional[_Iterable[_Union[_BNIJMEIKNIJ_pb2.BNIJMEIKNIJ, _Mapping]]] = ...) -> None: ...
