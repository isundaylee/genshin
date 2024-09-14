from genshin.packet.proto import AbilityScalarValueEntry_pb2 as _AbilityScalarValueEntry_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AbilityMetaReInitOverrideMap(_message.Message):
    __slots__ = ("override_map",)
    OVERRIDE_MAP_FIELD_NUMBER: _ClassVar[int]
    override_map: _containers.RepeatedCompositeFieldContainer[_AbilityScalarValueEntry_pb2.AbilityScalarValueEntry]
    def __init__(self, override_map: _Optional[_Iterable[_Union[_AbilityScalarValueEntry_pb2.AbilityScalarValueEntry, _Mapping]]] = ...) -> None: ...
