from genshin.packet.proto import AbilityInvokeEntry_pb2 as _AbilityInvokeEntry_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClientAbilityChangeNotify(_message.Message):
    __slots__ = ("entity_id", "invokes", "is_init_hash")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    INVOKES_FIELD_NUMBER: _ClassVar[int]
    IS_INIT_HASH_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    invokes: _containers.RepeatedCompositeFieldContainer[_AbilityInvokeEntry_pb2.AbilityInvokeEntry]
    is_init_hash: bool
    def __init__(self, entity_id: _Optional[int] = ..., invokes: _Optional[_Iterable[_Union[_AbilityInvokeEntry_pb2.AbilityInvokeEntry, _Mapping]]] = ..., is_init_hash: bool = ...) -> None: ...
