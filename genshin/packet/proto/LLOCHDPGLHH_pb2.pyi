from genshin.packet.proto import MBLGAMKOLNH_pb2 as _MBLGAMKOLNH_pb2
from genshin.packet.proto import PDCHBPPHCIO_pb2 as _PDCHBPPHCIO_pb2
from genshin.packet.proto import KEPEDPMNKMH_pb2 as _KEPEDPMNKMH_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LLOCHDPGLHH(_message.Message):
    __slots__ = ("LEPOCHAIDCI", "LAGHFECAPIM", "EJLJPGFDGDH")
    LEPOCHAIDCI_FIELD_NUMBER: _ClassVar[int]
    LAGHFECAPIM_FIELD_NUMBER: _ClassVar[int]
    EJLJPGFDGDH_FIELD_NUMBER: _ClassVar[int]
    LEPOCHAIDCI: _MBLGAMKOLNH_pb2.MBLGAMKOLNH
    LAGHFECAPIM: _PDCHBPPHCIO_pb2.PDCHBPPHCIO
    EJLJPGFDGDH: _KEPEDPMNKMH_pb2.KEPEDPMNKMH
    def __init__(self, LEPOCHAIDCI: _Optional[_Union[_MBLGAMKOLNH_pb2.MBLGAMKOLNH, _Mapping]] = ..., LAGHFECAPIM: _Optional[_Union[_PDCHBPPHCIO_pb2.PDCHBPPHCIO, _Mapping]] = ..., EJLJPGFDGDH: _Optional[_Union[_KEPEDPMNKMH_pb2.KEPEDPMNKMH, _Mapping]] = ...) -> None: ...
