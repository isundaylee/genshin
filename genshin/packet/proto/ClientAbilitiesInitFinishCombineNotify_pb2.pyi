from genshin.packet.proto import EntityAbilityInvokeEntry_pb2 as _EntityAbilityInvokeEntry_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClientAbilitiesInitFinishCombineNotify(_message.Message):
    __slots__ = ("entity_invoke_list",)
    ENTITY_INVOKE_LIST_FIELD_NUMBER: _ClassVar[int]
    entity_invoke_list: _containers.RepeatedCompositeFieldContainer[_EntityAbilityInvokeEntry_pb2.EntityAbilityInvokeEntry]
    def __init__(self, entity_invoke_list: _Optional[_Iterable[_Union[_EntityAbilityInvokeEntry_pb2.EntityAbilityInvokeEntry, _Mapping]]] = ...) -> None: ...
