def calculate_tps(unit_price, deposit_paid):
    principal = unit_price - deposit_paid
    annual_rate = 0.07
    monthly_rate = annual_rate / 12
    months = 25 * 12
    if principal <= 0: return 0
    m = principal * (monthly_rate * (1 + monthly_rate)**months) / ((1 + monthly_rate)**months - 1)
    return round(m, 2)

def get_category(income):
    if income < 20000: return "Social Housing"
    elif income < 50000: return "Low-Cost Housing"
    elif income < 150000: return "Affordable Housing"
    return "Market Rate"
