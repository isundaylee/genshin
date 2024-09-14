from genshin.packet.proto import Achievement_pb2 as _Achievement_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AchievementUpdateNotify(_message.Message):
    __slots__ = ("achievement_list",)
    ACHIEVEMENT_LIST_FIELD_NUMBER: _ClassVar[int]
    achievement_list: _containers.RepeatedCompositeFieldContainer[_Achievement_pb2.Achievement]
    def __init__(self, achievement_list: _Optional[_Iterable[_Union[_Achievement_pb2.Achievement, _Mapping]]] = ...) -> None: ...
