from genshin.packet.proto import InterOpType_pb2 as _InterOpType_pb2
from genshin.packet.proto import InteractType_pb2 as _InteractType_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GadgetInteractRsp(_message.Message):
    __slots__ = ("op_type", "retcode", "gadget_entity_id", "interact_type", "gadget_id", "CHDDOFMLBLM")
    OP_TYPE_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    GADGET_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    INTERACT_TYPE_FIELD_NUMBER: _ClassVar[int]
    GADGET_ID_FIELD_NUMBER: _ClassVar[int]
    CHDDOFMLBLM_FIELD_NUMBER: _ClassVar[int]
    op_type: _InterOpType_pb2.InterOpType
    retcode: int
    gadget_entity_id: int
    interact_type: _InteractType_pb2.InteractType
    gadget_id: int
    CHDDOFMLBLM: int
    def __init__(self, op_type: _Optional[_Union[_InterOpType_pb2.InterOpType, str]] = ..., retcode: _Optional[int] = ..., gadget_entity_id: _Optional[int] = ..., interact_type: _Optional[_Union[_InteractType_pb2.InteractType, str]] = ..., gadget_id: _Optional[int] = ..., CHDDOFMLBLM: _Optional[int] = ...) -> None: ...
