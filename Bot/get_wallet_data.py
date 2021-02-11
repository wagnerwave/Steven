from binance.client import Client
from config import API_KEY, API_SECRET_KEY

client = Client(API_KEY, API_SECRET_KEY)

def getWalletBTC():
    BTC = client.get_asset_balance(asset='BTC')
    print(BTC)

def getWalletETH():
    ETH = client.get_asset_balance(asset='ETH')
    print(ETH)

def getWalletUSDC():
    USDC = client.get_asset_balance(asset='USDC')
    print(USDC)

def getWalletXMR():
    XMR = client.get_asset_balance(asset='XMR')
    print(XMR)

def getAllWallet():
    getWalletBTC()
    getWalletETH()
    getWalletUSDC()
    getWalletXMR()

if __name__ == "__main__":
    getAllWallet()