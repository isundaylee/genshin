from genshin.packet.proto import ForwardType_pb2 as _ForwardType_pb2
from genshin.packet.proto import CombatTypeArgument_pb2 as _CombatTypeArgument_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CombatInvokeEntry(_message.Message):
    __slots__ = ("forward_type", "argument_type", "combat_data")
    FORWARD_TYPE_FIELD_NUMBER: _ClassVar[int]
    ARGUMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    COMBAT_DATA_FIELD_NUMBER: _ClassVar[int]
    forward_type: _ForwardType_pb2.ForwardType
    argument_type: _CombatTypeArgument_pb2.CombatTypeArgument
    combat_data: bytes
    def __init__(self, forward_type: _Optional[_Union[_ForwardType_pb2.ForwardType, str]] = ..., argument_type: _Optional[_Union[_CombatTypeArgument_pb2.CombatTypeArgument, str]] = ..., combat_data: _Optional[bytes] = ...) -> None: ...
