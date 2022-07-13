from dataclasses import dataclass
from enum import Enum
from typing import Dict

from hivemind import PeerID

ModuleUID = str
UID_DELIMITER = "."  # delimits parts of one module uid, e.g. "bloom.transformer.h.4.self_attention"
CHAIN_DELIMITER = " "  # delimits multiple uids in a sequence, e.g. "bloom.layer3 bloom.layer4"


class ServerState(Enum):
    OFFLINE = 0
    JOINING = 1
    ONLINE = 2


@dataclass
class ServerInfo:
    state: ServerState
    throughput: float


@dataclass
class RemoteModuleInfo:
    uid: ModuleUID
    servers: Dict[PeerID, ServerInfo]