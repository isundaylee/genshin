from genshin.packet.proto import LAADOJLABDH_pb2 as _LAADOJLABDH_pb2
from genshin.packet.proto import PAGIAOELFBI_pb2 as _PAGIAOELFBI_pb2
from genshin.packet.proto import ELENLLNEHNE_pb2 as _ELENLLNEHNE_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BONLFJGNBIB(_message.Message):
    __slots__ = ("NGANCEICGHC", "EIMCFAMHHBJ", "AMGMMKEDDMK", "EJNINFFFKJP")
    NGANCEICGHC_FIELD_NUMBER: _ClassVar[int]
    EIMCFAMHHBJ_FIELD_NUMBER: _ClassVar[int]
    AMGMMKEDDMK_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    NGANCEICGHC: _LAADOJLABDH_pb2.LAADOJLABDH
    EIMCFAMHHBJ: _PAGIAOELFBI_pb2.PAGIAOELFBI
    AMGMMKEDDMK: _ELENLLNEHNE_pb2.ELENLLNEHNE
    EJNINFFFKJP: int
    def __init__(self, NGANCEICGHC: _Optional[_Union[_LAADOJLABDH_pb2.LAADOJLABDH, _Mapping]] = ..., EIMCFAMHHBJ: _Optional[_Union[_PAGIAOELFBI_pb2.PAGIAOELFBI, _Mapping]] = ..., AMGMMKEDDMK: _Optional[_Union[_ELENLLNEHNE_pb2.ELENLLNEHNE, str]] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
