from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class MailCollectState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MAIL_COLLECT_STATE_COLLECTIBLE_UNKNOWN: _ClassVar[MailCollectState]
    MAIL_COLLECT_STATE_NOT_COLLECTIBLE: _ClassVar[MailCollectState]
    MAIL_COLLECT_STATE_COLLECTIBLE_UNCOLLECTED: _ClassVar[MailCollectState]
    MAIL_COLLECT_STATE_COLLECTIBLE_COLLECTED: _ClassVar[MailCollectState]
MAIL_COLLECT_STATE_COLLECTIBLE_UNKNOWN: MailCollectState
MAIL_COLLECT_STATE_NOT_COLLECTIBLE: MailCollectState
MAIL_COLLECT_STATE_COLLECTIBLE_UNCOLLECTED: MailCollectState
MAIL_COLLECT_STATE_COLLECTIBLE_COLLECTED: MailCollectState
