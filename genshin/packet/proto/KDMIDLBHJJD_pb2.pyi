from genshin.packet.proto import HDNFFPFFNDN_pb2 as _HDNFFPFFNDN_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KDMIDLBHJJD(_message.Message):
    __slots__ = ("MDMMNLEEMDF", "AGIDBEEINDE", "BDNKLFDGOHK", "FFEKMFFDNAP")
    MDMMNLEEMDF_FIELD_NUMBER: _ClassVar[int]
    AGIDBEEINDE_FIELD_NUMBER: _ClassVar[int]
    BDNKLFDGOHK_FIELD_NUMBER: _ClassVar[int]
    FFEKMFFDNAP_FIELD_NUMBER: _ClassVar[int]
    MDMMNLEEMDF: _HDNFFPFFNDN_pb2.HDNFFPFFNDN
    AGIDBEEINDE: int
    BDNKLFDGOHK: int
    FFEKMFFDNAP: bool
    def __init__(self, MDMMNLEEMDF: _Optional[_Union[_HDNFFPFFNDN_pb2.HDNFFPFFNDN, _Mapping]] = ..., AGIDBEEINDE: _Optional[int] = ..., BDNKLFDGOHK: _Optional[int] = ..., FFEKMFFDNAP: bool = ...) -> None: ...
