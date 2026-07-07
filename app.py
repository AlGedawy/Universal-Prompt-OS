import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="PROMPT_OS // v3.0", 
    page_icon="⚡", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# 2. High-Contrast Enterprise Light CSS Injection
st.markdown("""
<style>
    @import url('https://googleapis.com');
    
    /* Global Background & Typography Reset */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #F8FAFC !important;
        font-family: 'Inter', sans-serif !important;
        color: #0F172A !important;
    }
    
    /* Clean, Professional Minimalist Title */
    .brand-title {
        font-family: 'Inter', sans-serif;
        font-size: 2rem;
        font-weight: 700;
        color: #0F172A;
        letter-spacing: -0.5px;
        margin-bottom: 2px;
    }
    .brand-subtitle {
        font-family: 'JetBrains Mono', monospace;
        color: #64748B;
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-bottom: 25px;
    }
    
    /* Structured White Layout Cards with Soft Shadow */
    div[data-testid="stVerticalBlock"] > div {
        background: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 8px !important;
        padding: 20px !important;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05) !important;
    }
    
    /* High-Contrast Inputs (Dark Charcoal Text on Pure White Background) */
    .stTextArea textarea {
        background-color: #FFFFFF !important;
        border: 1px solid #CBD5E1 !important;
        color: #0F172A !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 0.9rem !important;
        border-radius: 6px !important;
    }
    .stTextArea textarea:focus {
        border-color: #0284C7 !important;
        box-shadow: 0 0 0 2px rgba(2, 132, 199, 0.1) !important;
    }
    
    /* High-Contrast Selectbox */
    .stSelectbox div[data-baseweb="select"] {
        background-color: #FFFFFF !important;
        border: 1px solid #CBD5E1 !important;
        color: #0F172A !important;
        font-size: 0.9rem !important;
        border-radius: 6px !important;
    }
    
    /* Labels Styling (Smaller & Crisper) */
    label p {
        font-size: 0.85rem !important;
        font-weight: 600 !important;
        color: #334155 !important;
    }
    
    /* Professional Steel Blue Telemetry Box */
    .status-box {
        background: #F1F5F9 !important;
        border-left: 4px solid #475569 !important;
        padding: 12px !important;
        border-radius: 4px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.8rem;
        color: #334155;
    }
    
    /* Solid Corporate Action Button */
    .stButton>button {
        background: #0F172A !important;
        color: #FFFFFF !important;
        border: none !important;
        padding: 12px 24px !important;
        font-size: 0.9rem !important;
        font-weight: 500 !important;
        font-family: 'JetBrains Mono', monospace !important;
        border-radius: 6px !important;
        width: 100% !important;
        letter-spacing: 0.5px;
        transition: background 0.2s ease !important;
    }
    .stButton>button:hover {
        background: #1E293B !important;
    }
    
    /* Clean Code Block Styling */
    code, pre {
        background-color: #0F172A !important;
        color: #F8FAFC !important;
        border: none !important;
        border-radius: 6px !important;
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 0.85rem !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Branding Header
st.markdown('<h1 class="brand-title">Prompt_OS // Core</h1>', unsafe_allow_html=True)
st.markdown('<p class="brand-subtitle">Universal Latent Space Compiler v3.0</p>', unsafe_allow_html=True)

# ==========================================
# CORE DATA ENGINE (The Knowledge Database)
# ==========================================
MODEL_DATABASE = {
    "Deep Reasoning Engines (OpenAI o1/o3, DeepSeek R1)": {
        "tag_style": "Markdown",
        "anchor_trigger": "[OBJECTIVE_FUNCTION: EXACT_BOUNDS]",
        "mitigation_code": "CRITICAL: Disable conversational filler. Enforce mathematical and formal logical boundaries. Validate all negative constraints before state convergence.",
        "telemetry": "Telemetry: Deep Cognitive Latent Search Engaged. Manual CoT Suppressed."
    },
    "Long-Context Architectures (Google Gemini 1.5/2.0, Claude 3.5 Sonnet)": {
        "tag_style": "XML",
        "anchor_trigger": "[ANCHOR_DENSITY: HIGHEST]",
        "mitigation_code": "SYSTEM DIRECTIVE: Maintain absolute semantic adherence throughout the entire text span. Neutralize middle-context attention decay by sequential node tracking.",
        "telemetry": "Telemetry: Context Optimization Deployed. Attention Anchor Pins Matrix Active."
    },
    "Autonomous AI Agents & Execution Tools (LangChain, CrewAI, Terminal Exec)": {
        "tag_style": "XML",
        "anchor_trigger": "[AGENT_STATE: STATEFUL_MONITORING]",
        "mitigation_code": "AGENT CONSTRAINT: Print execution state and sub-goal validation parameters before calling any external tool. Prevent iterative logic looping.",
        "telemetry": "Telemetry: Stateful Loop Prevention Active. Tool Execution Boundaries Enforced."
    }
}

OUTPUT_DATABASE = {
    "Technical/Code (Zero-Prose Deployment)": {
        "instruction": "Enforce a Zero-Prose Output state. Deliver code inside strict, executable, and modular compilation blocks only. No conversational context allowed."
    },
    "Strategic/Analytical Report (High-Density ASCII Maps)": {
        "instruction": "Deploy the 'Chain of Density' semantic protocol. Maximize information concentration per line. Use complex multi-dimensional markdown tables and functional ASCII flowcharts for interdependency mapping."
    },
    "Radical Innovation (First-Principles Breakdown)": {
        "instruction": "Execute an absolute first-principles deconstruction. Discard all standard industry assumptions using hard negative constraints. Rely on analogical prompting from non-adjacent industries."
    }
}

# ==========================================
# USER INTERFACE LAYOUT
# ==========================================
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("### 📥 1. Core Objectives")
    user_request = st.text_area(
        "Objective Specification (The Raw Request):", 
        height=120,
        placeholder="Type your primary task objective here..."
    )
    
    constraints_input = st.text_area(
        "Immutable Boundaries (Hard Negative Constraints):", 
        height=100,
        placeholder="Type explicit restrictions or rules to enforce..."
    )

with col2:
    st.markdown("### 🎛️ 2. Architectural Tuning")
    target_receiver = st.selectbox("Target Receiver Architecture:", list(MODEL_DATABASE.keys()))
    product_format = st.selectbox("Target Output Format Matrix:", list(OUTPUT_DATABASE.keys()))
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="status-box">
        <strong>SYSTEM LOG:</strong> {MODEL_DATABASE[target_receiver]['telemetry']}
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# COMPILATION PROTOCOL
# ==========================================
if st.button("⚡ EXECUTE SYSTEM COMPILATION"):
    if not user_request:
        st.error("Error: Missing Objective Specification.")
    else:
        model_meta = MODEL_DATABASE[target_receiver]
        output_meta = OUTPUT_DATABASE[product_format]
        
        verification_string = (
            "1. Generate a latent factual validation array in memory.\n"
            "2. Cross-examine all claims against the provided data feed.\n"
            "3. If data is insufficient for absolute certainty, print [INSUFFICIENT_DATA_ERROR].\n"
            "4. Correct all semantic anomalies before printing the final response."
        )

        bounds = constraints_input if constraints_input else "No deviations from first-principles reasoning allowed."

        xml_template = """**[SYSTEM OPERATION COMMAND: UNIVERSAL METAMORPHIC PROMPT v3.0]**
**{TRIGGER}**
**[COMPILING_STATE: SYSTEM_RESOLVED]**

{MITIGATION}

<system_directive>
You are executing at the absolute threshold of elite AI systems architecture. Adopt the appropriate domain expertise to full capacity.
</system_directive>

<isolated_instruction>
Objective Action: {REQUEST}
Format Execution Policy: {POLICY}
</isolated_instruction>

<immutable_constraints>
{BOUNDS}
</immutable_constraints>

<dynamic_data_feed>
[Insert Raw Data / Documents Here if applicable. If not, rely strictly on grounded parametric memory.]
</dynamic_data_feed>

<verification_matrix>
{VERIFICATION}
</verification_matrix>

**EXECUTION:** Initialize high-density processing flow now. Output result based on your operational constraints."""

        markdown_template = """# SYSTEM OPERATION COMMAND: UNIVERSAL METAMORPHIC PROMPT v3.0
**{TRIGGER}**
**COMPILING_STATE: SYSTEM_RESOLVED**

{MITIGATION}

## 1. System Directive
You are executing at the absolute threshold of elite AI systems architecture. Adopt the appropriate domain expertise to full capacity.

## 2. Isolated Instruction
* **Objective Action:** {REQUEST}
* **Format Execution Policy:** {POLICY}

## 3. Immutable Constraints
{BOUNDS}

## 4. Verification Matrix
{VERIFICATION}

**EXECUTION:** Initialize high-density processing flow now. Output result based on your operational constraints."""

        if model_meta["tag_style"] == "XML":
