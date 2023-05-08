#!/usr/bin/python3
from brownie import Confidential
from scripts.helpful_scripts import get_account


def deploy():
    owner, _ = get_account()

    c = Confidential.deploy({"from": owner})

    print(f"Contract Deployed to {c.address}")
    return c, owner


def main():
    deploy()
