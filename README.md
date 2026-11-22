# ⚡ 家庭用電気・ガス料金プラン比較シミュレーター (CLI Energy Plan Simulator)

月間の電力使用量（kWh）・ガス使用量（m³）およびライフスタイル条件（在宅勤務・エアコン使用・エコ割引）を入力することで、複数の料金プランの月額・年額コストを自動試算し、最安プランを提案するCLIツールです。

A Python CLI tool that calculates and ranks monthly and annual electricity/gas utility plans based on household usage and lifestyle modifiers.

---

## 🛠 使用技術 / Tech Stack
- **Language:** Python 3.x (Standard Library only — zero external dependencies)
- **Key Concepts Used:**
  - Modular data modeling with nested dictionaries (`rates.py`)
  - Input validation loops (`while True` + `try / except ValueError`)
  - Flexible surcharge/discount calculation using `**kwargs`
  - Numeric sorting & ranking with `sorted()` and `lambda` functions

---

## 🚀 実行方法 / How to Run

1. リポジトリをクローン / Clone the repository:
   ```bash
   git clone https://github.com/Romamatsu/energy-plan-simulator.git
   cd energy-plan-simulator
   ```

2. アプリを実行 / Run the simulator:
   ```bash
   python3 main.py
   ```

---

## 💡 UI/UXの工夫 / Design Highlights
UI/UXデザイナーとしての経験を活かし、コマンドライン上でもユーザーが最安プランと節約額を直感的に比較できるよう、視認性の高いテーブルレイアウトと `★` による最安プランの強調表示を実装しました。

---

## 🔮 今後の展望 / Next Steps
- **Webアプリ化:** Django / TypeScript を用いたWebブラウザ版UIの構築
- **クラウドデプロイ:** AWS（EC2 / Lambda / RDS）を活用したクラウド環境への展開
