# lab.py
# الملف الرئيسي لتشغيل المختبر الهجين، مع ميزة التحذيرات والحفظ الدائم في ملف نصي

from math_rules import calculate_ratio, safe_divide
from validator_rules import enforce_strict_bounds

def run_hybrid_system():
    print("--- بدء تشغيل النظام الهجين والتحقق من القواعد ---")
    
    # الذاكرة المؤقتة لتخزين العمليات والتحذيرات
    audit_history = []
    
    # قائمة بيانات للتجربة (أزواج من الأرقام)
    test_data = [
        (25.0, 100.0),  # نسبة طبيعية (25%)
        (85.0, 100.0),  # نسبة عالية تحتاج تنبيه (85%)
        (45.0, 50.0)    # نسبة جيدة (90%)
    ]
    
    for i, (part, total) in enumerate(test_data, 1):
        ratio = calculate_ratio(part, total)
        safe_val = enforce_strict_bounds(ratio, 0.0, 100.0)
        
        # تسجيل العملية الأساسية
        result_msg = f"العملية {i}: النسبة هي {safe_val}%"
        audit_history.append(result_msg)
        
        # اتخاذ قرار ذكي بناءً على النتيجة
        if safe_val > 80.0:
            warning_msg = f"⚠️ تحذير ذكي (العملية {i}): النسبة مرتفعة وتتجاوز الحد الموصى به (80%)!"
            audit_history.append(warning_msg)
        else:
            normal_msg = f"✅ الحالة (العملية {i}): ضمن النطاق الآمن تماماً."
            audit_history.append(normal_msg)

    print("\n--- طباعة السجل على الشاشة ---")
    for record in audit_history:
        print(record)

    # حفظ السجل بشكل دائم في ملف نصي (Audit Log File)
    log_filename = "audit_log.txt"
    with open(log_filename, "w", encoding="utf-8") as log_file:
        log_file.write("=== سجل التدقيق والتحذيرات للنظام الهجين ===\n")
        for record in audit_history:
            log_file.write(record + "\n")
    
    print(f"\n--- تم بنجاح حفظ السجل بالكامل في الملف: {log_filename} ---")

if __name__ == "__main__":
    run_hybrid_system()
 
