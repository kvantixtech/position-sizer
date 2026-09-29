> **Archived, September 2026.** A small utility written in March 2026, when Kvantix was building a crypto trading engine. That engine did not pass our own statistical tests: [the reports](https://github.com/kvantixtech/kvantix-reports) are published unedited. This code is kept for reference only. It is not part of any Kvantix product, is not maintained, and claims no trading edge.
>
> Kvantix now validates trading signals and forecasts independently: [kvantix.tech](https://kvantix.tech) · [github.com/kvantixtech](https://github.com/kvantixtech)

# Darwin Position Sizer 🧬
A strict mathematical position-sizing utility for spot markets.

Many algorithmic traders fail due to improper risk management rather than bad entry signals. This utility calculates the exact asset quantity to purchase based on a strict percentage-based risk model, invalidation level (stop-loss), and total portfolio size.

### Core Philosophy
* **Capital Preservation First:** Never risk more than the defined threshold (e.g., 1%) of the total portfolio on a single trade.
* **Math over Emotion:** Calculates position size dynamically based on the distance to the stop-loss.
