# Darwin Position Sizer 🧬
A strict mathematical position-sizing utility for spot markets.

Many algorithmic traders fail due to improper risk management rather than bad entry signals. This utility calculates the exact asset quantity to purchase based on a strict percentage-based risk model, invalidation level (stop-loss), and total portfolio size.

### Core Philosophy
* **Capital Preservation First:** Never risk more than the defined threshold (e.g., 1%) of the total portfolio on a single trade.
* **Math over Emotion:** Calculates position size dynamically based on the distance to the stop-loss.
