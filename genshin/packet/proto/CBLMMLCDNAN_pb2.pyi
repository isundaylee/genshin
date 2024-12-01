from genshin.packet.proto import IPFHGELOANB_pb2 as _IPFHGELOANB_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CBLMMLCDNAN(_message.Message):
    __slots__ = ("MJOCKFMGCBG", "IAEEGKBCHOH", "DDIBJFCLGOB", "CGDPDDAENIE", "GAMMCKBFPHM", "MNPJCKKCHNC", "EJNINFFFKJP")
    MJOCKFMGCBG_FIELD_NUMBER: _ClassVar[int]
    IAEEGKBCHOH_FIELD_NUMBER: _ClassVar[int]
    DDIBJFCLGOB_FIELD_NUMBER: _ClassVar[int]
    CGDPDDAENIE_FIELD_NUMBER: _ClassVar[int]
    GAMMCKBFPHM_FIELD_NUMBER: _ClassVar[int]
    MNPJCKKCHNC_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    MJOCKFMGCBG: bytes
    IAEEGKBCHOH: bytes
    DDIBJFCLGOB: str
    CGDPDDAENIE: bytes
    GAMMCKBFPHM: str
    MNPJCKKCHNC: _IPFHGELOANB_pb2.IPFHGELOANB
    EJNINFFFKJP: int
    def __init__(self, MJOCKFMGCBG: _Optional[bytes] = ..., IAEEGKBCHOH: _Optional[bytes] = ..., DDIBJFCLGOB: _Optional[str] = ..., CGDPDDAENIE: _Optional[bytes] = ..., GAMMCKBFPHM: _Optional[str] = ..., MNPJCKKCHNC: _Optional[_Union[_IPFHGELOANB_pb2.IPFHGELOANB, _Mapping]] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
