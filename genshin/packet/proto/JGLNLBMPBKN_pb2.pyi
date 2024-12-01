from genshin.packet.proto import CNHLJKCJAHB_pb2 as _CNHLJKCJAHB_pb2
from genshin.packet.proto import LJJFJILBNLL_pb2 as _LJJFJILBNLL_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JGLNLBMPBKN(_message.Message):
    __slots__ = ("KFEDMCEKGMK", "ICCHDGKMNLF")
    KFEDMCEKGMK_FIELD_NUMBER: _ClassVar[int]
    ICCHDGKMNLF_FIELD_NUMBER: _ClassVar[int]
    KFEDMCEKGMK: _CNHLJKCJAHB_pb2.CNHLJKCJAHB
    ICCHDGKMNLF: _LJJFJILBNLL_pb2.LJJFJILBNLL
    def __init__(self, KFEDMCEKGMK: _Optional[_Union[_CNHLJKCJAHB_pb2.CNHLJKCJAHB, _Mapping]] = ..., ICCHDGKMNLF: _Optional[_Union[_LJJFJILBNLL_pb2.LJJFJILBNLL, _Mapping]] = ...) -> None: ...
