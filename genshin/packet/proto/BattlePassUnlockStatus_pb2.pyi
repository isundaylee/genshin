from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class BattlePassUnlockStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BATTLE_PASS_UNLOCK_STATUS_INVALID: _ClassVar[BattlePassUnlockStatus]
    BATTLE_PASS_UNLOCK_STATUS_FREE: _ClassVar[BattlePassUnlockStatus]
    BATTLE_PASS_UNLOCK_STATUS_PAID: _ClassVar[BattlePassUnlockStatus]
BATTLE_PASS_UNLOCK_STATUS_INVALID: BattlePassUnlockStatus
BATTLE_PASS_UNLOCK_STATUS_FREE: BattlePassUnlockStatus
BATTLE_PASS_UNLOCK_STATUS_PAID: BattlePassUnlockStatus
