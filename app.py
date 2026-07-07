import streamlit as st

# ==========================================
# CONSTANT TEMPLATES & STRINGS (Defined Globally to Prevent Parsing Errors)
# ==========================================
VERIFICATION_STRING = "1. Generate a latent factual validation array in memory.\n2. Cross-examine all claims against the provided data feed.\n3. If data is insufficient for absolute certainty, print [INSUFFICIENT_DATA_ERROR].\n4. Correct all semantic anomalies before printing the final response."

XML_TEMPLATE = """**[SYSTEM OPERATION COMMAND: UNIVERSAL METAMORPHIC PROMPT v3.0]**
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

MARKDOWN_TEMPLATE = """# SYSTEM OPERATION COMMAND: UNIVERSAL METAMORPHIC PROMPT v3.0
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

# 1. Page Configuration Setup (Rigid Corporate Identity)
st.set_page_config(
    page_title="PROMPT_OS // McKinsey & Co. Design System", 
    page_icon="⚖️", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# 2. McKinsey Design System CSS Injection (Bower Serif Typography & High-Contrast Blue)
st.markdown("""
<style>
    @import url('https://googleapis.com');
    
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #FFFFFF !important;
        font-family: 'Inter', sans-serif !important;
        color: #051C2C !important;
    }
    
    .mckinsey-title {
        font-family: 'Lora', Georgia, serif;
        font-size: 2.4rem;
        font-weight: 700;
        color: #051C2C;
        letter-spacing: -0.5px;
        margin-bottom: 2px;
        padding-top: 10px;
    }
    .mckinsey-subtitle {
        font-family: 'Inter', sans-serif;
        color: #2251FF;
        font-size: 0.8rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 30px;
        border-bottom: 2px solid #051C2C;
        padding-bottom: 12px;
    }
    
    div[data-testid="stVerticalBlock"] > div {
        background: #F8FAFC !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 2px !important;
        padding: 24px !important;
        box-shadow: none !important;
    }
    
    .stTextArea textarea {
        background-color: #FFFFFF !important;
        border: 1px solid #051C2C !important;
        color: #051C2C !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 0.95rem !important;
        border-radius: 2px !important;
    }
    .stTextArea textarea:focus {
        border-color: #2251FF !important;
        box-shadow: 0 0 0 1px #2251FF !important;
    }
    
    .stSelectbox div[data-baseweb="select"] {
        background-color: #FFFFFF !important;
        border: 1px solid #CBD5E1 !important;
        color: #051C2C !important;
        font-size: 0.95rem !important;
        border-radius: 2px !important;
    }
    
    label p {
        font-family: 'Inter', sans-serif !important;
        font-size: 0.9rem !important;
        font-weight: 700 !important;
        color: #051C2C !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .mckinsey-log-box {
        background: #051C2C !important;
        border-left: 4px solid #2251FF !important;
        padding: 16px !important;
        border-radius: 2px;
        font-family: 'Inter', sans-serif;
        font-size: 0.85rem;
        color: #F8FAFC;
    }
    
    .stButton>button {
        background: #2251FF !important;
        color: #FFFFFF !important;
        border: none !important;
        padding: 14px 28px !important;
        font-size: 0.95rem !important;
        font-weight: 600 !important;
        border-radius: 2px !important;
        width: 100% !important;
        letter-spacing: 0.5px;
        transition: background 0.15s ease-in-out !important;
    }
    .stButton>button:hover {
        background: #051C2C !important;
    }
    
    code, pre {
        background-color: #051C2C !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 2px !important;
        font-size: 0.9rem !important;
        padding: 15px !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Branding Header Component
st.markdown('<h1 class="mckinsey-title">McKinsey&Company</h1>', unsafe_allow_html=True)
st.markdown('<p class="mckinsey-subtitle">Linguistic Strategy Engine // Prompt OS v3.0</p>', unsafe_allow_html=True)

# ==========================================
# CORE DATA ENGINE (The Knowledge Database)
# ==========================================
MODEL_DATABASE = {
    "Deep Reasoning Engines (OpenAI o1/o3, DeepSeek R1)": {
        "tag_style": "Markdown",
        "anchor_trigger": "[OBJECTIVE_FUNCTION: EXACT_BOUNDS]",
        "mitigation_code": "CRITICAL: Disable conversational filler. Enforce mathematical and formal logical boundaries. Validate all negative constraints before state convergence.",
        "telemetry": "Active Deployment Protocol: Mathematical boundary optimization engaged. Token weighting focused on logic nodes."
    },
    "Long-Context Architectures (Google Gemini 1.5/2.0, Claude 3.5 Sonnet)": {
        "tag_style": "XML",
        "anchor_trigger": "[ANCHOR_DENSITY: HIGHEST]",
        "mitigation_code": "SYSTEM DIRECTIVE: Maintain absolute semantic adherence throughout the entire text span. Neutralize middle-context attention decay by sequential node tracking.",
        "telemetry": "Active Deployment Protocol: Attention anchor matrix verified. Context mitigation scripts fully armed."
    },
    "Autonomous AI Agents & Execution Tools (LangChain, CrewAI, Tool Agents)": {
        "tag_style": "XML",
        "anchor_trigger": "[AGENT_STATE: STATEFUL_MONITORING]",
        "mitigation_code": "AGENT CONSTRAINT: Print execution state and sub-goal validation parameters before calling any external tool. Prevent iterative logic looping.",
        "telemetry": "Active Deployment Protocol: Stateful tracking system initialization template verified. Zero-loop safety enabled."
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
# USER INTERFACE LAYOUT & INTERFACE INPUTS
# ==========================================
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("### 📥 Input parameters")
    user_request = st.text_area(
        "Objective Specification (The Raw Request):", 
        height=130,
        placeholder="Type raw human request parameters here..."
    )
    
    constraints_input = st.text_area(
        "Immutable Boundaries (Hard Negative Constraints):", 
        height=110,
        placeholder="Enforce distinct operational restrictions here..."
    )

with col2:
    st.markdown("### 🎛️ Architecture Selection")
    target_receiver = st.selectbox("Target Receiver Architecture:", list(MODEL_DATABASE.keys()))
    product_format = st.selectbox("Target Output Format Matrix:", list(OUTPUT_DATABASE.keys()))
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="mckinsey-log-box">
        <strong>MANAGEMENT ANALYSIS LOG:</strong><br>{MODEL_DATABASE[target_receiver]['telemetry']}
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# RUNTIME KPI METRICS SYSTEM (Operational Dashboard)
# ==========================================
st.markdown("### 📊 Operational Completion Metrics (KPIs)")
kpi_col1, kpi_col2, kpi_col3 = st.columns(3)

request_length = len(user_request.strip()) if user_request else 0
constraints_length = len(constraints_input.strip()) if constraints_input else 0

if request_length == 0:
    density_score = 0
    density_status = "Critical Blank"
elif request_length < 50:
    density_score = 35
    density_status = "Insufficient Context"
elif request_length < 150:
    density_score = 70
    density_status = "Optimal Stability"
else:
    density_score = 100
