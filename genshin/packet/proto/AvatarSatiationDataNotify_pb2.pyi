from genshin.packet.proto import AvatarSatiationData_pb2 as _AvatarSatiationData_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarSatiationDataNotify(_message.Message):
    __slots__ = ("satiation_data_list",)
    SATIATION_DATA_LIST_FIELD_NUMBER: _ClassVar[int]
    satiation_data_list: _containers.RepeatedCompositeFieldContainer[_AvatarSatiationData_pb2.AvatarSatiationData]
    def __init__(self, satiation_data_list: _Optional[_Iterable[_Union[_AvatarSatiationData_pb2.AvatarSatiationData, _Mapping]]] = ...) -> None: ...
