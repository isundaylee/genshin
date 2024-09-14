from genshin.packet.proto import AbilityControlBlock_pb2 as _AbilityControlBlock_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AbilityChangeNotify(_message.Message):
    __slots__ = ("ability_control_block", "entity_id")
    ABILITY_CONTROL_BLOCK_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    ability_control_block: _AbilityControlBlock_pb2.AbilityControlBlock
    entity_id: int
    def __init__(self, ability_control_block: _Optional[_Union[_AbilityControlBlock_pb2.AbilityControlBlock, _Mapping]] = ..., entity_id: _Optional[int] = ...) -> None: ...
