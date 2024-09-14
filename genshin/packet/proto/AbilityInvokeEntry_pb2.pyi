from genshin.packet.proto import AbilityInvokeArgument_pb2 as _AbilityInvokeArgument_pb2
from genshin.packet.proto import ForwardType_pb2 as _ForwardType_pb2
from genshin.packet.proto import AbilityInvokeEntryHead_pb2 as _AbilityInvokeEntryHead_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AbilityInvokeEntry(_message.Message):
    __slots__ = ("event_id", "argument_type", "forward_peer", "forward_type", "head", "is_ignore_auth", "entity_id", "total_tick_time", "ability_data")
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    ARGUMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    FORWARD_PEER_FIELD_NUMBER: _ClassVar[int]
    FORWARD_TYPE_FIELD_NUMBER: _ClassVar[int]
    HEAD_FIELD_NUMBER: _ClassVar[int]
    IS_IGNORE_AUTH_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TICK_TIME_FIELD_NUMBER: _ClassVar[int]
    ABILITY_DATA_FIELD_NUMBER: _ClassVar[int]
    event_id: int
    argument_type: _AbilityInvokeArgument_pb2.AbilityInvokeArgument
    forward_peer: int
    forward_type: _ForwardType_pb2.ForwardType
    head: _AbilityInvokeEntryHead_pb2.AbilityInvokeEntryHead
    is_ignore_auth: bool
    entity_id: int
    total_tick_time: float
    ability_data: bytes
    def __init__(self, event_id: _Optional[int] = ..., argument_type: _Optional[_Union[_AbilityInvokeArgument_pb2.AbilityInvokeArgument, str]] = ..., forward_peer: _Optional[int] = ..., forward_type: _Optional[_Union[_ForwardType_pb2.ForwardType, str]] = ..., head: _Optional[_Union[_AbilityInvokeEntryHead_pb2.AbilityInvokeEntryHead, _Mapping]] = ..., is_ignore_auth: bool = ..., entity_id: _Optional[int] = ..., total_tick_time: _Optional[float] = ..., ability_data: _Optional[bytes] = ...) -> None: ...
