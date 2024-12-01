from genshin.packet.proto import NHNLJIBHPMJ_pb2 as _NHNLJIBHPMJ_pb2
from genshin.packet.proto import KHJMIKAAFHB_pb2 as _KHJMIKAAFHB_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CLFNCMGFGPC(_message.Message):
    __slots__ = ("AMOLHEFINEK", "MEHKOPGFFHM", "HPFCCAFCHDH")
    AMOLHEFINEK_FIELD_NUMBER: _ClassVar[int]
    MEHKOPGFFHM_FIELD_NUMBER: _ClassVar[int]
    HPFCCAFCHDH_FIELD_NUMBER: _ClassVar[int]
    AMOLHEFINEK: _NHNLJIBHPMJ_pb2.NHNLJIBHPMJ
    MEHKOPGFFHM: _KHJMIKAAFHB_pb2.KHJMIKAAFHB
    HPFCCAFCHDH: bool
    def __init__(self, AMOLHEFINEK: _Optional[_Union[_NHNLJIBHPMJ_pb2.NHNLJIBHPMJ, _Mapping]] = ..., MEHKOPGFFHM: _Optional[_Union[_KHJMIKAAFHB_pb2.KHJMIKAAFHB, _Mapping]] = ..., HPFCCAFCHDH: bool = ...) -> None: ...
