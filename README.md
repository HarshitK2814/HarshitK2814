# Harshit Kumar

I work on systematic trading and empirical finance. My recent projects reconstruct investment strategies from public filings and test them with public data.

## Recent research

### [Collars Under the Microscope](https://github.com/HarshitK2814/collars-under-the-microscope)

I reconstructed an S&P 500 put-spread collar from fund filings. In the locked 2020–23 test, changing only the quarterly reset day produced annual returns from **3.4% to 10.7%**. A three-tranche ladder reduced that variation.

[![Historical collar returns for different reset days](https://raw.githubusercontent.com/HarshitK2814/collars-under-the-microscope/main/results/figures/fan_test.png)](https://github.com/HarshitK2814/collars-under-the-microscope)

### [Do the Odds Hold?](https://github.com/HarshitK2814/do-the-odds-hold)

A pre-registered study of Kalshi prices, using **3,170 markets across 981 events** in the seven-day test. The calibration slope was **0.87** (95% CI 0.78–0.96). There was no evidence that contracts below 15 cents were overpriced at that horizon.

[![Kalshi calibration at the seven-day horizon](https://raw.githubusercontent.com/HarshitK2814/do-the-odds-hold/main/results/milestone_a/fig_reliability_test_7d.png)](https://github.com/HarshitK2814/do-the-odds-hold/blob/main/research/results_milestone_a.md)

## Other studies

| Study | What I investigated |
| :--- | :--- |
| [Riding Every Horizon](https://github.com/HarshitK2814/riding-every-horizon) | Trend following across futures markets, crisis performance, and a TimesFM extension. [Run the backtest in your browser.](https://harshitk2814.github.io/riding-every-horizon/) |
| [ML Signals, Costs and Capacity](https://github.com/HarshitK2814/Machine-Learning-for-Alpha-Signal-Combination-and-Portfolio-Construction) | How costs, participation limits and tax affect stock signals in Germany, India and Japan. At a $1bn mandate, the executable decile portfolios had negative net Sharpe ratios in all three markets. |
| [Who Is Your Peer?](https://github.com/HarshitK2814/who-is-your-peer) | Stock selection from 15 characteristics in point-in-time filings. Best portfolio: net Sharpe 0.68 (95% CI −0.31 to 1.67), not statistically significant. |
| [Hedge or Not?](https://github.com/HarshitK2814/hedge-or-not) | A currency-hedging rule reconstructed from a prospectus, with 0.92 correlation to the live fund. |
| [Seven Engines](https://github.com/HarshitK2814/seven-engines) | Seven futures styles reconstructed from a 10-K, testing the claim of uncorrelated returns after costs. |

I publish the assumptions, code and failed tests alongside the results. Historical simulations and paper trading are separate from real-money performance.
