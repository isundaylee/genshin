from genshin.packet.proto import AbilityInvokeEntry_pb2 as _AbilityInvokeEntry_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AbilityInvocationsNotify(_message.Message):
    __slots__ = ("invokes",)
    INVOKES_FIELD_NUMBER: _ClassVar[int]
    invokes: _containers.RepeatedCompositeFieldContainer[_AbilityInvokeEntry_pb2.AbilityInvokeEntry]
    def __init__(self, invokes: _Optional[_Iterable[_Union[_AbilityInvokeEntry_pb2.AbilityInvokeEntry, _Mapping]]] = ...) -> None: ...
