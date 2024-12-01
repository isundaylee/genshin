from genshin.packet.proto import AFAILBMMKKA_pb2 as _AFAILBMMKKA_pb2
from genshin.packet.proto import AJCPMKDEBKJ_pb2 as _AJCPMKDEBKJ_pb2
from genshin.packet.proto import NDAIEHPFOLJ_pb2 as _NDAIEHPFOLJ_pb2
from genshin.packet.proto import FGJPIPDNEHD_pb2 as _FGJPIPDNEHD_pb2
from genshin.packet.proto import FEGOJCJLOLN_pb2 as _FEGOJCJLOLN_pb2
from genshin.packet.proto import ODOAHMKGPEL_pb2 as _ODOAHMKGPEL_pb2
from genshin.packet.proto import MBGHHPNOILD_pb2 as _MBGHHPNOILD_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OKAEHFFLKAD(_message.Message):
    __slots__ = ("FAGAEEGLEPE", "KOOCJBIJKAA", "OCPDFCFCIEE", "FAPLKGMKACA", "MGFLDKELPMF", "CJDBDFGEJAO", "ECNPNKLKBLN", "EANPNHBOMKN", "FIKLBLMACIB", "LGLOCKFJODI")
    class FAGAEEGLEPEEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _AFAILBMMKKA_pb2.AFAILBMMKKA
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_AFAILBMMKKA_pb2.AFAILBMMKKA, _Mapping]] = ...) -> None: ...
    class OCPDFCFCIEEEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _NDAIEHPFOLJ_pb2.NDAIEHPFOLJ
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_NDAIEHPFOLJ_pb2.NDAIEHPFOLJ, _Mapping]] = ...) -> None: ...
    class CJDBDFGEJAOEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _ODOAHMKGPEL_pb2.ODOAHMKGPEL
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_ODOAHMKGPEL_pb2.ODOAHMKGPEL, _Mapping]] = ...) -> None: ...
    class EANPNHBOMKNEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _MBGHHPNOILD_pb2.MBGHHPNOILD
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_MBGHHPNOILD_pb2.MBGHHPNOILD, _Mapping]] = ...) -> None: ...
    FAGAEEGLEPE_FIELD_NUMBER: _ClassVar[int]
    KOOCJBIJKAA_FIELD_NUMBER: _ClassVar[int]
    OCPDFCFCIEE_FIELD_NUMBER: _ClassVar[int]
    FAPLKGMKACA_FIELD_NUMBER: _ClassVar[int]
    MGFLDKELPMF_FIELD_NUMBER: _ClassVar[int]
    CJDBDFGEJAO_FIELD_NUMBER: _ClassVar[int]
    ECNPNKLKBLN_FIELD_NUMBER: _ClassVar[int]
    EANPNHBOMKN_FIELD_NUMBER: _ClassVar[int]
    FIKLBLMACIB_FIELD_NUMBER: _ClassVar[int]
    LGLOCKFJODI_FIELD_NUMBER: _ClassVar[int]
    FAGAEEGLEPE: _containers.MessageMap[int, _AFAILBMMKKA_pb2.AFAILBMMKKA]
    KOOCJBIJKAA: _containers.RepeatedCompositeFieldContainer[_AJCPMKDEBKJ_pb2.AJCPMKDEBKJ]
    OCPDFCFCIEE: _containers.MessageMap[int, _NDAIEHPFOLJ_pb2.NDAIEHPFOLJ]
    FAPLKGMKACA: _containers.RepeatedCompositeFieldContainer[_FGJPIPDNEHD_pb2.FGJPIPDNEHD]
    MGFLDKELPMF: _FEGOJCJLOLN_pb2.FEGOJCJLOLN
    CJDBDFGEJAO: _containers.MessageMap[int, _ODOAHMKGPEL_pb2.ODOAHMKGPEL]
    ECNPNKLKBLN: _containers.RepeatedCompositeFieldContainer[_AJCPMKDEBKJ_pb2.AJCPMKDEBKJ]
    EANPNHBOMKN: _containers.MessageMap[int, _MBGHHPNOILD_pb2.MBGHHPNOILD]
    FIKLBLMACIB: int
    LGLOCKFJODI: int
    def __init__(self, FAGAEEGLEPE: _Optional[_Mapping[int, _AFAILBMMKKA_pb2.AFAILBMMKKA]] = ..., KOOCJBIJKAA: _Optional[_Iterable[_Union[_AJCPMKDEBKJ_pb2.AJCPMKDEBKJ, _Mapping]]] = ..., OCPDFCFCIEE: _Optional[_Mapping[int, _NDAIEHPFOLJ_pb2.NDAIEHPFOLJ]] = ..., FAPLKGMKACA: _Optional[_Iterable[_Union[_FGJPIPDNEHD_pb2.FGJPIPDNEHD, _Mapping]]] = ..., MGFLDKELPMF: _Optional[_Union[_FEGOJCJLOLN_pb2.FEGOJCJLOLN, _Mapping]] = ..., CJDBDFGEJAO: _Optional[_Mapping[int, _ODOAHMKGPEL_pb2.ODOAHMKGPEL]] = ..., ECNPNKLKBLN: _Optional[_Iterable[_Union[_AJCPMKDEBKJ_pb2.AJCPMKDEBKJ, _Mapping]]] = ..., EANPNHBOMKN: _Optional[_Mapping[int, _MBGHHPNOILD_pb2.MBGHHPNOILD]] = ..., FIKLBLMACIB: _Optional[int] = ..., LGLOCKFJODI: _Optional[int] = ...) -> None: ...
