import streamlit as st

# إعدادات الصفحة الرسمية للنظام
st.set_page_config(page_title="Prompt OS 3.0", page_icon="🚀", layout="wide")

# العنوان الرئيسي لواجهة النظام
st.title("🚀 Universal Prompt OS 3.0")
st.subheader("المحرك الميتا-مصفوفي الشامل لصناعة الأوامر الفائقة والمنهجيات الابتكارية")
st.write("---")

# ==========================================
# أولاً: قاعدة البيانات الشاملة والأسرار اللغوية (The Core Data Engine)
# ==========================================
MODEL_DATABASE = {
    "Reasoning Models (OpenAI o1/o3, DeepSeek R1)": {
        "tag_style": "Markdown",
        "anchor_trigger": "[OBJECTIVE_FUNCTION: EXACT_BOUNDS]",
        "mitigation_code": "CRITICAL: Disable conversational filler. Enforce mathematical and formal logical boundaries. Validate all negative constraints before state convergence.",
        "description": "تفعيل وضع الاستدلال الرياضي العميق وحظر القفز المنطقي المتسرع."
    },
    "Long-Context Engines (Google Gemini 1.5/2.0, Claude 3.5)": {
        "tag_style": "XML",
        "anchor_trigger": "[ANCHOR_DENSITY: HIGHEST]",
        "mitigation_code": "SYSTEM DIRECTIVE: Maintain absolute semantic adherence throughout the entire text span. Neutralize middle-context attention decay by sequential node tracking.",
        "description": "تثبيت الذاكرة السياقية ومنع هبوط التركيز في وسط البيانات الضخمة."
    },
    "Autonomous AI Agents & Tools (LangChain, CrewAI, Interpreters)": {
        "tag_style": "XML",
        "anchor_trigger": "[AGENT_STATE: STATEFUL_MONITORING]",
        "mitigation_code": "AGENT CONSTRAINT: Print execution state and sub-goal validation parameters before calling any external tool. Prevent iterative logic looping.",
        "description": "فرض الرقابة الذاتية على الوكلاء الذكيين ومنع الحلقات التنفيذية المفرغة."
    }
}

OUTPUT_DATABASE = {
    "Technical/Code (Zero-Prose Deployment)": {
        "instruction": "Enforce a Zero-Prose Output state. Deliver code inside strict, executable, and modular compilation blocks only. No conversational context allowed."
    },
    "Strategic/Analytical Report (High-Density ASCII)": {
        "instruction": "Deploy the 'Chain of Density' semantic protocol. Maximize information concentration per line. Use complex multi-dimensional markdown tables and functional ASCII flowcharts for interdependency mapping."
    },
    "Radical Innovation (First-Principles Breakdown)": {
        "instruction": "Execute an absolute first-principles deconstruction. Discard all standard industry assumptions using hard negative constraints. Rely on analogical prompting from non-adjacent industries."
    }
}

# ==========================================
# ثانياً: واجهة المستخدم وديناميكية الاختيار
# ==========================================
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🎯 1. مدخلات ومعطيات الطلب الأساسية")
    user_request = st.text_area("أدخل طلبك الخام هنا (ما هي المهمة التي تريد إنجازها؟):", 
                                placeholder="مثال: تحليل المخاطر المترتبة على أتمتة سلاسل الإمداد بالذكاء الاصطناعي...")
    
    constraints_input = st.text_area("الشروط والمحرمات الصارمة (القيود):", 
                                     placeholder="مثال: عدم تقديم حلول تقليدية، الالتزام التام بقوانين الشحن الدولية الجديدة...")

with col2:
    st.markdown("### 🎛️ 2. هندسة التكيف والمعمارية المستقبلة")
    target_receiver = st.selectbox("اختر نوع المستقبل للأمر (Target Receiver):", list(MODEL_DATABASE.keys()))
    product_format = st.selectbox("اختر شكل المنتج النهائي المطلوب (Output Format):", list(OUTPUT_DATABASE.keys()))
    
    st.info(f"**تأثير التكيف الحركي**: {MODEL_DATABASE[target_receiver]['description']}")

st.write("---")

# ==========================================
# ثالثاً: بروتوكول تجميع النسيج (The Fabric Compilation)
# ==========================================
if st.button("🔥 توليد الأمر الخارق (Compile Super Prompt)"):
    if not user_request:
        st.error("رجاءً أدخل الطلب الأساسي أولاً لتفعيل المحرك.")
    else:
        # سحب البيانات المناسبة من قاعدة المعطيات بناءً على الاختيارات
        model_meta = MODEL_DATABASE[target_receiver]
        output_meta = OUTPUT_DATABASE[product_format]
        
        # صياغة حلقة التحقق الذاتي وعزل الهلوسة الصارمة
        verification_string = """
1. Generate a latent factual validation array in memory.
2. Cross-examine all claims against the provided data feed.
3. If data is insufficient for absolute certainty, print [INSUFFICIENT_DATA_ERROR] instead of guessing.
4. Correct all semantic anomalies before printing the final response.
"""

        # بناء الأمر النهائي بناءً على المدرسة الهيكلية المفروضة (XML أو Markdown)
        if model_meta["tag_style"] == "XML":
            final_prompt = f"""**[SYSTEM OPERATION COMMAND: UNIVERSAL METAMORPHIC PROMPT v3.0]**
**{model_meta['anchor_trigger']}**
**[COMPILING_STATE: SYSTEM_RESOLVED]**

{model_meta['mitigation_code']}

<system_directive>
You are executing at the absolute threshold of elite AI systems architecture. Adopt the appropriate domain expertise to full capacity.
</system_directive>

<isolated_instruction>
Objective Action: {user_request}
Format Execution Policy: {output_meta['instruction']}
</isolated_instruction>

<immutable_constraints>
{constraints_input if constraints_input else "No deviations from first-principles reasoning allowed."}
</immutable_constraints>

<dynamic_data_feed>
[Insert Raw Data / Documents Here if applicable. If not, rely strictly on grounded parametric memory.]
</dynamic_data_feed>

<verification_matrix>
{verification_string}
</verification_matrix>

**EXECUTION:** Initialize high-density processing flow now. Output result based on your operational constraints.
"""
        else:
            final_prompt = f"""# SYSTEM OPERATION COMMAND: UNIVERSAL METAMORPHIC PROMPT v3.0
**{model_meta['anchor_trigger']}**
**COMPILING_STATE: SYSTEM_RESOLVED**

{model_meta['mitigation_code']}

## 1. System Directive
You are executing at the absolute threshold of elite AI systems architecture. Adopt the appropriate domain expertise to full capacity.

## 2. Isolated Instruction
* **Objective Action:** {user_request}
* **Format Execution Policy:** {output_meta['instruction']}

## 3. Immutable Constraints
{constraints_input if constraints_input else "No deviations from first-principles reasoning allowed."}

## 4. Verification Matrix
{verification_string}

**EXECUTION:** Initialize high-density processing flow now. Output result based on your operational constraints.
"""

        # عرض النتيجة النهائية للمستخد جاهزة للنسخ والمحاكاة المباشرة
        st.success("🎉 تم تجميع وتشييد الأمر الاحترافي الخارق بنجاح!")
        st.caption("انسخ الكود أدناه وضعه في أي نموذج أو أداة أو وكيل ذكاء اصطناعي لتشهد الطفرة في المخرجات:")
        st.code(final_prompt, language="markdown")
