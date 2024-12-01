from genshin.packet.proto import FBONNIGMEIP_pb2 as _FBONNIGMEIP_pb2
from genshin.packet.proto import AJLCOMMPDIC_pb2 as _AJLCOMMPDIC_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AONPGPIPNCE(_message.Message):
    __slots__ = ("LKFGEAGBPGA", "NIHANLGJPLA", "IMIOGMDOKCB", "JJDJDFCEFCK", "EBLJFMCMDGD", "OALFNNIOHCM")
    LKFGEAGBPGA_FIELD_NUMBER: _ClassVar[int]
    NIHANLGJPLA_FIELD_NUMBER: _ClassVar[int]
    IMIOGMDOKCB_FIELD_NUMBER: _ClassVar[int]
    JJDJDFCEFCK_FIELD_NUMBER: _ClassVar[int]
    EBLJFMCMDGD_FIELD_NUMBER: _ClassVar[int]
    OALFNNIOHCM_FIELD_NUMBER: _ClassVar[int]
    LKFGEAGBPGA: str
    NIHANLGJPLA: str
    IMIOGMDOKCB: _FBONNIGMEIP_pb2.FBONNIGMEIP
    JJDJDFCEFCK: int
    EBLJFMCMDGD: int
    OALFNNIOHCM: _AJLCOMMPDIC_pb2.AJLCOMMPDIC
    def __init__(self, LKFGEAGBPGA: _Optional[str] = ..., NIHANLGJPLA: _Optional[str] = ..., IMIOGMDOKCB: _Optional[_Union[_FBONNIGMEIP_pb2.FBONNIGMEIP, str]] = ..., JJDJDFCEFCK: _Optional[int] = ..., EBLJFMCMDGD: _Optional[int] = ..., OALFNNIOHCM: _Optional[_Union[_AJLCOMMPDIC_pb2.AJLCOMMPDIC, str]] = ...) -> None: ...
