from genshin.packet.proto import AvatarExpeditionInfo_pb2 as _AvatarExpeditionInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarExpeditionCallBackRsp(_message.Message):
    __slots__ = ("expedition_info_map", "retcode")
    class ExpeditionInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _AvatarExpeditionInfo_pb2.AvatarExpeditionInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_AvatarExpeditionInfo_pb2.AvatarExpeditionInfo, _Mapping]] = ...) -> None: ...
    EXPEDITION_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    expedition_info_map: _containers.MessageMap[int, _AvatarExpeditionInfo_pb2.AvatarExpeditionInfo]
    retcode: int
    def __init__(self, expedition_info_map: _Optional[_Mapping[int, _AvatarExpeditionInfo_pb2.AvatarExpeditionInfo]] = ..., retcode: _Optional[int] = ...) -> None: ...
