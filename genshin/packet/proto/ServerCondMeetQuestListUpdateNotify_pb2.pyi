from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ServerCondMeetQuestListUpdateNotify(_message.Message):
    __slots__ = ("del_quest_id_list", "add_quest_id_list")
    DEL_QUEST_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    ADD_QUEST_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    del_quest_id_list: _containers.RepeatedScalarFieldContainer[int]
    add_quest_id_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, del_quest_id_list: _Optional[_Iterable[int]] = ..., add_quest_id_list: _Optional[_Iterable[int]] = ...) -> None: ...
