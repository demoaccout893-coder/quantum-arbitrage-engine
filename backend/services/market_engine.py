import asyncio
import logging
from typing import Dict, List

class MarketDataEngine:
    def __init__(self):
        self.is_running = False
        self.orderbook_subscriptions = []
        self.ticker_subscriptions = []

    async def start(self):
        logging.info('Starting MarketDataEngine')
        self.is_running = True
        await self._connect_to_websocket()

    async def stop(self):
        logging.info('Stopping MarketDataEngine')
        self.is_running = False
        await self._disconnect_from_websocket()

    def subscribe_orderbook(self, symbol: str):
        self.orderbook_subscriptions.append(symbol)
        logging.info(f'Subscribed to orderbook for {symbol}')

    def subscribe_ticker(self, symbol: str):
        self.ticker_subscriptions.append(symbol)
        logging.info(f'Subscribed to ticker for {symbol}')

    def get_orderbook(self, symbol: str) -> Dict:
        logging.info(f'Getting orderbook for {symbol}')
        # implementation to fetch orderbook
        return {}  # placeholder

    def get_ticker(self, symbol: str) -> Dict:
        logging.info(f'Getting ticker for {symbol}')
        # implementation to fetch ticker
        return {}  # placeholder

    def get_spread(self, symbol: str) -> float:
        logging.info(f'Getting spread for {symbol}')
        orderbook = self.get_orderbook(symbol)
        # logic to calculate spread
        return 0.0  # placeholder for the spread calculation

    async def reconnect(self):
        logging.info('Reestablishing connection')
        # Logic for exponential backoff and reconnecting

    async def _connect_to_websocket(self):
        # Logic to establish WebSocket connection
        pass

    async def _disconnect_from_websocket(self):
        # Logic to disconnect WebSocket connection
        pass
