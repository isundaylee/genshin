from genshin.packet.proto import UnionCmd_pb2 as _UnionCmd_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UnionCmdNotify(_message.Message):
    __slots__ = ("cmd_list",)
    CMD_LIST_FIELD_NUMBER: _ClassVar[int]
    cmd_list: _containers.RepeatedCompositeFieldContainer[_UnionCmd_pb2.UnionCmd]
    def __init__(self, cmd_list: _Optional[_Iterable[_Union[_UnionCmd_pb2.UnionCmd, _Mapping]]] = ...) -> None: ...
