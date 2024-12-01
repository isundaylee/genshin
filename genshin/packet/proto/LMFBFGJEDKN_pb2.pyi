from genshin.packet.proto import HMGBJNNDKEM_pb2 as _HMGBJNNDKEM_pb2
from genshin.packet.proto import KKHBLIPJOBE_pb2 as _KKHBLIPJOBE_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LMFBFGJEDKN(_message.Message):
    __slots__ = ("HDCJFKPPLFC", "JAJAKIIIAPI", "EJNINFFFKJP")
    HDCJFKPPLFC_FIELD_NUMBER: _ClassVar[int]
    JAJAKIIIAPI_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    HDCJFKPPLFC: _containers.RepeatedCompositeFieldContainer[_HMGBJNNDKEM_pb2.HMGBJNNDKEM]
    JAJAKIIIAPI: _KKHBLIPJOBE_pb2.KKHBLIPJOBE
    EJNINFFFKJP: int
    def __init__(self, HDCJFKPPLFC: _Optional[_Iterable[_Union[_HMGBJNNDKEM_pb2.HMGBJNNDKEM, _Mapping]]] = ..., JAJAKIIIAPI: _Optional[_Union[_KKHBLIPJOBE_pb2.KKHBLIPJOBE, _Mapping]] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
