from genshin.packet.proto import FetterData_pb2 as _FetterData_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarFetterInfo(_message.Message):
    __slots__ = ("exp_number", "exp_level", "open_id_list", "finish_id_list", "rewarded_fetter_level_list", "fetter_list")
    EXP_NUMBER_FIELD_NUMBER: _ClassVar[int]
    EXP_LEVEL_FIELD_NUMBER: _ClassVar[int]
    OPEN_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    FINISH_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    REWARDED_FETTER_LEVEL_LIST_FIELD_NUMBER: _ClassVar[int]
    FETTER_LIST_FIELD_NUMBER: _ClassVar[int]
    exp_number: int
    exp_level: int
    open_id_list: _containers.RepeatedScalarFieldContainer[int]
    finish_id_list: _containers.RepeatedScalarFieldContainer[int]
    rewarded_fetter_level_list: _containers.RepeatedScalarFieldContainer[int]
    fetter_list: _containers.RepeatedCompositeFieldContainer[_FetterData_pb2.FetterData]
    def __init__(self, exp_number: _Optional[int] = ..., exp_level: _Optional[int] = ..., open_id_list: _Optional[_Iterable[int]] = ..., finish_id_list: _Optional[_Iterable[int]] = ..., rewarded_fetter_level_list: _Optional[_Iterable[int]] = ..., fetter_list: _Optional[_Iterable[_Union[_FetterData_pb2.FetterData, _Mapping]]] = ...) -> None: ...
