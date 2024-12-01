from genshin.packet.proto import HOPIKHOIONP_pb2 as _HOPIKHOIONP_pb2
from genshin.packet.proto import HIJLLEIHODA_pb2 as _HIJLLEIHODA_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BBIKBHKDNPI(_message.Message):
    __slots__ = ("KGAJIKDIHNI", "JOAHNCLHCBH", "PAFLDBLJHFD")
    KGAJIKDIHNI_FIELD_NUMBER: _ClassVar[int]
    JOAHNCLHCBH_FIELD_NUMBER: _ClassVar[int]
    PAFLDBLJHFD_FIELD_NUMBER: _ClassVar[int]
    KGAJIKDIHNI: _containers.RepeatedCompositeFieldContainer[_HOPIKHOIONP_pb2.HOPIKHOIONP]
    JOAHNCLHCBH: _containers.RepeatedCompositeFieldContainer[_HIJLLEIHODA_pb2.HIJLLEIHODA]
    PAFLDBLJHFD: int
    def __init__(self, KGAJIKDIHNI: _Optional[_Iterable[_Union[_HOPIKHOIONP_pb2.HOPIKHOIONP, _Mapping]]] = ..., JOAHNCLHCBH: _Optional[_Iterable[_Union[_HIJLLEIHODA_pb2.HIJLLEIHODA, _Mapping]]] = ..., PAFLDBLJHFD: _Optional[int] = ...) -> None: ...
