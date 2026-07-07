import streamlit as st

# 1. Page Configuration & Premium Title Layout
st.set_page_config(
    page_title="PROMPT_OS // v3.0", 
    page_icon="⚡", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# 2. Advanced Premium CSS Injection (Custom Dark Theme & Micro-Interactions)
st.markdown("""
<style>
    /* Absolute Theme Resets & Typography */
    @import url('https://googleapis.com');
    
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #0B0F19 !important;
        font-family: 'Inter', sans-serif !important;
        color: #E2E8F0 !important;
    }
    
    /* Header & Branding Area */
    .brand-title {
        font-family: 'JetBrains+Mono', monospace;
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(135deg, #00F2FE 0%, #4FACFE 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -1.5px;
        margin-bottom: 0px;
    }
    .brand-subtitle {
        font-family: 'JetBrains Mono', monospace;
        color: #64748B;
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 30px;
    }
    
    /* Glassmorphism Input Cards */
    div[data-testid="stVerticalBlock"] > div {
        background: rgba(15, 23, 42, 0.6);
        border: 1px solid rgba(51, 65, 85, 0.5);
        border-radius: 12px;
        padding: 5px;
    }
    
    /* Sleek Custom Text Areas & Select Boxes */
    .stTextArea textarea, .stSelectbox div[data-baseweb="select"] {
        background-color: #020617 !important;
        border: 1px solid #1E293B !important;
        color: #F8FAFC !important;
        font-family: 'Inter', sans-serif;
        border-radius: 8px !important;
        transition: all 0.3s ease;
    }
    .stTextArea textarea:focus {
        border-color: #38BDF8 !important;
        box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.2) !important;
    }
    
    /* Kinetic Feedback Status Box */
    .status-box {
        background: rgba(14, 116, 144, 0.15) !important;
        border-left: 4px solid #06B6D4 !important;
        padding: 15px !important;
        border-radius: 0px 8px 8px 0px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.85rem;
        color: #22D3EE;
    }
    
    /* High-Performance Action Button */
    .stButton>button {
        background: linear-gradient(135deg, #38BDF8 0%, #0369A1 100%) !important;
        color: #FFFFFF !important;
        border: none !important;
        padding: 14px 28px !important;
        font-weight: 600 !important;
        font-family: 'JetBrains Mono', monospace !important;
        border-radius: 8px !important;
        width: 100% !important;
        letter-spacing: 1px;
        box-shadow: 0 4px 20px rgba(56, 189, 248, 0.25) !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 24px rgba(56, 189, 248, 0.4) !important;
    }
    
    /* Code Blocks Overhaul */
    code, pre {
        background-color: #020617 !important;
        border: 1px solid #334155 !important;
        border-radius: 8px !important;
        font-family: 'JetBrains Mono', monospace !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Branding Header
st.markdown('<h1 class="brand-title">PROMPT_OS // METAMORPHIC</h1>', unsafe_allow_html=True)
st.markdown('<p class="brand-subtitle">Universal Latent Space Operating System v3.0</p>', unsafe_allow_html=True)

# ==========================================
# CORE DATA ENGINE (The Knowledge Database)
# ==========================================
MODEL_DATABASE = {
    "Deep Reasoning Engines (OpenAI o1/o3, DeepSeek R1)": {
        "tag_style": "Markdown",
        "anchor_trigger": "[OBJECTIVE_FUNCTION: EXACT_BOUNDS]",
        "mitigation_code": "CRITICAL: Disable conversational filler. Enforce mathematical and formal logical boundaries. Validate all negative constraints before state convergence.",
        "telemetry": "Active Status: Deep Cognitive Latent Search Forced. Manual CoT suppressed."
    },
    "Long-Context Architectures (Google Gemini 1.5/2.0, Claude 3.5 Sonnet)": {
        "tag_style": "XML",
        "anchor_trigger": "[ANCHOR_DENSITY: HIGHEST]",
        "mitigation_code": "SYSTEM DIRECTIVE: Maintain absolute semantic adherence throughout the entire text span. Neutralize middle-context attention decay by sequential node tracking.",
        "telemetry": "Active Status: Context Optimization Mapping deployed. Middle-context dropping neutralized."
    },
    "Autonomous AI Agents & Execution Tools (LangChain, CrewAI, Terminal Exec)": {
        "tag_style": "XML",
        "anchor_trigger": "[AGENT_STATE: STATEFUL_MONITORING]",
        "mitigation_code": "AGENT CONSTRAINT: Print execution state and sub-goal validation parameters before calling any external tool. Prevent iterative logic looping.",
        "telemetry": "Active Status: Stateful Loop Prevention Shield active. Runtime threshold monitored."
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
# USER INTERFACE LAYOUT (Dynamic Compilation)
# ==========================================
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("### 📥 1. Core Target Dynamics")
    user_request = st.text_area(
        "Objective Specification (The Raw Request):", 
        height=140,
        placeholder="e.g., Deconstruct the vulnerability vectors of decentralized finance smart contracts during liquidity drain stress tests..."
    )
    
    constraints_input = st.text_area(
        "Immutable Boundaries (Hard Negative Constraints):", 
        height=110,
        placeholder="e.g., Ban traditional audit checklists. Rely strictly on game theory models and zero-knowledge mathematical axioms..."
    )

with col2:
    st.markdown("### 🎛️ 2. Architectural Adaptation Tuning")
    target_receiver = st.selectbox("Select Targeted System Receiver Architecture:", list(MODEL_DATABASE.keys()))
    product_format = st.selectbox("Select Target Output Matrix Format:", list(OUTPUT_DATABASE.keys()))
    
    st.markdown("<br>", unsafe_allow_html=True)
    # Interactive Kinetic Telemetry Box
    st.markdown(f"""
    <div class="status-box">
        <strong>⚙️ SYSTEM TELEMETRY LAYER:</strong><br>
        {MODEL_DATABASE[target_receiver]['telemetry']}
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ==========================================
# FABRIC COMPILATION PROTOCOL & OUTPUT
# ==========================================
if st.button("⚡ EXECUTE SYSTEM COMPILATION"):
    if not user_request:
        st.error("COMPILATION CRITICAL ERROR: Empty Objective Specification. System execution halted.")
    else:
        model_meta = MODEL_DATABASE[target_receiver]
        output_meta = OUTPUT_DATABASE[product_format]
        
        verification_string = """
1. Generate a latent factual validation array in memory.
2. Cross-examine all claims against the provided data feed.
3. If data is insufficient for absolute certainty, print [INSUFFICIENT_DATA_ERROR] instead of guessing.
4. Correct all semantic anomalies before printing the final response.
"""

        # Generate XML vs Markdown structural layout
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

