from genshin.packet.proto import BGDCPBEGANK_pb2 as _BGDCPBEGANK_pb2
from genshin.packet.proto import NNLFBHCELOG_pb2 as _NNLFBHCELOG_pb2
from genshin.packet.proto import NMBNHIOGAJK_pb2 as _NMBNHIOGAJK_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HLJFHHIKKEN(_message.Message):
    __slots__ = ("NEFMGJIDAAK", "LDIAJBOKPHB", "IDBADJONFOJ", "IONMDBJFHCN", "OMKGPFGKFNB", "MONEJDBPOLB", "IOBNFNDNEAL", "ABHDEMELCDN", "LPNKAMMEFCB", "FCPECPMOGOJ")
    NEFMGJIDAAK_FIELD_NUMBER: _ClassVar[int]
    LDIAJBOKPHB_FIELD_NUMBER: _ClassVar[int]
    IDBADJONFOJ_FIELD_NUMBER: _ClassVar[int]
    IONMDBJFHCN_FIELD_NUMBER: _ClassVar[int]
    OMKGPFGKFNB_FIELD_NUMBER: _ClassVar[int]
    MONEJDBPOLB_FIELD_NUMBER: _ClassVar[int]
    IOBNFNDNEAL_FIELD_NUMBER: _ClassVar[int]
    ABHDEMELCDN_FIELD_NUMBER: _ClassVar[int]
    LPNKAMMEFCB_FIELD_NUMBER: _ClassVar[int]
    FCPECPMOGOJ_FIELD_NUMBER: _ClassVar[int]
    NEFMGJIDAAK: _containers.RepeatedCompositeFieldContainer[_BGDCPBEGANK_pb2.BGDCPBEGANK]
    LDIAJBOKPHB: _NNLFBHCELOG_pb2.NNLFBHCELOG
    IDBADJONFOJ: _containers.RepeatedScalarFieldContainer[int]
    IONMDBJFHCN: _containers.RepeatedScalarFieldContainer[int]
    OMKGPFGKFNB: _containers.RepeatedScalarFieldContainer[int]
    MONEJDBPOLB: int
    IOBNFNDNEAL: bool
    ABHDEMELCDN: bool
    LPNKAMMEFCB: _NMBNHIOGAJK_pb2.NMBNHIOGAJK
    FCPECPMOGOJ: int
    def __init__(self, NEFMGJIDAAK: _Optional[_Iterable[_Union[_BGDCPBEGANK_pb2.BGDCPBEGANK, _Mapping]]] = ..., LDIAJBOKPHB: _Optional[_Union[_NNLFBHCELOG_pb2.NNLFBHCELOG, _Mapping]] = ..., IDBADJONFOJ: _Optional[_Iterable[int]] = ..., IONMDBJFHCN: _Optional[_Iterable[int]] = ..., OMKGPFGKFNB: _Optional[_Iterable[int]] = ..., MONEJDBPOLB: _Optional[int] = ..., IOBNFNDNEAL: bool = ..., ABHDEMELCDN: bool = ..., LPNKAMMEFCB: _Optional[_Union[_NMBNHIOGAJK_pb2.NMBNHIOGAJK, str]] = ..., FCPECPMOGOJ: _Optional[int] = ...) -> None: ...
