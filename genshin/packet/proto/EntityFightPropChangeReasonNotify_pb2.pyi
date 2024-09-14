from genshin.packet.proto import DetailInfo_pb2 as _DetailInfo_pb2
from genshin.packet.proto import PropChangeReason_pb2 as _PropChangeReason_pb2
from genshin.packet.proto import ChangeHpDebtsReason_pb2 as _ChangeHpDebtsReason_pb2
from genshin.packet.proto import ChangeHpReason_pb2 as _ChangeHpReason_pb2
from genshin.packet.proto import ChangeEnergyReason_pb2 as _ChangeEnergyReason_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EntityFightPropChangeReasonNotify(_message.Message):
    __slots__ = ("detail_info", "entity_id", "reason", "change_hp_debts_reason", "param_list", "prop_delta", "prop_type", "NNFONEOHGHE", "change_hp_reason", "change_energy_reason")
    DETAIL_INFO_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    CHANGE_HP_DEBTS_REASON_FIELD_NUMBER: _ClassVar[int]
    PARAM_LIST_FIELD_NUMBER: _ClassVar[int]
    PROP_DELTA_FIELD_NUMBER: _ClassVar[int]
    PROP_TYPE_FIELD_NUMBER: _ClassVar[int]
    NNFONEOHGHE_FIELD_NUMBER: _ClassVar[int]
    CHANGE_HP_REASON_FIELD_NUMBER: _ClassVar[int]
    CHANGE_ENERGY_REASON_FIELD_NUMBER: _ClassVar[int]
    detail_info: _DetailInfo_pb2.DetailInfo
    entity_id: int
    reason: _PropChangeReason_pb2.PropChangeReason
    change_hp_debts_reason: _ChangeHpDebtsReason_pb2.ChangeHpDebtsReason
    param_list: _containers.RepeatedScalarFieldContainer[int]
    prop_delta: float
    prop_type: int
    NNFONEOHGHE: float
    change_hp_reason: _ChangeHpReason_pb2.ChangeHpReason
    change_energy_reason: _ChangeEnergyReason_pb2.ChangeEnergyReason
    def __init__(self, detail_info: _Optional[_Union[_DetailInfo_pb2.DetailInfo, _Mapping]] = ..., entity_id: _Optional[int] = ..., reason: _Optional[_Union[_PropChangeReason_pb2.PropChangeReason, str]] = ..., change_hp_debts_reason: _Optional[_Union[_ChangeHpDebtsReason_pb2.ChangeHpDebtsReason, str]] = ..., param_list: _Optional[_Iterable[int]] = ..., prop_delta: _Optional[float] = ..., prop_type: _Optional[int] = ..., NNFONEOHGHE: _Optional[float] = ..., change_hp_reason: _Optional[_Union[_ChangeHpReason_pb2.ChangeHpReason, str]] = ..., change_energy_reason: _Optional[_Union[_ChangeEnergyReason_pb2.ChangeEnergyReason, str]] = ...) -> None: ...
