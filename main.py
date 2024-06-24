name: weixin

on:
  workflow_dispatch:
  schedule:
    # 代表国际标准时间4点0分，北京时间需要+8小时，代表北京时间中午12点运行
    - cron: '0 23 * * *'

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Set up Python 3.8
        uses: actions/setup-python@v5
        with:
          python-version: '3.8'
      
      - name: Install pip packages
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      
      - name: Run weixin script
        run: |
          python main.py
