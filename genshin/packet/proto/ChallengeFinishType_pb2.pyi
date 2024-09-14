from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ChallengeFinishType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ChallengeFinishType_NONE: _ClassVar[ChallengeFinishType]
    ChallengeFinishType_FAIL: _ClassVar[ChallengeFinishType]
    ChallengeFinishType_SUCC: _ClassVar[ChallengeFinishType]
    ChallengeFinishType_PAUSE: _ClassVar[ChallengeFinishType]
ChallengeFinishType_NONE: ChallengeFinishType
ChallengeFinishType_FAIL: ChallengeFinishType
ChallengeFinishType_SUCC: ChallengeFinishType
ChallengeFinishType_PAUSE: ChallengeFinishType
