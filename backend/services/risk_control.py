class RiskController:
    def __init__(self, max_daily_loss: float, max_exposure_per_exchange: float, max_open_trades: int):
        self.max_daily_loss = max_daily_loss
        self.max_exposure_per_exchange = max_exposure_per_exchange
        self.max_open_trades = max_open_trades
        self.current_daily_loss = 0.0
        self.open_trades = 0
        self.kill_switch = False

    def validate_trade(self, trade_amount: float, exchange: str) -> bool:
        if self.kill_switch:
            raise Exception("Kill switch activated. Trading is disabled.")
        if trade_amount < 0:
            raise ValueError("Trade amount must be positive.")
        if self.open_trades >= self.max_open_trades:
            raise Exception("Maximum open trades limit reached.")
        if trade_amount > self.max_exposure_per_exchange:
            raise Exception("Trade amount exceeds maximum exposure per exchange.")
        return True

    def record_trade(self, trade_amount: float):
        if self.validate_trade(trade_amount, exchange="any"):
            self.open_trades += 1
            # hypothetical function to log the trade and update losses
            self.update_daily_loss(trade_amount)

    def update_daily_loss(self, amount: float):
        self.current_daily_loss += amount
        if self.current_daily_loss > self.max_daily_loss:
            self.activate_kill_switch()

    def activate_kill_switch(self):
        self.kill_switch = True
        print("Kill switch activated due to exceeding max daily loss.")

    def reset(self):
        self.current_daily_loss = 0.0
        self.open_trades = 0
        self.kill_switch = False
