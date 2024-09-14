from genshin.packet.proto import ForwardType_pb2 as _ForwardType_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EvtDestroyGadgetNotify(_message.Message):
    __slots__ = ("entity_id", "forward_type")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    FORWARD_TYPE_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    forward_type: _ForwardType_pb2.ForwardType
    def __init__(self, entity_id: _Optional[int] = ..., forward_type: _Optional[_Union[_ForwardType_pb2.ForwardType, str]] = ...) -> None: ...
