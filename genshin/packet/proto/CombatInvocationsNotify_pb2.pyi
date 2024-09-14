from genshin.packet.proto import CombatInvokeEntry_pb2 as _CombatInvokeEntry_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CombatInvocationsNotify(_message.Message):
    __slots__ = ("invoke_list",)
    INVOKE_LIST_FIELD_NUMBER: _ClassVar[int]
    invoke_list: _containers.RepeatedCompositeFieldContainer[_CombatInvokeEntry_pb2.CombatInvokeEntry]
    def __init__(self, invoke_list: _Optional[_Iterable[_Union[_CombatInvokeEntry_pb2.CombatInvokeEntry, _Mapping]]] = ...) -> None: ...
