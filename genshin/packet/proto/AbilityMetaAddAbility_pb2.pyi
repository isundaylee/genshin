from genshin.packet.proto import AbilityAppliedAbility_pb2 as _AbilityAppliedAbility_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AbilityMetaAddAbility(_message.Message):
    __slots__ = ("ability",)
    ABILITY_FIELD_NUMBER: _ClassVar[int]
    ability: _AbilityAppliedAbility_pb2.AbilityAppliedAbility
    def __init__(self, ability: _Optional[_Union[_AbilityAppliedAbility_pb2.AbilityAppliedAbility, _Mapping]] = ...) -> None: ...
