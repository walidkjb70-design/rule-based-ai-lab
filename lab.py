# lab.py
# الآلة الحاسبة التفاعلية للنظام الهجين مع التحذيرات والتسجيل الدائم

from math_rules import calculate_ratio, safe_divide
from validator_rules import enforce_strict_bounds

def run_interactive_calculator():
    print("--- مرحباً بك في الآلة الحاسبة الذكية للنظام الهجين ---")
    
    audit_history = []
    
    # حلقة تكرارية لتسمح لك بإدخال عدة عمليات
    while True:
        user_input = input("\nهل تريد إجراء عملية حسابية جديدة؟ (اكتب 'نعم' أو 'خروج'): ")
        
        if user_input.strip() != "نعم":
            print("شكراً لاستخدام الآلة الحاسبة. جاري حفظ السجل وإغلاق النظام...")
            break
            
        try:
            # استقبال الأرقام منك مباشرة
            part = float(input("أدخل الجزء (الرقم الأول): "))
            total = float(input("أدخل الكل (الرقم الكلي): "))
            
            # تنفيذ القواعد الرياضية والتحقق
            ratio = calculate_ratio(part, total)
            safe_val = enforce_strict_bounds(ratio, 0.0, 100.0)
            
            # تسجيل العملية الأساسية
            result_msg = f"العملية: الجزء={part}, الكل={total} ➔ النسبة هي {safe_val}%"
            audit_history.append(result_msg)
            print(result_msg)
            
            # اتخاذ قرار ذكي بناءً على النتيجة
            if safe_val > 80.0:
                warning_msg = f"⚠️ تحذير ذكي: النسبة ({safe_val}%) مرتفعة وتتجاوز الحد الموصى به (80%)!"
                audit_history.append(warning_msg)
                print(warning_msg)
            else:
                normal_msg = f"✅ الحالة: النسبة ({safe_val}%) ضمن النطاق الآمن تماماً."
                audit_history.append(normal_msg)
                print(normal_msg)
                
        except ValueError:
            print("❌ خطأ: يرجى إدخال أرقام صحيحة فقط.")
            audit_history.append("⚠️ خطأ في الإدخال: أدخل المستخدم قيماً غير صالحة.")

    # حفظ السجل بالكامل في ملف نصي عند الخروج
    if audit_history:
        log_filename = "audit_log.txt"
        with open(log_filename, "w", encoding="utf-8") as log_file:
            log_file.write("=== سجل التدقيق والتحذيرات للآلة الحاسبة الذكية ===\n")
            for record in audit_history:
                log_file.write(record + "\n")
        
        print(f"\n--- تم حفظ جميع العمليات بنجاح في الملف: {log_filename} ---")

if __name__ == "__main__":
    run_interactive_calculator()

