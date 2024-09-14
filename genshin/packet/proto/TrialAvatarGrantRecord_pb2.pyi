from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TrialAvatarGrantRecord(_message.Message):
    __slots__ = ("grant_reason", "from_parent_quest_id")
    class GrantReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        GRANT_REASON_INVALID: _ClassVar[TrialAvatarGrantRecord.GrantReason]
        GRANT_REASON_BY_QUEST: _ClassVar[TrialAvatarGrantRecord.GrantReason]
        GRANT_REASON_BY_TRIAL_AVATAR_ACTIVITY: _ClassVar[TrialAvatarGrantRecord.GrantReason]
        GRANT_REASON_BY_DUNGEON_ELEMENT_CHALLENGE: _ClassVar[TrialAvatarGrantRecord.GrantReason]
        GRANT_REASON_BY_MIST_TRIAL_ACTIVITY: _ClassVar[TrialAvatarGrantRecord.GrantReason]
        GRANT_REASON_BY_SUMO_ACTIVITY: _ClassVar[TrialAvatarGrantRecord.GrantReason]
        GRANT_REASON_BY_POTION_ACTIVITY: _ClassVar[TrialAvatarGrantRecord.GrantReason]
        GRANT_REASON_BY_CRYSTAL_LINK_ACTIVITY: _ClassVar[TrialAvatarGrantRecord.GrantReason]
        GRANT_REASON_BY_IRODORI_MASTER: _ClassVar[TrialAvatarGrantRecord.GrantReason]
        GRANT_REASON_BY_GM: _ClassVar[TrialAvatarGrantRecord.GrantReason]
        GRANT_REASON_BY_INSTABLE_SPRAY_ACTIVITY: _ClassVar[TrialAvatarGrantRecord.GrantReason]
        GRANT_REASON_BY_MUQADAS_POTION_ACTIVITY: _ClassVar[TrialAvatarGrantRecord.GrantReason]
        GRANT_REASON_BY_VINTAGE_HUNTING: _ClassVar[TrialAvatarGrantRecord.GrantReason]
        GRANT_REASON_BY_CHAR_AMUSEMENT: _ClassVar[TrialAvatarGrantRecord.GrantReason]
        FJBKKFJNBHD_HMLDNDBKNFL: _ClassVar[TrialAvatarGrantRecord.GrantReason]
        FJBKKFJNBHD_PJDEJIHFCPP: _ClassVar[TrialAvatarGrantRecord.GrantReason]
    GRANT_REASON_INVALID: TrialAvatarGrantRecord.GrantReason
    GRANT_REASON_BY_QUEST: TrialAvatarGrantRecord.GrantReason
    GRANT_REASON_BY_TRIAL_AVATAR_ACTIVITY: TrialAvatarGrantRecord.GrantReason
    GRANT_REASON_BY_DUNGEON_ELEMENT_CHALLENGE: TrialAvatarGrantRecord.GrantReason
    GRANT_REASON_BY_MIST_TRIAL_ACTIVITY: TrialAvatarGrantRecord.GrantReason
    GRANT_REASON_BY_SUMO_ACTIVITY: TrialAvatarGrantRecord.GrantReason
    GRANT_REASON_BY_POTION_ACTIVITY: TrialAvatarGrantRecord.GrantReason
    GRANT_REASON_BY_CRYSTAL_LINK_ACTIVITY: TrialAvatarGrantRecord.GrantReason
    GRANT_REASON_BY_IRODORI_MASTER: TrialAvatarGrantRecord.GrantReason
    GRANT_REASON_BY_GM: TrialAvatarGrantRecord.GrantReason
    GRANT_REASON_BY_INSTABLE_SPRAY_ACTIVITY: TrialAvatarGrantRecord.GrantReason
    GRANT_REASON_BY_MUQADAS_POTION_ACTIVITY: TrialAvatarGrantRecord.GrantReason
    GRANT_REASON_BY_VINTAGE_HUNTING: TrialAvatarGrantRecord.GrantReason
    GRANT_REASON_BY_CHAR_AMUSEMENT: TrialAvatarGrantRecord.GrantReason
    FJBKKFJNBHD_HMLDNDBKNFL: TrialAvatarGrantRecord.GrantReason
    FJBKKFJNBHD_PJDEJIHFCPP: TrialAvatarGrantRecord.GrantReason
    GRANT_REASON_FIELD_NUMBER: _ClassVar[int]
    FROM_PARENT_QUEST_ID_FIELD_NUMBER: _ClassVar[int]
    grant_reason: int
    from_parent_quest_id: int
    def __init__(self, grant_reason: _Optional[int] = ..., from_parent_quest_id: _Optional[int] = ...) -> None: ...
