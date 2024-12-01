from genshin.packet.proto import APDDLGFJONM_pb2 as _APDDLGFJONM_pb2
from genshin.packet.proto import ALCMFILLBKD_pb2 as _ALCMFILLBKD_pb2
from genshin.packet.proto import JEHLCIMIJGN_pb2 as _JEHLCIMIJGN_pb2
from genshin.packet.proto import NFPLLBBAPIM_pb2 as _NFPLLBBAPIM_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NBNOOMEKHIE(_message.Message):
    __slots__ = ("BFMEOMIAEEK", "KCBMIPFEADJ", "NBKMBDEOPEI", "BFAFICCJAAA")
    BFMEOMIAEEK_FIELD_NUMBER: _ClassVar[int]
    KCBMIPFEADJ_FIELD_NUMBER: _ClassVar[int]
    NBKMBDEOPEI_FIELD_NUMBER: _ClassVar[int]
    BFAFICCJAAA_FIELD_NUMBER: _ClassVar[int]
    BFMEOMIAEEK: _APDDLGFJONM_pb2.APDDLGFJONM
    KCBMIPFEADJ: _ALCMFILLBKD_pb2.ALCMFILLBKD
    NBKMBDEOPEI: _JEHLCIMIJGN_pb2.JEHLCIMIJGN
    BFAFICCJAAA: _NFPLLBBAPIM_pb2.NFPLLBBAPIM
    def __init__(self, BFMEOMIAEEK: _Optional[_Union[_APDDLGFJONM_pb2.APDDLGFJONM, _Mapping]] = ..., KCBMIPFEADJ: _Optional[_Union[_ALCMFILLBKD_pb2.ALCMFILLBKD, _Mapping]] = ..., NBKMBDEOPEI: _Optional[_Union[_JEHLCIMIJGN_pb2.JEHLCIMIJGN, _Mapping]] = ..., BFAFICCJAAA: _Optional[_Union[_NFPLLBBAPIM_pb2.NFPLLBBAPIM, _Mapping]] = ...) -> None: ...
