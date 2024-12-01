from genshin.packet.proto import KDEHCGJAGFJ_pb2 as _KDEHCGJAGFJ_pb2
from genshin.packet.proto import DMDININEFDG_pb2 as _DMDININEFDG_pb2
from genshin.packet.proto import EIEMABMNOLO_pb2 as _EIEMABMNOLO_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PCOMGJBEDCB(_message.Message):
    __slots__ = ("BFMMHKFPCJB", "GJEBAJAJPII", "PJABEFAJBGB", "BIHHIKJCIAH", "IGBDOEBPPHO", "EALJHPFDEHK", "JGCCKLNFEHE", "FFOBIONLMOJ")
    BFMMHKFPCJB_FIELD_NUMBER: _ClassVar[int]
    GJEBAJAJPII_FIELD_NUMBER: _ClassVar[int]
    PJABEFAJBGB_FIELD_NUMBER: _ClassVar[int]
    BIHHIKJCIAH_FIELD_NUMBER: _ClassVar[int]
    IGBDOEBPPHO_FIELD_NUMBER: _ClassVar[int]
    EALJHPFDEHK_FIELD_NUMBER: _ClassVar[int]
    JGCCKLNFEHE_FIELD_NUMBER: _ClassVar[int]
    FFOBIONLMOJ_FIELD_NUMBER: _ClassVar[int]
    BFMMHKFPCJB: str
    GJEBAJAJPII: _KDEHCGJAGFJ_pb2.KDEHCGJAGFJ
    PJABEFAJBGB: int
    BIHHIKJCIAH: _DMDININEFDG_pb2.DMDININEFDG
    IGBDOEBPPHO: int
    EALJHPFDEHK: int
    JGCCKLNFEHE: _EIEMABMNOLO_pb2.EIEMABMNOLO
    FFOBIONLMOJ: int
    def __init__(self, BFMMHKFPCJB: _Optional[str] = ..., GJEBAJAJPII: _Optional[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]] = ..., PJABEFAJBGB: _Optional[int] = ..., BIHHIKJCIAH: _Optional[_Union[_DMDININEFDG_pb2.DMDININEFDG, str]] = ..., IGBDOEBPPHO: _Optional[int] = ..., EALJHPFDEHK: _Optional[int] = ..., JGCCKLNFEHE: _Optional[_Union[_EIEMABMNOLO_pb2.EIEMABMNOLO, str]] = ..., FFOBIONLMOJ: _Optional[int] = ...) -> None: ...
