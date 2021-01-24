from binance.client import Client
import get_wallet_data

client = Client('API_KEY', 'SECRET_KEY')
risk_lvls = {'low' : 10, 'medium' : 25, 'high' : 50, 'fool' : 75} # donner le choix en parametre lors du lancement du programme ?

def compute_investment(currency, risk):
    currency_stock = client.get_asset_balance(asset=currency)
    invest = currency_stock * risk / 100
    return invest
    