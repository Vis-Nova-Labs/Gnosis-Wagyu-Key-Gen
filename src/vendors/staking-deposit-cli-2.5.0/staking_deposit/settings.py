from typing import Dict, NamedTuple
from eth_utils import decode_hex

DEPOSIT_CLI_VERSION = '2.5.0'


class BaseChainSetting(NamedTuple):
    NETWORK_NAME: str
    GENESIS_FORK_VERSION: bytes
    GENESIS_VALIDATORS_ROOT: bytes


#MAINNET = 'mainnet'
#GOERLI = 'goerli'
#PRATER = 'prater'
#SEPOLIA = 'sepolia'
#ZHEJIANG = 'zhejiang'
GNOSIS = 'gnosis'
CHIADO = 'chiado'


# Mainnet settings
#MainnetSetting = BaseChainSetting(
#    NETWORK_NAME=MAINNET, GENESIS_FORK_VERSION=bytes.fromhex('00000000'),
#    GENESIS_VALIDATORS_ROOT=bytes.fromhex('4b363db94e286120d76eb905340fdd4e54bfe9f06bf33ff6cf5ad27f511bfe95'))
# Goerli settings
#GoerliSetting = BaseChainSetting(
#    NETWORK_NAME=GOERLI, GENESIS_FORK_VERSION=bytes.fromhex('00001020'),
#    GENESIS_VALIDATORS_ROOT=bytes.fromhex('043db0d9a83813551ee2f33450d23797757d430911a9320530ad8a0eabc43efb'))
# Sepolia settings
#SepoliaSetting = BaseChainSetting(
#    NETWORK_NAME=SEPOLIA, GENESIS_FORK_VERSION=bytes.fromhex('90000069'),
#    GENESIS_VALIDATORS_ROOT=bytes.fromhex('d8ea171f3c94aea21ebc42a1ed61052acf3f9209c00e4efbaaddac09ed9b8078'))
# Zhejiang settings
#ZhejiangSetting = BaseChainSetting(
#    NETWORK_NAME=ZHEJIANG, GENESIS_FORK_VERSION=bytes.fromhex('00000069'),
#    GENESIS_VALIDATORS_ROOT=bytes.fromhex('53a92d8f2bb1d85f62d16a156e6ebcd1bcaba652d0900b2c2f387826f3481f6f'))
###############################################################################################################
# Gnosis settings
GnosisSetting = BaseChainSetting(
    NETWORK_NAME=GNOSIS, GENESIS_FORK_VERSION=bytes.fromhex('00000064'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('f5dcb5564e829aab27264b9becd5dfaa017085611224cb3036f573368dbb9d47'))
#Chiado settings
ChiadoSetting = BaseChainSetting(
    NETWORK_NAME=CHIADO, GENESIS_FORK_VERSION=bytes.fromhex('0000006f'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('9d642dac73058fbf39c0ae41ab1e34e4d889043cb199851ded7095bc99eb4c1e'))


ALL_CHAINS: Dict[str, BaseChainSetting] = {
    GNOSIS: GnosisSetting,
    CHIADO: ChiadoSetting,
    #MAINNET: MainnetSetting,
    #GOERLI: GoerliSetting,
    #PRATER: GoerliSetting,  # Prater is the old name of the Prater/Goerli testnet
    #SEPOLIA: SepoliaSetting,
    #ZHEJIANG: ZhejiangSetting,
}


def get_chain_setting(chain_name: str = GNOSIS) -> BaseChainSetting:
    return ALL_CHAINS[chain_name]


def get_devnet_chain_setting(network_name: str,
                             genesis_fork_version: str,
                             genesis_validator_root: str) -> BaseChainSetting:
    return BaseChainSetting(
        NETWORK_NAME=network_name,
        GENESIS_FORK_VERSION=decode_hex(genesis_fork_version),
        GENESIS_VALIDATORS_ROOT=decode_hex(genesis_validator_root),
    )
