from scripts.helpful_scripts import fund_with_link, get_account,OPENSEA_URL, get_contract
from brownie import AdvancedCollectible,network,config



def deploy_and_create():
    account = get_account()
    advanced_collectible = AdvancedCollectible.deploy(
        get_contract("vrf_coordinator"),
        get_contract("link_token"),
        config["networks"][network.show_active()]["keyhash"],
        config["networks"][network.show_active()]["fee"],
        {"from":account}
    )
    fund_with_link(advanced_collectible.address)
    createing_tx = advanced_collectible.createCollectible({"from":account})
    createing_tx.wait(1)
    print("New token has been created!!")
    return advanced_collectible,createing_tx

def  main():
    deploy_and_create()
