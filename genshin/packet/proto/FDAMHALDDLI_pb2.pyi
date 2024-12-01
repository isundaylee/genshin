from genshin.packet.proto import HGMNLAGDFDC_pb2 as _HGMNLAGDFDC_pb2
from genshin.packet.proto import HFHJKHOPLMN_pb2 as _HFHJKHOPLMN_pb2
from genshin.packet.proto import PKJMPCPEGGO_pb2 as _PKJMPCPEGGO_pb2
from genshin.packet.proto import DMAJHDNKEDI_pb2 as _DMAJHDNKEDI_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FDAMHALDDLI(_message.Message):
    __slots__ = ("EFAJIHMNOBK", "FGAEINCCKDK", "OMKNBNMEBIK", "HCEJPKIAJAP", "IANEBDKAMBM", "AMLIJKENIIN", "KNJPPIFOFME", "OMENIAMEDCE", "EDNALCKIJPG", "DPBDBMIIOMP")
    EFAJIHMNOBK_FIELD_NUMBER: _ClassVar[int]
    FGAEINCCKDK_FIELD_NUMBER: _ClassVar[int]
    OMKNBNMEBIK_FIELD_NUMBER: _ClassVar[int]
    HCEJPKIAJAP_FIELD_NUMBER: _ClassVar[int]
    IANEBDKAMBM_FIELD_NUMBER: _ClassVar[int]
    AMLIJKENIIN_FIELD_NUMBER: _ClassVar[int]
    KNJPPIFOFME_FIELD_NUMBER: _ClassVar[int]
    OMENIAMEDCE_FIELD_NUMBER: _ClassVar[int]
    EDNALCKIJPG_FIELD_NUMBER: _ClassVar[int]
    DPBDBMIIOMP_FIELD_NUMBER: _ClassVar[int]
    EFAJIHMNOBK: str
    FGAEINCCKDK: _HGMNLAGDFDC_pb2.HGMNLAGDFDC
    OMKNBNMEBIK: str
    HCEJPKIAJAP: _containers.RepeatedCompositeFieldContainer[_HFHJKHOPLMN_pb2.HFHJKHOPLMN]
    IANEBDKAMBM: _PKJMPCPEGGO_pb2.PKJMPCPEGGO
    AMLIJKENIIN: _DMAJHDNKEDI_pb2.DMAJHDNKEDI
    KNJPPIFOFME: bool
    OMENIAMEDCE: bool
    EDNALCKIJPG: int
    DPBDBMIIOMP: int
    def __init__(self, EFAJIHMNOBK: _Optional[str] = ..., FGAEINCCKDK: _Optional[_Union[_HGMNLAGDFDC_pb2.HGMNLAGDFDC, _Mapping]] = ..., OMKNBNMEBIK: _Optional[str] = ..., HCEJPKIAJAP: _Optional[_Iterable[_Union[_HFHJKHOPLMN_pb2.HFHJKHOPLMN, _Mapping]]] = ..., IANEBDKAMBM: _Optional[_Union[_PKJMPCPEGGO_pb2.PKJMPCPEGGO, _Mapping]] = ..., AMLIJKENIIN: _Optional[_Union[_DMAJHDNKEDI_pb2.DMAJHDNKEDI, str]] = ..., KNJPPIFOFME: bool = ..., OMENIAMEDCE: bool = ..., EDNALCKIJPG: _Optional[int] = ..., DPBDBMIIOMP: _Optional[int] = ...) -> None: ...
