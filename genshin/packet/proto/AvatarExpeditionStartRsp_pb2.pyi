from genshin.packet.proto import AvatarExpeditionInfo_pb2 as _AvatarExpeditionInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarExpeditionStartRsp(_message.Message):
    __slots__ = ("retcode", "expedition_info_map")
    class ExpeditionInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _AvatarExpeditionInfo_pb2.AvatarExpeditionInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_AvatarExpeditionInfo_pb2.AvatarExpeditionInfo, _Mapping]] = ...) -> None: ...
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    EXPEDITION_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    expedition_info_map: _containers.MessageMap[int, _AvatarExpeditionInfo_pb2.AvatarExpeditionInfo]
    def __init__(self, retcode: _Optional[int] = ..., expedition_info_map: _Optional[_Mapping[int, _AvatarExpeditionInfo_pb2.AvatarExpeditionInfo]] = ...) -> None: ...
