class DarwinRiskManager:
    def __init__(self, account_balance, risk_percentage=1.0):
        """
        Initialize the risk manager.
        :param account_balance: Total capital in base currency (e.g., USDT).
        :param risk_percentage: Max percentage of account to risk per trade (1.0 = 1%).
        """
        self.account_balance = account_balance
        self.risk_percentage = risk_percentage / 100.0

    def calculate_position(self, entry_price, stop_loss_price):
        """
        Calculates the exact position size to ensure the maximum loss 
        does not exceed the defined risk percentage.
        """
        if entry_price <= stop_loss_price:
            raise ValueError("[ERROR] Stop loss must be below entry price for long positions.")

        # Calculate absolute risk per coin
        risk_per_coin = entry_price - stop_loss_price
        
        # Calculate maximum allowed monetary loss
        max_monetary_loss = self.account_balance * self.risk_percentage
        
        # Calculate position size (Quantity to buy)
        position_size = max_monetary_loss / risk_per_coin
        
        # Calculate total capital required for the trade
        capital_required = position_size * entry_price

        return {
            "max_loss_amount": round(max_monetary_loss, 2),
            "position_size": round(position_size, 4),
            "capital_required": round(capital_required, 2)
        }

if __name__ == "__main__":
    # Example Scenario: $10,000 account, risking 1% per trade.
    # Buying BTC at $65,000, Stop Loss at $62,000.
    
    risk_manager = DarwinRiskManager(account_balance=10000, risk_percentage=1.0)
    
    try:
        trade_plan = risk_manager.calculate_position(entry_price=65000, stop_loss_price=62000)
        
        print("=== Darwin Trade Execution Plan ===")
        print(f"Max Allowed Risk: ${trade_plan['max_loss_amount']}")
        print(f"Asset Quantity to Buy: {trade_plan['position_size']} BTC")
        print(f"Total Capital Allocated: ${trade_plan['capital_required']}")
        
    except ValueError as e:
        print(e)
