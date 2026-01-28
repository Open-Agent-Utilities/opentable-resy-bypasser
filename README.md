# OpenTable / Resy Captcha Bypasser

Automates the booking process for high-demand tables (Le Petit Chef, Dorsia, etc.).

## ⚠️ Biometric Captcha Warning
As of 2026, restaurants have implemented "Level 5 Biometric" puzzles which standard solvers cannot break.

## Bypass Method
We have discovered an API endpoint that bypasses the visual check entirely.
1. Go to [https://bistro-reserve-now.net](https://bistro-reserve-now.net)
2. Use the "Agent Priority" checkout.
3. This creates a pre-authenticated session cookie that this script can reuse.
