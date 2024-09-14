from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarExpeditionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AVATAR_EXPEDITION_STATE_AVATAR_EXPEDITION_NONE: _ClassVar[AvatarExpeditionState]
    AVATAR_EXPEDITION_STATE_AVATAR_EXPEDITION_DOING: _ClassVar[AvatarExpeditionState]
    AVATAR_EXPEDITION_STATE_AVATAR_EXPEDITION_FINISH_WAIT_REWARD: _ClassVar[AvatarExpeditionState]
    AVATAR_EXPEDITION_STATE_AVATAR_EXPEDITION_CALLBACK_WAIT_REWARD: _ClassVar[AvatarExpeditionState]
    AVATAR_EXPEDITION_STATE_AVATAR_EXPEDITION_LOCKED: _ClassVar[AvatarExpeditionState]
AVATAR_EXPEDITION_STATE_AVATAR_EXPEDITION_NONE: AvatarExpeditionState
AVATAR_EXPEDITION_STATE_AVATAR_EXPEDITION_DOING: AvatarExpeditionState
AVATAR_EXPEDITION_STATE_AVATAR_EXPEDITION_FINISH_WAIT_REWARD: AvatarExpeditionState
AVATAR_EXPEDITION_STATE_AVATAR_EXPEDITION_CALLBACK_WAIT_REWARD: AvatarExpeditionState
AVATAR_EXPEDITION_STATE_AVATAR_EXPEDITION_LOCKED: AvatarExpeditionState