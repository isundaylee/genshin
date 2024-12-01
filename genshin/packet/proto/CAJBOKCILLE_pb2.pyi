from genshin.packet.proto import AvatarRenameInfo_pb2 as _AvatarRenameInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CAJBOKCILLE(_message.Message):
    __slots__ = ("avatar_rename_list",)
    AVATAR_RENAME_LIST_FIELD_NUMBER: _ClassVar[int]
    avatar_rename_list: _containers.RepeatedCompositeFieldContainer[_AvatarRenameInfo_pb2.AvatarRenameInfo]
    def __init__(self, avatar_rename_list: _Optional[_Iterable[_Union[_AvatarRenameInfo_pb2.AvatarRenameInfo, _Mapping]]] = ...) -> None: ...
