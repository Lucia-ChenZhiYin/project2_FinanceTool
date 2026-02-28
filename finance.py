# 複利計算小工具
print("--- 歡迎使用北科資財複利計算機 ---")

# 1. 取得使用者輸入
principal = float(input("請輸入本金 (元): "))
rate = float(input("請輸入年利率 (%): "))
years = int(input("請輸入投資年數 (年): "))

# 2. 計算複利公式： 本金 * (1 + 利率)^年數
# Python 裡的次方是 **
final_amount = principal * (1 + (rate / 100)) ** years

# 3. 顯示結果
print("-" * 30)
print(f"{years} 年後，你的錢會變成: {round(final_amount)} 元")