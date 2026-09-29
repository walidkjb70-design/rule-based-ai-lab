# main.py
# الملف الرئيسي لتشغيل المختبر الهجين وربط القواعد بالتدقيق

# 1. استيراد القواعد والدوال التي صنعناها مسبقاً
from math_rules import calculate_ratio
from validator_rules import enforce_strict_bounds

def run_hybrid_system():
    print("--- بدء تشغيل النظام الهجين والتحقق من القواعد ---")
    
    # تجربة حساب نسبة معينة
    part = 25.0
    total = 100.0
    ratio = calculate_ratio(part, total)
    print(f"النسبة المحسوبة: {ratio}%")
    
    # استخدام وحدة التدقيق للتأكد أن النسبة آمنة وصارمة
    safe_value = enforce_strict_bounds(ratio, 0.0, 100.0)
    print(f"تم اعتماد القيمة بنجاح عبر حارس الحدود: {safe_value}")

if __name__ == "__main__":
    run_hybrid_system()
