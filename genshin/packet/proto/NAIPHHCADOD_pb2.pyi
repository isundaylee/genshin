from genshin.packet.proto import BKCINFMCJLJ_pb2 as _BKCINFMCJLJ_pb2
from genshin.packet.proto import ELENLLNEHNE_pb2 as _ELENLLNEHNE_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NAIPHHCADOD(_message.Message):
    __slots__ = ("AFLHEFEDFBE", "EJNINFFFKJP", "AMGMMKEDDMK")
    AFLHEFEDFBE_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    AMGMMKEDDMK_FIELD_NUMBER: _ClassVar[int]
    AFLHEFEDFBE: _BKCINFMCJLJ_pb2.BKCINFMCJLJ
    EJNINFFFKJP: int
    AMGMMKEDDMK: _ELENLLNEHNE_pb2.ELENLLNEHNE
    def __init__(self, AFLHEFEDFBE: _Optional[_Union[_BKCINFMCJLJ_pb2.BKCINFMCJLJ, _Mapping]] = ..., EJNINFFFKJP: _Optional[int] = ..., AMGMMKEDDMK: _Optional[_Union[_ELENLLNEHNE_pb2.ELENLLNEHNE, str]] = ...) -> None: ...
