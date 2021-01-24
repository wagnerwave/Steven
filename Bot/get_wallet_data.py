from binance.client import Client

client = Client('API_KEY', 'SECRET_KEY')

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