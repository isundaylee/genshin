from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class MissionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MISSION_INVALID: _ClassVar[MissionStatus]
    MISSION_UNFINISHED: _ClassVar[MissionStatus]
    MISSION_FINISHED: _ClassVar[MissionStatus]
    MISSION_POINT_TAKEN: _ClassVar[MissionStatus]
MISSION_INVALID: MissionStatus
MISSION_UNFINISHED: MissionStatus
MISSION_FINISHED: MissionStatus
MISSION_POINT_TAKEN: MissionStatus
