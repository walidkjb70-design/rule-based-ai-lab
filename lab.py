# lab.py
# الملف الرئيسي لتشغيل المختبر الهجين، ربط القواعد، والاحتفاظ بسجل العمليات

from math_rules import calculate_ratio, safe_divide
from validator_rules import enforce_strict_bounds

def run_hybrid_system():
    print("--- بدء تشغيل النظام الهجين والتحقق من القواعد ---")
    
    # قائمة فارغة لتخزين سجل النتائج (الذاكرة المؤقتة للمختبر)
    audit_history = []
    
    # تجربة العملية الأولى
    part1, total1 = 25.0, 100.0
    ratio1 = calculate_ratio(part1, total1)
    safe_val1 = enforce_strict_bounds(ratio1, 0.0, 100.0)
    
    # حفظ النتيجة في سجل العمليات
    audit_history.append(f"العملية 1: النسبة الآمنة هي {safe_val1}%")
    
    # تجربة العملية الثانية
    part2, total2 = 45.0, 50.0
    ratio2 = calculate_ratio(part2, total2)
    safe_val2 = enforce_strict_bounds(ratio2, 0.0, 200.0) # توسيع النطاق مؤقتاً للتدقيق
    
    # حفظ النتيجة في سجل العمليات
    audit_history.append(f"العملية 2: النسبة الآمنة هي {safe_val2}%")
    
    print("\n--- سجل الذاكرة المؤقتة (Audit History) ---")
    for record in audit_history:
        print(record)
    
    print("--- تم الانتهاء من دورة العمل بنجاح ---")

if __name__ == "__main__":
    run_hybrid_system()
 
