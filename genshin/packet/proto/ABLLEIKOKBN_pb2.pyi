from genshin.packet.proto import HDPFODICAAN_pb2 as _HDPFODICAAN_pb2
from genshin.packet.proto import CLINDENDFKL_pb2 as _CLINDENDFKL_pb2
from genshin.packet.proto import NFILMAGDNGJ_pb2 as _NFILMAGDNGJ_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ABLLEIKOKBN(_message.Message):
    __slots__ = ("KGKEDKPMDPL", "ADOFOOABKFO", "DLHGOHEKHJH")
    KGKEDKPMDPL_FIELD_NUMBER: _ClassVar[int]
    ADOFOOABKFO_FIELD_NUMBER: _ClassVar[int]
    DLHGOHEKHJH_FIELD_NUMBER: _ClassVar[int]
    KGKEDKPMDPL: _HDPFODICAAN_pb2.HDPFODICAAN
    ADOFOOABKFO: _CLINDENDFKL_pb2.CLINDENDFKL
    DLHGOHEKHJH: _NFILMAGDNGJ_pb2.NFILMAGDNGJ
    def __init__(self, KGKEDKPMDPL: _Optional[_Union[_HDPFODICAAN_pb2.HDPFODICAAN, _Mapping]] = ..., ADOFOOABKFO: _Optional[_Union[_CLINDENDFKL_pb2.CLINDENDFKL, _Mapping]] = ..., DLHGOHEKHJH: _Optional[_Union[_NFILMAGDNGJ_pb2.NFILMAGDNGJ, _Mapping]] = ...) -> None: ...
