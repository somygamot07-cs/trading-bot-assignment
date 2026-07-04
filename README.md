# Binance Futures Testnet Trading Bot

## Features

- Market Orders
- Limit Orders
- BUY and SELL Support
- Input Validation
- Logging
- Error Handling
- CLI Interface

## Installation

```bash
pip install -r requirements.txt
```

## Setup

Create .env file

```env
API_KEY=your_api_key
API_SECRET=your_api_secret
```

## Market Order Example

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

## Limit Order Example

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000
```