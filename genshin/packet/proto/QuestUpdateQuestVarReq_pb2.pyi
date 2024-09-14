from genshin.packet.proto import QuestVarOp_pb2 as _QuestVarOp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QuestUpdateQuestVarReq(_message.Message):
    __slots__ = ("quest_id", "parent_quest_var_seq", "parent_quest_id", "quest_var_op_list")
    QUEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_QUEST_VAR_SEQ_FIELD_NUMBER: _ClassVar[int]
    PARENT_QUEST_ID_FIELD_NUMBER: _ClassVar[int]
    QUEST_VAR_OP_LIST_FIELD_NUMBER: _ClassVar[int]
    quest_id: int
    parent_quest_var_seq: int
    parent_quest_id: int
    quest_var_op_list: _containers.RepeatedCompositeFieldContainer[_QuestVarOp_pb2.QuestVarOp]
    def __init__(self, quest_id: _Optional[int] = ..., parent_quest_var_seq: _Optional[int] = ..., parent_quest_id: _Optional[int] = ..., quest_var_op_list: _Optional[_Iterable[_Union[_QuestVarOp_pb2.QuestVarOp, _Mapping]]] = ...) -> None: ...
