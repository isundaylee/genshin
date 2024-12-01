from genshin.packet.proto import KDEHCGJAGFJ_pb2 as _KDEHCGJAGFJ_pb2
from genshin.packet.proto import HAOGHPBGFPF_pb2 as _HAOGHPBGFPF_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NPAJIDCHFFJ(_message.Message):
    __slots__ = ("OCNAEJFMCAG", "KDBJKIFIEJH", "EGEBLKIOPLK", "ONIMBHEFLKJ", "ECIFINMNLND", "EJNINFFFKJP")
    OCNAEJFMCAG_FIELD_NUMBER: _ClassVar[int]
    KDBJKIFIEJH_FIELD_NUMBER: _ClassVar[int]
    EGEBLKIOPLK_FIELD_NUMBER: _ClassVar[int]
    ONIMBHEFLKJ_FIELD_NUMBER: _ClassVar[int]
    ECIFINMNLND_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    OCNAEJFMCAG: _containers.RepeatedCompositeFieldContainer[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ]
    KDBJKIFIEJH: _containers.RepeatedCompositeFieldContainer[_HAOGHPBGFPF_pb2.HAOGHPBGFPF]
    EGEBLKIOPLK: _containers.RepeatedCompositeFieldContainer[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ]
    ONIMBHEFLKJ: _containers.RepeatedCompositeFieldContainer[_HAOGHPBGFPF_pb2.HAOGHPBGFPF]
    ECIFINMNLND: int
    EJNINFFFKJP: int
    def __init__(self, OCNAEJFMCAG: _Optional[_Iterable[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]]] = ..., KDBJKIFIEJH: _Optional[_Iterable[_Union[_HAOGHPBGFPF_pb2.HAOGHPBGFPF, _Mapping]]] = ..., EGEBLKIOPLK: _Optional[_Iterable[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]]] = ..., ONIMBHEFLKJ: _Optional[_Iterable[_Union[_HAOGHPBGFPF_pb2.HAOGHPBGFPF, _Mapping]]] = ..., ECIFINMNLND: _Optional[int] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
