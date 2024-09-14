from genshin.packet.proto import MassivePropParam_pb2 as _MassivePropParam_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MassivePropSyncInfo(_message.Message):
    __slots__ = ("id", "prop_list")
    ID_FIELD_NUMBER: _ClassVar[int]
    PROP_LIST_FIELD_NUMBER: _ClassVar[int]
    id: int
    prop_list: _containers.RepeatedCompositeFieldContainer[_MassivePropParam_pb2.MassivePropParam]
    def __init__(self, id: _Optional[int] = ..., prop_list: _Optional[_Iterable[_Union[_MassivePropParam_pb2.MassivePropParam, _Mapping]]] = ...) -> None: ...
