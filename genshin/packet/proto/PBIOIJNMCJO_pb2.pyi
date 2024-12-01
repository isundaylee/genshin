from genshin.packet.proto import BAADCBGPEFO_pb2 as _BAADCBGPEFO_pb2
from genshin.packet.proto import CMGOOOMLAIA_pb2 as _CMGOOOMLAIA_pb2
from genshin.packet.proto import KBAIOMIOCCP_pb2 as _KBAIOMIOCCP_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PBIOIJNMCJO(_message.Message):
    __slots__ = ("LGFPFKPANPI", "IMIOGMDOKCB", "JMLABOBCLDE")
    LGFPFKPANPI_FIELD_NUMBER: _ClassVar[int]
    IMIOGMDOKCB_FIELD_NUMBER: _ClassVar[int]
    JMLABOBCLDE_FIELD_NUMBER: _ClassVar[int]
    LGFPFKPANPI: _containers.RepeatedCompositeFieldContainer[_BAADCBGPEFO_pb2.BAADCBGPEFO]
    IMIOGMDOKCB: _CMGOOOMLAIA_pb2.CMGOOOMLAIA
    JMLABOBCLDE: _KBAIOMIOCCP_pb2.KBAIOMIOCCP
    def __init__(self, LGFPFKPANPI: _Optional[_Iterable[_Union[_BAADCBGPEFO_pb2.BAADCBGPEFO, _Mapping]]] = ..., IMIOGMDOKCB: _Optional[_Union[_CMGOOOMLAIA_pb2.CMGOOOMLAIA, str]] = ..., JMLABOBCLDE: _Optional[_Union[_KBAIOMIOCCP_pb2.KBAIOMIOCCP, str]] = ...) -> None: ...
