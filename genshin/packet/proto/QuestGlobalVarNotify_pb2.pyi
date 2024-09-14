from genshin.packet.proto import QuestGlobalVar_pb2 as _QuestGlobalVar_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QuestGlobalVarNotify(_message.Message):
    __slots__ = ("var_list",)
    VAR_LIST_FIELD_NUMBER: _ClassVar[int]
    var_list: _containers.RepeatedCompositeFieldContainer[_QuestGlobalVar_pb2.QuestGlobalVar]
    def __init__(self, var_list: _Optional[_Iterable[_Union[_QuestGlobalVar_pb2.QuestGlobalVar, _Mapping]]] = ...) -> None: ...
