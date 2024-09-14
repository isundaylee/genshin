from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ForgeQueueManipulateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FORGE_QUEUE_MANIPULATE_TYPE_RECEIVE_OUTPUT: _ClassVar[ForgeQueueManipulateType]
    FORGE_QUEUE_MANIPULATE_TYPE_STOP_FORGE: _ClassVar[ForgeQueueManipulateType]
FORGE_QUEUE_MANIPULATE_TYPE_RECEIVE_OUTPUT: ForgeQueueManipulateType
FORGE_QUEUE_MANIPULATE_TYPE_STOP_FORGE: ForgeQueueManipulateType
