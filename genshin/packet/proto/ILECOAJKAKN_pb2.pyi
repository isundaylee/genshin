from genshin.packet.proto import GBMACCKLNJE_pb2 as _GBMACCKLNJE_pb2
from genshin.packet.proto import JCFMHOHIDOD_pb2 as _JCFMHOHIDOD_pb2
from genshin.packet.proto import OFBHCGGGGGN_pb2 as _OFBHCGGGGGN_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ILECOAJKAKN(_message.Message):
    __slots__ = ("GOGOFPNOKBK", "JAEBIMKPKFE", "AGNJKCKECBO", "FMIEBPKJJPJ", "OAJOOBGHAGM", "POAFICPFPCJ", "MONEJDBPOLB", "AMLIJKENIIN", "OEDOJBLAMDM", "HCJFDJHILAM")
    class AGNJKCKECBOEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _JCFMHOHIDOD_pb2.JCFMHOHIDOD
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_JCFMHOHIDOD_pb2.JCFMHOHIDOD, _Mapping]] = ...) -> None: ...
    class FMIEBPKJJPJEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _OFBHCGGGGGN_pb2.OFBHCGGGGGN
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_OFBHCGGGGGN_pb2.OFBHCGGGGGN, _Mapping]] = ...) -> None: ...
    GOGOFPNOKBK_FIELD_NUMBER: _ClassVar[int]
    JAEBIMKPKFE_FIELD_NUMBER: _ClassVar[int]
    AGNJKCKECBO_FIELD_NUMBER: _ClassVar[int]
    FMIEBPKJJPJ_FIELD_NUMBER: _ClassVar[int]
    OAJOOBGHAGM_FIELD_NUMBER: _ClassVar[int]
    POAFICPFPCJ_FIELD_NUMBER: _ClassVar[int]
    MONEJDBPOLB_FIELD_NUMBER: _ClassVar[int]
    AMLIJKENIIN_FIELD_NUMBER: _ClassVar[int]
    OEDOJBLAMDM_FIELD_NUMBER: _ClassVar[int]
    HCJFDJHILAM_FIELD_NUMBER: _ClassVar[int]
    GOGOFPNOKBK: _containers.RepeatedScalarFieldContainer[int]
    JAEBIMKPKFE: _containers.RepeatedCompositeFieldContainer[_GBMACCKLNJE_pb2.GBMACCKLNJE]
    AGNJKCKECBO: _containers.MessageMap[int, _JCFMHOHIDOD_pb2.JCFMHOHIDOD]
    FMIEBPKJJPJ: _containers.MessageMap[int, _OFBHCGGGGGN_pb2.OFBHCGGGGGN]
    OAJOOBGHAGM: int
    POAFICPFPCJ: int
    MONEJDBPOLB: int
    AMLIJKENIIN: int
    OEDOJBLAMDM: int
    HCJFDJHILAM: bool
    def __init__(self, GOGOFPNOKBK: _Optional[_Iterable[int]] = ..., JAEBIMKPKFE: _Optional[_Iterable[_Union[_GBMACCKLNJE_pb2.GBMACCKLNJE, _Mapping]]] = ..., AGNJKCKECBO: _Optional[_Mapping[int, _JCFMHOHIDOD_pb2.JCFMHOHIDOD]] = ..., FMIEBPKJJPJ: _Optional[_Mapping[int, _OFBHCGGGGGN_pb2.OFBHCGGGGGN]] = ..., OAJOOBGHAGM: _Optional[int] = ..., POAFICPFPCJ: _Optional[int] = ..., MONEJDBPOLB: _Optional[int] = ..., AMLIJKENIIN: _Optional[int] = ..., OEDOJBLAMDM: _Optional[int] = ..., HCJFDJHILAM: bool = ...) -> None: ...
