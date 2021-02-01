# Steven
Steven my trading assistant.

For deploy the environnment : 
```
docker-compose up --build
```
# Usage
```
python3 main.py [Period] [Symbol] [Quantity]

Exemple : python3 main.py short BTC 0.001

Period : Short - Medium - Long
         Short : 1 hour
         Medium : 1 week
         Long : 1 mouth

Symbol : BTC - ETH - XMR
         BTC : Bitcoin
         ETH : Etherium 
         XMR : Monero

Quatity : the quantities of money for your trading bot
          Exemple : 0.650
```
