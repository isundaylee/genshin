from genshin.packet.proto import ParentQuest_pb2 as _ParentQuest_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FinishedParentQuestNotify(_message.Message):
    __slots__ = ("parent_quest_list",)
    PARENT_QUEST_LIST_FIELD_NUMBER: _ClassVar[int]
    parent_quest_list: _containers.RepeatedCompositeFieldContainer[_ParentQuest_pb2.ParentQuest]
    def __init__(self, parent_quest_list: _Optional[_Iterable[_Union[_ParentQuest_pb2.ParentQuest, _Mapping]]] = ...) -> None: ...
