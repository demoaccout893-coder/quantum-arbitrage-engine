import ccxt

class ExchangeAdapter:
    def __init__(self, exchange_name):
        self.exchange_name = exchange_name
        self.exchange = self._create_exchange()  

    def _create_exchange(self):
        try:
            exchange_class = getattr(ccxt, self.exchange_name)
            return exchange_class()
        except AttributeError:
            raise ValueError(f'Exchange {self.exchange_name} is not supported')

    def fetch_balance(self):
        return self.exchange.fetch_balance() 

    def fetch_ticker(self, symbol):
        return self.exchange.fetch_ticker(symbol) 

    def fetch_trades(self, symbol):
        return self.exchange.fetch_trades(symbol) 

class BinanceAdapter(ExchangeAdapter):
    def __init__(self):
        super().__init__('binance')

class OKXAdapter(ExchangeAdapter):
    def __init__(self):
        super().__init__('okex')

class KrakenAdapter(ExchangeAdapter):
    def __init__(self):
        super().__init__('kraken')

class BybitAdapter(ExchangeAdapter):
    def __init__(self):
        super().__init__('bybit')

class KuCoinAdapter(ExchangeAdapter):
    def __init__(self):
        super().__init__('kucoin')

class GateioAdapter(ExchangeAdapter):
    def __init__(self):
        super().__init__('gateio')
