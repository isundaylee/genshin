from genshin.packet.proto import LIPHHIENHHK_pb2 as _LIPHHIENHHK_pb2
from genshin.packet.proto import IPENCEJBEEB_pb2 as _IPENCEJBEEB_pb2
from genshin.packet.proto import PCLLABLBNGA_pb2 as _PCLLABLBNGA_pb2
from genshin.packet.proto import EHGJONOCFDE_pb2 as _EHGJONOCFDE_pb2
from genshin.packet.proto import FJCOKOHBJIN_pb2 as _FJCOKOHBJIN_pb2
from genshin.packet.proto import CAJFFFBLLKB_pb2 as _CAJFFFBLLKB_pb2
from genshin.packet.proto import LOAACAFCPIF_pb2 as _LOAACAFCPIF_pb2
from genshin.packet.proto import KLEEBOCFJPI_pb2 as _KLEEBOCFJPI_pb2
from genshin.packet.proto import AJPMIIOMCDO_pb2 as _AJPMIIOMCDO_pb2
from genshin.packet.proto import KFPAKMBEGPE_pb2 as _KFPAKMBEGPE_pb2
from genshin.packet.proto import EIMACLGMLLC_pb2 as _EIMACLGMLLC_pb2
from genshin.packet.proto import PJIFOJFADLG_pb2 as _PJIFOJFADLG_pb2
from genshin.packet.proto import NAPNKPIHEBF_pb2 as _NAPNKPIHEBF_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EJLNBCBFOGL(_message.Message):
    __slots__ = ("GFMEKOGIHJN", "BIPADACDOFI", "BIHMCIIFMIG", "KHLGCIFJBCK", "MGDFIJMHGND", "BCKBKIDDFCD", "BFMMHKFPCJB", "EMJHADALPLA", "IGDCOEIOOCG", "ICPMAKBNJNL", "life_state", "ECOCHKAPDAM", "MCINIPFFCCD", "BJDAMEMIGCC", "npc", "gadget", "monster", "avatar", "AGIDBEEINDE")
    GFMEKOGIHJN_FIELD_NUMBER: _ClassVar[int]
    BIPADACDOFI_FIELD_NUMBER: _ClassVar[int]
    BIHMCIIFMIG_FIELD_NUMBER: _ClassVar[int]
    KHLGCIFJBCK_FIELD_NUMBER: _ClassVar[int]
    MGDFIJMHGND_FIELD_NUMBER: _ClassVar[int]
    BCKBKIDDFCD_FIELD_NUMBER: _ClassVar[int]
    BFMMHKFPCJB_FIELD_NUMBER: _ClassVar[int]
    EMJHADALPLA_FIELD_NUMBER: _ClassVar[int]
    IGDCOEIOOCG_FIELD_NUMBER: _ClassVar[int]
    ICPMAKBNJNL_FIELD_NUMBER: _ClassVar[int]
    LIFE_STATE_FIELD_NUMBER: _ClassVar[int]
    ECOCHKAPDAM_FIELD_NUMBER: _ClassVar[int]
    MCINIPFFCCD_FIELD_NUMBER: _ClassVar[int]
    BJDAMEMIGCC_FIELD_NUMBER: _ClassVar[int]
    NPC_FIELD_NUMBER: _ClassVar[int]
    GADGET_FIELD_NUMBER: _ClassVar[int]
    MONSTER_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    AGIDBEEINDE_FIELD_NUMBER: _ClassVar[int]
    GFMEKOGIHJN: _LIPHHIENHHK_pb2.LIPHHIENHHK
    BIPADACDOFI: _containers.RepeatedScalarFieldContainer[str]
    BIHMCIIFMIG: _IPENCEJBEEB_pb2.IPENCEJBEEB
    KHLGCIFJBCK: _containers.RepeatedCompositeFieldContainer[_PCLLABLBNGA_pb2.PCLLABLBNGA]
    MGDFIJMHGND: _containers.RepeatedCompositeFieldContainer[_EHGJONOCFDE_pb2.EHGJONOCFDE]
    BCKBKIDDFCD: _containers.RepeatedCompositeFieldContainer[_FJCOKOHBJIN_pb2.FJCOKOHBJIN]
    BFMMHKFPCJB: str
    EMJHADALPLA: _containers.RepeatedCompositeFieldContainer[_CAJFFFBLLKB_pb2.CAJFFFBLLKB]
    IGDCOEIOOCG: _LOAACAFCPIF_pb2.LOAACAFCPIF
    ICPMAKBNJNL: _containers.RepeatedCompositeFieldContainer[_KLEEBOCFJPI_pb2.KLEEBOCFJPI]
    life_state: int
    ECOCHKAPDAM: int
    MCINIPFFCCD: int
    BJDAMEMIGCC: _AJPMIIOMCDO_pb2.AJPMIIOMCDO
    npc: _KFPAKMBEGPE_pb2.KFPAKMBEGPE
    gadget: _EIMACLGMLLC_pb2.EIMACLGMLLC
    monster: _PJIFOJFADLG_pb2.PJIFOJFADLG
    avatar: _NAPNKPIHEBF_pb2.NAPNKPIHEBF
    AGIDBEEINDE: int
    def __init__(self, GFMEKOGIHJN: _Optional[_Union[_LIPHHIENHHK_pb2.LIPHHIENHHK, _Mapping]] = ..., BIPADACDOFI: _Optional[_Iterable[str]] = ..., BIHMCIIFMIG: _Optional[_Union[_IPENCEJBEEB_pb2.IPENCEJBEEB, _Mapping]] = ..., KHLGCIFJBCK: _Optional[_Iterable[_Union[_PCLLABLBNGA_pb2.PCLLABLBNGA, _Mapping]]] = ..., MGDFIJMHGND: _Optional[_Iterable[_Union[_EHGJONOCFDE_pb2.EHGJONOCFDE, _Mapping]]] = ..., BCKBKIDDFCD: _Optional[_Iterable[_Union[_FJCOKOHBJIN_pb2.FJCOKOHBJIN, _Mapping]]] = ..., BFMMHKFPCJB: _Optional[str] = ..., EMJHADALPLA: _Optional[_Iterable[_Union[_CAJFFFBLLKB_pb2.CAJFFFBLLKB, _Mapping]]] = ..., IGDCOEIOOCG: _Optional[_Union[_LOAACAFCPIF_pb2.LOAACAFCPIF, _Mapping]] = ..., ICPMAKBNJNL: _Optional[_Iterable[_Union[_KLEEBOCFJPI_pb2.KLEEBOCFJPI, _Mapping]]] = ..., life_state: _Optional[int] = ..., ECOCHKAPDAM: _Optional[int] = ..., MCINIPFFCCD: _Optional[int] = ..., BJDAMEMIGCC: _Optional[_Union[_AJPMIIOMCDO_pb2.AJPMIIOMCDO, str]] = ..., npc: _Optional[_Union[_KFPAKMBEGPE_pb2.KFPAKMBEGPE, _Mapping]] = ..., gadget: _Optional[_Union[_EIMACLGMLLC_pb2.EIMACLGMLLC, _Mapping]] = ..., monster: _Optional[_Union[_PJIFOJFADLG_pb2.PJIFOJFADLG, _Mapping]] = ..., avatar: _Optional[_Union[_NAPNKPIHEBF_pb2.NAPNKPIHEBF, _Mapping]] = ..., AGIDBEEINDE: _Optional[int] = ...) -> None: ...
