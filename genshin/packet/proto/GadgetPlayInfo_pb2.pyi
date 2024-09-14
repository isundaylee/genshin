from genshin.packet.proto import GadgetCrucibleInfo_pb2 as _GadgetCrucibleInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GadgetPlayInfo(_message.Message):
    __slots__ = ("play_type", "duration", "progress_stage_list", "start_cd", "start_time", "progress", "crucible_info")
    PLAY_TYPE_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_STAGE_LIST_FIELD_NUMBER: _ClassVar[int]
    START_CD_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    CRUCIBLE_INFO_FIELD_NUMBER: _ClassVar[int]
    play_type: int
    duration: int
    progress_stage_list: _containers.RepeatedScalarFieldContainer[int]
    start_cd: int
    start_time: int
    progress: int
    crucible_info: _GadgetCrucibleInfo_pb2.GadgetCrucibleInfo
    def __init__(self, play_type: _Optional[int] = ..., duration: _Optional[int] = ..., progress_stage_list: _Optional[_Iterable[int]] = ..., start_cd: _Optional[int] = ..., start_time: _Optional[int] = ..., progress: _Optional[int] = ..., crucible_info: _Optional[_Union[_GadgetCrucibleInfo_pb2.GadgetCrucibleInfo, _Mapping]] = ...) -> None: ...
