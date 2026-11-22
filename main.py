from rates import PLANS

def get_valid_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("0または正の数を入力してください。")
                continue
            return value
        except ValueError:
            print("入力が無効です。数字を入力してください。")


def calculate_monthly_cost(plan_name, elec, gas, **kwargs):
    plans_data = PLANS[plan_name]
    total_cost = plans_data["base_fee"]+ (elec * plans_data["elec_rate"]) + (gas * plans_data["gas_rate"])
    if elec > 0 and gas > 0:
        total_cost = total_cost - plans_data["bundle_discount"]
    total_cost += kwargs.get("ac_surcharge", 0)
    total_cost += kwargs.get("remote_surcharge", 0)
    total_cost -= kwargs.get("eco_discount", 0)
    return total_cost



# Now each question only repeats ITSELF if the user types a letter!
elec_kwh = get_valid_number("月間電力使用量（kWh）を入力してください: ")
gas_m3 = get_valid_number("月間ガス使用量（m³）を入力してください: ")
ac_surcharge = input("エアコンを頻繁に使用しますか？（y／n）: ").strip().lower()
remote_surcharge = input("在宅勤務をしていますか？（y／n）: ").strip().lower()
eco_discount = input("エコサービス／ペーパーレスの請求書を利用していますか？ (y/n): ").strip().lower()

if ac_surcharge == "y":
    ac_surcharge = 1800
else:
    ac_surcharge = 0
if remote_surcharge == "y":
    remote_surcharge = 1200
else:
    remote_surcharge = 0
if eco_discount == "y":
    eco_discount = 500
else:
    eco_discount = 0

results=[]


for plan in PLANS:
    total = round(calculate_monthly_cost(plan, elec_kwh, gas_m3, ac_surcharge=ac_surcharge, remote_surcharge=remote_surcharge , eco_discount= eco_discount))
    results.append({
        "plan": plan,
        "monthly_cost": total,
        "yearly_cost": total * 12
        })

ranked_plans = sorted(results, key=lambda x: x["monthly_cost"])
ranked_plans[0]["plan"] = f"{ranked_plans[0]['plan']} ★"


print("┌─────────────────────────────────────────────────────────────────────────┐")
print(f"│                           電気・ガス料金比較 ")
print("├─────────────────────────────────────────────────────────────────────────┤")
print(f"│{'月間電力使用量(kWh) ':<23}│ {elec_kwh!s:<43}│")
print("├────────────────────────────┼────────────────────────────────────────────┤")
print(f"│{'月間ガス使用量(m³) ':<23}│ {gas_m3!s:<43}│")
print("├────────────────────────────┴────────────────────────────────────────────┤")
print(f"│{'プラン':<26}│{'プランごとの月額料金(¥)':<15}│{'プランごとの年額料金(¥)':<15}│")
print("├────────────────────────────┼──────────────────────┼─────────────────────┤")
for v in ranked_plans:
     print(f"│{v['plan']!s:<28}│¥{v['monthly_cost']!s:<21}│¥{v['yearly_cost']!s:<20}│")
print("└────────────────────────────┴──────────────────────┴─────────────────────┘")

