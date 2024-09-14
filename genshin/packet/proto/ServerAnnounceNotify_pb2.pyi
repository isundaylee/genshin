from genshin.packet.proto import AnnounceData_pb2 as _AnnounceData_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ServerAnnounceNotify(_message.Message):
    __slots__ = ("announce_data_list",)
    ANNOUNCE_DATA_LIST_FIELD_NUMBER: _ClassVar[int]
    announce_data_list: _containers.RepeatedCompositeFieldContainer[_AnnounceData_pb2.AnnounceData]
    def __init__(self, announce_data_list: _Optional[_Iterable[_Union[_AnnounceData_pb2.AnnounceData, _Mapping]]] = ...) -> None: ...
