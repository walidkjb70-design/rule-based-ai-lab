# validator_rules.py
# وحدة التدقيق الصارم والتحقق من النطاقات لضمان عدم وجود انحراف منطقي

def validate_percentage_range(value: float) -> bool:
    """التحقق من أن النسبة تقع بدقة بين 0% و 100%"""
    return 0.0 <= value <= 100.0

def enforce_strict_bounds(value: float, min_val: float, max_val: float) -> float:
    """إجبار القيمة على البقاء ضمن الحد الآمن، أو إطلاق خطأ هندسي إذا تجاوزته"""
    if not (min_val <= value <= max_val):
        raise ValueError(f"قيمة غير مسموح بها ({value}): خارج النطاق الصارم بين {min_val} و {max_val}.")
    return value
