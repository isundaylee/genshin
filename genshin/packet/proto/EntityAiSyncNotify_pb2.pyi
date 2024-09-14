from genshin.packet.proto import AiSyncInfo_pb2 as _AiSyncInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EntityAiSyncNotify(_message.Message):
    __slots__ = ("info_list", "local_avatar_alerted_monster_list")
    INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    LOCAL_AVATAR_ALERTED_MONSTER_LIST_FIELD_NUMBER: _ClassVar[int]
    info_list: _containers.RepeatedCompositeFieldContainer[_AiSyncInfo_pb2.AiSyncInfo]
    local_avatar_alerted_monster_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, info_list: _Optional[_Iterable[_Union[_AiSyncInfo_pb2.AiSyncInfo, _Mapping]]] = ..., local_avatar_alerted_monster_list: _Optional[_Iterable[int]] = ...) -> None: ...
