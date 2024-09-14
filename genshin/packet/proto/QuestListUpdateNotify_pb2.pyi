from genshin.packet.proto import Quest_pb2 as _Quest_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QuestListUpdateNotify(_message.Message):
    __slots__ = ("quest_list",)
    QUEST_LIST_FIELD_NUMBER: _ClassVar[int]
    quest_list: _containers.RepeatedCompositeFieldContainer[_Quest_pb2.Quest]
    def __init__(self, quest_list: _Optional[_Iterable[_Union[_Quest_pb2.Quest, _Mapping]]] = ...) -> None: ...
