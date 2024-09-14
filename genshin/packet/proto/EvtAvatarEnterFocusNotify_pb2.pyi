from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from genshin.packet.proto import ForwardType_pb2 as _ForwardType_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EvtAvatarEnterFocusNotify(_message.Message):
    __slots__ = ("focus_forward", "forward_type", "entity_id", "bt1", "bt2", "bt3", "bt4", "bt5", "bt6", "bt7", "bt8", "bt9", "bt110")
    FOCUS_FORWARD_FIELD_NUMBER: _ClassVar[int]
    FORWARD_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    BT1_FIELD_NUMBER: _ClassVar[int]
    BT2_FIELD_NUMBER: _ClassVar[int]
    BT3_FIELD_NUMBER: _ClassVar[int]
    BT4_FIELD_NUMBER: _ClassVar[int]
    BT5_FIELD_NUMBER: _ClassVar[int]
    BT6_FIELD_NUMBER: _ClassVar[int]
    BT7_FIELD_NUMBER: _ClassVar[int]
    BT8_FIELD_NUMBER: _ClassVar[int]
    BT9_FIELD_NUMBER: _ClassVar[int]
    BT110_FIELD_NUMBER: _ClassVar[int]
    focus_forward: _Vector_pb2.Vector
    forward_type: _ForwardType_pb2.ForwardType
    entity_id: int
    bt1: bool
    bt2: bool
    bt3: bool
    bt4: bool
    bt5: bool
    bt6: bool
    bt7: bool
    bt8: bool
    bt9: bool
    bt110: bool
    def __init__(self, focus_forward: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., forward_type: _Optional[_Union[_ForwardType_pb2.ForwardType, str]] = ..., entity_id: _Optional[int] = ..., bt1: bool = ..., bt2: bool = ..., bt3: bool = ..., bt4: bool = ..., bt5: bool = ..., bt6: bool = ..., bt7: bool = ..., bt8: bool = ..., bt9: bool = ..., bt110: bool = ...) -> None: ...
