from genshin.packet.proto import InterOpType_pb2 as _InterOpType_pb2
from genshin.packet.proto import ResinCostType_pb2 as _ResinCostType_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GadgetInteractReq(_message.Message):
    __slots__ = ("ui_interact_id", "op_type", "is_use_condense_resin", "gadget_id", "resin_cost_type", "CHDDOFMLBLM", "gadget_entity_id")
    UI_INTERACT_ID_FIELD_NUMBER: _ClassVar[int]
    OP_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_USE_CONDENSE_RESIN_FIELD_NUMBER: _ClassVar[int]
    GADGET_ID_FIELD_NUMBER: _ClassVar[int]
    RESIN_COST_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHDDOFMLBLM_FIELD_NUMBER: _ClassVar[int]
    GADGET_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    ui_interact_id: int
    op_type: _InterOpType_pb2.InterOpType
    is_use_condense_resin: bool
    gadget_id: int
    resin_cost_type: _ResinCostType_pb2.ResinCostType
    CHDDOFMLBLM: int
    gadget_entity_id: int
    def __init__(self, ui_interact_id: _Optional[int] = ..., op_type: _Optional[_Union[_InterOpType_pb2.InterOpType, str]] = ..., is_use_condense_resin: bool = ..., gadget_id: _Optional[int] = ..., resin_cost_type: _Optional[_Union[_ResinCostType_pb2.ResinCostType, str]] = ..., CHDDOFMLBLM: _Optional[int] = ..., gadget_entity_id: _Optional[int] = ...) -> None: ...
