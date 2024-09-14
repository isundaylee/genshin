from genshin.packet.proto import ForgeQueueManipulateType_pb2 as _ForgeQueueManipulateType_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ForgeQueueManipulateReq(_message.Message):
    __slots__ = ("forge_queue_id", "manipulate_type")
    FORGE_QUEUE_ID_FIELD_NUMBER: _ClassVar[int]
    MANIPULATE_TYPE_FIELD_NUMBER: _ClassVar[int]
    forge_queue_id: int
    manipulate_type: _ForgeQueueManipulateType_pb2.ForgeQueueManipulateType
    def __init__(self, forge_queue_id: _Optional[int] = ..., manipulate_type: _Optional[_Union[_ForgeQueueManipulateType_pb2.ForgeQueueManipulateType, str]] = ...) -> None: ...
