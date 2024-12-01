from genshin.packet.proto import JICKPPDLOHC_pb2 as _JICKPPDLOHC_pb2
from genshin.packet.proto import BDKCBBNPJHM_pb2 as _BDKCBBNPJHM_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HPMAENKJCOJ(_message.Message):
    __slots__ = ("MGDPFNIIFEA", "CNAJAFLIBED", "HGBBGLKPLFI", "FBCEKPOMNAI", "FDPPPBPOEMP")
    MGDPFNIIFEA_FIELD_NUMBER: _ClassVar[int]
    CNAJAFLIBED_FIELD_NUMBER: _ClassVar[int]
    HGBBGLKPLFI_FIELD_NUMBER: _ClassVar[int]
    FBCEKPOMNAI_FIELD_NUMBER: _ClassVar[int]
    FDPPPBPOEMP_FIELD_NUMBER: _ClassVar[int]
    MGDPFNIIFEA: _containers.RepeatedCompositeFieldContainer[_JICKPPDLOHC_pb2.JICKPPDLOHC]
    CNAJAFLIBED: _containers.RepeatedCompositeFieldContainer[_BDKCBBNPJHM_pb2.BDKCBBNPJHM]
    HGBBGLKPLFI: int
    FBCEKPOMNAI: bool
    FDPPPBPOEMP: int
    def __init__(self, MGDPFNIIFEA: _Optional[_Iterable[_Union[_JICKPPDLOHC_pb2.JICKPPDLOHC, _Mapping]]] = ..., CNAJAFLIBED: _Optional[_Iterable[_Union[_BDKCBBNPJHM_pb2.BDKCBBNPJHM, _Mapping]]] = ..., HGBBGLKPLFI: _Optional[int] = ..., FBCEKPOMNAI: bool = ..., FDPPPBPOEMP: _Optional[int] = ...) -> None: ...
