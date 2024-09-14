from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateAbilityCreatedMovingPlatformNotify(_message.Message):
    __slots__ = ("entity_id", "op_type")
    class OpType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OP_TYPE_NONE: _ClassVar[UpdateAbilityCreatedMovingPlatformNotify.OpType]
        OP_TYPE_ACTIVATE: _ClassVar[UpdateAbilityCreatedMovingPlatformNotify.OpType]
        OP_TYPE_DEACTIVATE: _ClassVar[UpdateAbilityCreatedMovingPlatformNotify.OpType]
    OP_TYPE_NONE: UpdateAbilityCreatedMovingPlatformNotify.OpType
    OP_TYPE_ACTIVATE: UpdateAbilityCreatedMovingPlatformNotify.OpType
    OP_TYPE_DEACTIVATE: UpdateAbilityCreatedMovingPlatformNotify.OpType
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    OP_TYPE_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    op_type: UpdateAbilityCreatedMovingPlatformNotify.OpType
    def __init__(self, entity_id: _Optional[int] = ..., op_type: _Optional[_Union[UpdateAbilityCreatedMovingPlatformNotify.OpType, str]] = ...) -> None: ...
