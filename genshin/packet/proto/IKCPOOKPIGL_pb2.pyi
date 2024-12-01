from genshin.packet.proto import GPEIBBJNHDA_pb2 as _GPEIBBJNHDA_pb2
from genshin.packet.proto import PLCGIEAONLG_pb2 as _PLCGIEAONLG_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IKCPOOKPIGL(_message.Message):
    __slots__ = ("PJKJCBDHMFH", "ONOGCEHFHFP", "avatar_list", "OAJOOBGHAGM", "AGMHMDHEFKD")
    class PJKJCBDHMFHEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _GPEIBBJNHDA_pb2.GPEIBBJNHDA
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_GPEIBBJNHDA_pb2.GPEIBBJNHDA, str]] = ...) -> None: ...
    PJKJCBDHMFH_FIELD_NUMBER: _ClassVar[int]
    ONOGCEHFHFP_FIELD_NUMBER: _ClassVar[int]
    AVATAR_LIST_FIELD_NUMBER: _ClassVar[int]
    OAJOOBGHAGM_FIELD_NUMBER: _ClassVar[int]
    AGMHMDHEFKD_FIELD_NUMBER: _ClassVar[int]
    PJKJCBDHMFH: _containers.ScalarMap[int, _GPEIBBJNHDA_pb2.GPEIBBJNHDA]
    ONOGCEHFHFP: _containers.RepeatedScalarFieldContainer[int]
    avatar_list: _containers.RepeatedCompositeFieldContainer[_PLCGIEAONLG_pb2.PLCGIEAONLG]
    OAJOOBGHAGM: int
    AGMHMDHEFKD: int
    def __init__(self, PJKJCBDHMFH: _Optional[_Mapping[int, _GPEIBBJNHDA_pb2.GPEIBBJNHDA]] = ..., ONOGCEHFHFP: _Optional[_Iterable[int]] = ..., avatar_list: _Optional[_Iterable[_Union[_PLCGIEAONLG_pb2.PLCGIEAONLG, _Mapping]]] = ..., OAJOOBGHAGM: _Optional[int] = ..., AGMHMDHEFKD: _Optional[int] = ...) -> None: ...
