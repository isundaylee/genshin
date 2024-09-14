from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ChangeHpDebtsReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHANGE_HP_DEBTS_NONE: _ClassVar[ChangeHpDebtsReason]
    CHANGE_HP_DEBTS_PAY: _ClassVar[ChangeHpDebtsReason]
    CHANGE_HP_DEBTS_PAY_FINISH: _ClassVar[ChangeHpDebtsReason]
    CHANGE_HP_DEBTS_CLEAR: _ClassVar[ChangeHpDebtsReason]
    CHANGE_HP_DEBTS_REDUCE_ABILITY: _ClassVar[ChangeHpDebtsReason]
    CHANGE_HP_DEBTS_ADD_ABILITY: _ClassVar[ChangeHpDebtsReason]
CHANGE_HP_DEBTS_NONE: ChangeHpDebtsReason
CHANGE_HP_DEBTS_PAY: ChangeHpDebtsReason
CHANGE_HP_DEBTS_PAY_FINISH: ChangeHpDebtsReason
CHANGE_HP_DEBTS_CLEAR: ChangeHpDebtsReason
CHANGE_HP_DEBTS_REDUCE_ABILITY: ChangeHpDebtsReason
CHANGE_HP_DEBTS_ADD_ABILITY: ChangeHpDebtsReason
