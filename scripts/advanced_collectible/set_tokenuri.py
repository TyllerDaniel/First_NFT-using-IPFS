from brownie import network,AdvancedCollectible
from scripts.helpful_scripts import OPENSEA_URL, get_breed,get_account


def main():
    print(f"Working on {network.show_active()}")
    advanced_collectible = AdvancedCollectible[-1]
    number_of_collectibles = advanced_collectible.tokenCounter()
    print(f"You have{number_of_collectibles} tokenIds")
    for token_id in range (number_of_collectibles):
        breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
        if not advanced_collectible.tokenURI(token_id).startswith("https://"):
            print(f"Setting Token URI of{token_id}")
            set_tokenURI(token_id,advanced_collectible,breed)

def set_tokenURI(token_id,nft_contract,tokenURI):
    account = get_account()
    tx = nft_contract.setTokenURI(token_id,tokenURI,{"from":account})
    tx.wait(1)
    print(f"Awesome! You can view your NFT at {OPENSEA_URL.format(nft_contract.address,token_id)}")
    print("Please wait upto 20 minutes then refresh")