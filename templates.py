"""templates.py - Professional Frontend Template"""


def get_html_template() -> str:
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>TruthLens — AI Fake News Detector</title>
<meta name="description" content="AI-powered fake news detection with 92%+ accuracy using Random Forest and TF-IDF."/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet"/>
<style>
*{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:#07070f;--s1:#0f0f1a;--s2:#161626;--s3:#1e1e32;
  --border:rgba(255,255,255,0.07);--border2:rgba(255,255,255,0.12);
  --purple:#7c6fff;--purple2:#a78bfa;--pink:#f472b6;
  --real:#10b981;--real2:#34d399;--fake:#f43f5e;--fake2:#fb7185;
  --text:#f0f0fa;--sub:#9898b8;--muted:#5a5a7a;
  --r:14px;
}
body{font-family:'Inter',sans-serif;background:var(--bg);color:var(--text);min-height:100vh;overflow-x:hidden}

/* bg orbs */
.orb{position:fixed;border-radius:50%;filter:blur(80px);pointer-events:none;z-index:0}
.orb1{width:600px;height:600px;top:-200px;left:-150px;background:radial-gradient(circle,rgba(124,111,255,.14),transparent 70%)}
.orb2{width:500px;height:500px;bottom:-100px;right:-100px;background:radial-gradient(circle,rgba(244,114,182,.10),transparent 70%)}

/* layout */
.app{position:relative;z-index:1;display:grid;grid-template-columns:260px 1fr;min-height:100vh}

/* ── sidebar ── */
.sidebar{background:var(--s1);border-right:1px solid var(--border);padding:28px 20px;display:flex;flex-direction:column;gap:32px}
.logo{display:flex;align-items:center;gap:10px}
.logo-icon{width:38px;height:38px;border-radius:10px;background:linear-gradient(135deg,var(--purple),var(--pink));display:flex;align-items:center;justify-content:center;font-size:18px;flex-shrink:0}
.logo-text{font-size:1.1rem;font-weight:800;letter-spacing:-.3px}
.logo-text span{background:linear-gradient(90deg,var(--purple2),var(--pink));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}

.nav-label{font-size:.65rem;font-weight:700;text-transform:uppercase;letter-spacing:1.2px;color:var(--muted);margin-bottom:6px}
.nav-item{display:flex;align-items:center;gap:10px;padding:10px 12px;border-radius:10px;font-size:.88rem;font-weight:500;color:var(--sub);cursor:pointer;transition:all .2s;border:1px solid transparent;margin-bottom:2px}
.nav-item:hover,.nav-item.active{background:rgba(124,111,255,.1);border-color:rgba(124,111,255,.2);color:var(--text)}
.nav-item.active{color:var(--purple2)}
.nav-icon{font-size:1rem;width:20px;text-align:center}

.sidebar-stats{margin-top:auto;background:var(--s2);border:1px solid var(--border);border-radius:12px;padding:16px}
.ss-title{font-size:.72rem;font-weight:600;text-transform:uppercase;letter-spacing:.8px;color:var(--muted);margin-bottom:12px}
.ss-row{display:flex;justify-content:space-between;align-items:center;margin-bottom:8px}
.ss-row:last-child{margin-bottom:0}
.ss-key{font-size:.8rem;color:var(--sub)}
.ss-val{font-size:.85rem;font-weight:700;color:var(--purple2)}
.accuracy-ring{display:flex;align-items:center;justify-content:center;margin:12px 0}

/* ── main ── */
.main{display:flex;flex-direction:column;overflow:hidden}

/* topbar */
.topbar{background:var(--s1);border-bottom:1px solid var(--border);padding:0 32px;height:60px;display:flex;align-items:center;justify-content:space-between;flex-shrink:0}
.topbar-title{font-size:.95rem;font-weight:700;color:var(--text)}
.topbar-pills{display:flex;gap:8px}
.pill{padding:4px 12px;border-radius:20px;font-size:.72rem;font-weight:600;letter-spacing:.4px}
.pill-purple{background:rgba(124,111,255,.15);color:var(--purple2);border:1px solid rgba(124,111,255,.25)}
.pill-green{background:rgba(16,185,129,.12);color:var(--real2);border:1px solid rgba(16,185,129,.2)}
.pill-pink{background:rgba(244,114,182,.1);color:#f9a8d4;border:1px solid rgba(244,114,182,.2)}

/* content */
.content{flex:1;padding:28px 32px 48px;overflow-y:auto;display:grid;grid-template-rows:auto 1fr auto;gap:24px}

/* hero */
.hero{text-align:center;padding:20px 0 4px}
.hero h1{font-size:clamp(1.6rem,3vw,2.4rem);font-weight:900;letter-spacing:-.5px;line-height:1.2;margin-bottom:10px}
.hero h1 span{background:linear-gradient(135deg,var(--purple2),var(--pink));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.hero p{font-size:.93rem;color:var(--sub);max-width:480px;margin:0 auto;line-height:1.6}

/* work area */
.work-grid{display:grid;grid-template-columns:1fr 400px;gap:20px;align-items:start}

/* input panel */
.panel{background:var(--s1);border:1px solid var(--border);border-radius:var(--r);overflow:hidden}
.panel-head{padding:16px 20px;border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between}
.panel-head-left{display:flex;align-items:center;gap:8px}
.panel-dot{width:8px;height:8px;border-radius:50%}
.panel-label{font-size:.78rem;font-weight:600;text-transform:uppercase;letter-spacing:.7px;color:var(--sub)}
.panel-body{padding:20px}

textarea{
  width:100%;min-height:220px;padding:14px 16px;resize:vertical;
  background:var(--s2);border:1px solid var(--border);border-radius:10px;
  color:var(--text);font-family:inherit;font-size:.9rem;line-height:1.65;outline:none;
  transition:border-color .2s,box-shadow .2s
}
textarea:focus{border-color:rgba(124,111,255,.5);box-shadow:0 0 0 3px rgba(124,111,255,.1)}
textarea::placeholder{color:var(--muted)}

.input-meta{display:flex;justify-content:space-between;align-items:center;margin-top:8px;margin-bottom:16px}
.word-pill{background:var(--s3);border:1px solid var(--border);border-radius:20px;padding:3px 10px;font-size:.72rem;color:var(--sub)}

.btn-analyze{
  width:100%;padding:14px;border:none;border-radius:10px;cursor:pointer;
  font-family:inherit;font-size:.95rem;font-weight:700;color:#fff;letter-spacing:.2px;
  background:linear-gradient(135deg,#6c5fff,#a855f7);
  box-shadow:0 4px 24px rgba(108,95,255,.4);
  transition:transform .18s,box-shadow .18s,opacity .18s;position:relative;overflow:hidden
}
.btn-analyze::before{content:'';position:absolute;inset:0;background:linear-gradient(135deg,#7c6fff,#ec4899);opacity:0;transition:opacity .3s}
.btn-analyze:hover:not(:disabled)::before{opacity:1}
.btn-analyze:hover:not(:disabled){transform:translateY(-2px);box-shadow:0 8px 32px rgba(108,95,255,.55)}
.btn-analyze:active{transform:translateY(0)}
.btn-analyze:disabled{opacity:.5;cursor:not-allowed}
.btn-analyze span{position:relative;z-index:1}

.sample-row{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:10px}
.btn-sample{
  padding:9px 10px;border-radius:8px;cursor:pointer;font-family:inherit;
  font-size:.78rem;font-weight:600;border:1px solid var(--border);
  background:var(--s3);color:var(--sub);transition:all .2s
}
.btn-sample:hover{border-color:rgba(124,111,255,.35);color:var(--text);background:rgba(124,111,255,.08)}

/* error */
.err{display:none;background:rgba(244,63,94,.08);border:1px solid rgba(244,63,94,.25);border-radius:8px;padding:10px 14px;font-size:.83rem;color:#fda4af;margin-top:10px;align-items:center;gap:8px}
.err.show{display:flex}

/* result panel */
.result-panel{display:flex;flex-direction:column;gap:16px}

/* verdict card */
.verdict-card{
  background:var(--s1);border:1px solid var(--border);border-radius:var(--r);
  padding:22px;display:none;animation:pop .35s cubic-bezier(.34,1.56,.64,1)
}
.verdict-card.show{display:block}
@keyframes pop{from{opacity:0;transform:scale(.95)}to{opacity:1;transform:scale(1)}}

.verdict-header{display:flex;align-items:center;gap:14px;margin-bottom:18px}
.verdict-badge{
  width:52px;height:52px;border-radius:14px;display:flex;align-items:center;
  justify-content:center;font-size:1.5rem;flex-shrink:0
}
.verdict-badge.real{background:rgba(16,185,129,.15);border:1px solid rgba(16,185,129,.3)}
.verdict-badge.fake{background:rgba(244,63,94,.12);border:1px solid rgba(244,63,94,.25)}
.verdict-info h2{font-size:1.05rem;font-weight:800;margin-bottom:3px}
.verdict-info h2.real{color:var(--real2)}
.verdict-info h2.fake{color:var(--fake2)}
.verdict-info p{font-size:.78rem;color:var(--sub)}

/* prob bars */
.prob-section{margin-bottom:16px}
.prob-row{margin-bottom:12px}
.prob-top{display:flex;justify-content:space-between;margin-bottom:5px}
.prob-name{font-size:.75rem;font-weight:600;text-transform:uppercase;letter-spacing:.5px;color:var(--sub)}
.prob-num{font-size:.8rem;font-weight:700}
.prob-num.real{color:var(--real2)}
.prob-num.fake{color:var(--fake2)}
.bar{height:7px;background:var(--s3);border-radius:4px;overflow:hidden}
.bar-inner{height:100%;border-radius:4px;width:0;transition:width .9s cubic-bezier(.4,0,.2,1)}
.bar-real{background:linear-gradient(90deg,var(--real),var(--real2))}
.bar-fake{background:linear-gradient(90deg,var(--fake),var(--fake2))}

/* confidence */
.conf-box{background:var(--s2);border:1px solid var(--border);border-radius:10px;padding:14px 16px;margin-bottom:14px}
.conf-top{display:flex;justify-content:space-between;align-items:center;margin-bottom:8px}
.conf-lbl{font-size:.72rem;font-weight:600;text-transform:uppercase;letter-spacing:.7px;color:var(--muted)}
.conf-val{font-size:1.15rem;font-weight:800;color:var(--purple2)}
.conf-bar{height:8px;background:var(--s3);border-radius:4px;overflow:hidden}
.conf-fill{height:100%;border-radius:4px;width:0;background:linear-gradient(90deg,var(--purple),var(--purple2));transition:width .9s cubic-bezier(.4,0,.2,1)}

/* tags */
.tag-row{display:flex;flex-wrap:wrap;gap:6px}
.tag{padding:4px 10px;border-radius:20px;font-size:.7rem;font-weight:600;background:var(--s3);border:1px solid var(--border);color:var(--sub)}

/* loading overlay */
.loading-card{
  background:var(--s1);border:1px solid var(--border);border-radius:var(--r);
  padding:32px;text-align:center;display:none
}
.loading-card.show{display:block}
.spinner{width:40px;height:40px;border-radius:50%;border:3px solid rgba(124,111,255,.15);border-top-color:var(--purple);animation:spin .75s linear infinite;margin:0 auto 14px}
@keyframes spin{to{transform:rotate(360deg)}}
.loading-card p{font-size:.85rem;color:var(--sub)}
.loading-card .dots::after{content:'';animation:dots 1.4s steps(4,end) infinite}
@keyframes dots{0%,100%{content:''}33%{content:'.'}66%{content:'..'}99%{content:'...'}}

/* placeholder panel */
.placeholder-card{
  background:var(--s1);border:1px dashed var(--border2);border-radius:var(--r);
  padding:40px 24px;text-align:center;color:var(--muted)
}
.placeholder-card .ph-icon{font-size:2.5rem;margin-bottom:14px;opacity:.5}
.placeholder-card p{font-size:.85rem;line-height:1.6}

/* footer */
.page-footer{border-top:1px solid var(--border);padding:16px 32px;display:flex;justify-content:space-between;align-items:center;background:var(--s1);flex-shrink:0}
.page-footer p{font-size:.72rem;color:var(--muted)}
.page-footer a{color:var(--purple2);text-decoration:none}

/* mobile */
@media(max-width:900px){
  .app{grid-template-columns:1fr}
  .sidebar{display:none}
  .work-grid{grid-template-columns:1fr}
  .content{padding:20px 16px 40px}
}
</style>
</head>
<body>
<div class="orb orb1"></div>
<div class="orb orb2"></div>

<div class="app">
  <!-- Sidebar -->
  <aside class="sidebar">
    <div>
      <div class="logo">
        <div class="logo-icon">🔍</div>
        <div class="logo-text"><span>TruthLens</span></div>
      </div>
    </div>
    <div>
      <div class="nav-label">Navigation</div>
      <div class="nav-item active"><span class="nav-icon">🏠</span> Detector</div>
      <div class="nav-item" onclick="window.open('/api/stats','_blank')"><span class="nav-icon">📊</span> API Stats</div>
      <div class="nav-item" onclick="showAbout()"><span class="nav-icon">📖</span> How It Works</div>
    </div>
    <div>
      <div class="nav-label">Model Info</div>
      <div class="nav-item"><span class="nav-icon">🌲</span> Random Forest</div>
      <div class="nav-item"><span class="nav-icon">📝</span> TF-IDF · N-grams</div>
      <div class="nav-item"><span class="nav-icon">🔠</span> 5,000 Features</div>
    </div>
    <div class="sidebar-stats">
      <div class="ss-title">Live Model Stats</div>
      <div class="ss-row"><span class="ss-key">Accuracy</span><span class="ss-val" id="sAcc">Loading…</span></div>
      <div class="ss-row"><span class="ss-key">Trees</span><span class="ss-val">200</span></div>
      <div class="ss-row"><span class="ss-key">Features</span><span class="ss-val">5,000</span></div>
      <div class="ss-row"><span class="ss-key">N-gram</span><span class="ss-val">1–3</span></div>
    </div>
  </aside>

  <!-- Main -->
  <div class="main">
    <!-- Topbar -->
    <div class="topbar">
      <div class="topbar-title">AI Fact-Check Workbench</div>
      <div class="topbar-pills">
        <span class="pill pill-purple">Random Forest</span>
        <span class="pill pill-green">92%+ Accuracy</span>
        <span class="pill pill-pink">Real-Time</span>
      </div>
    </div>

    <!-- Content -->
    <div class="content">
      <div class="hero">
        <h1>Detect <span>Fake News</span> Instantly</h1>
        <p>Paste any news article below. Our AI model analyzes linguistic patterns, sentiment, and n-gram features to determine credibility in milliseconds.</p>
      </div>

      <div class="work-grid">
        <!-- Input panel -->
        <div class="panel">
          <div class="panel-head">
            <div class="panel-head-left">
              <div class="panel-dot" style="background:#f43f5e"></div>
              <div class="panel-dot" style="background:#fbbf24;margin-left:5px"></div>
              <div class="panel-dot" style="background:#10b981;margin-left:5px"></div>
            </div>
            <div class="panel-label">Article Input</div>
            <div style="font-size:.72rem;color:var(--muted)">Min. 3 words</div>
          </div>
          <div class="panel-body">
            <textarea id="newsInput" placeholder="Paste or type a news article here...&#10;&#10;The longer and more detailed the article, the more accurate the prediction will be." oninput="onInput()"></textarea>
            <div class="input-meta">
              <span style="font-size:.75rem;color:var(--muted)">Tip: full articles outperform headlines</span>
              <span class="word-pill"><span id="wc">0</span> words</span>
            </div>
            <button class="btn-analyze" id="analyzeBtn" onclick="analyze()">
              <span>&#x1F50D;&nbsp; Analyze Article</span>
            </button>
            <div class="sample-row">
              <button class="btn-sample" onclick="loadSample('real')">&#x1F4F0; Real News Sample</button>
              <button class="btn-sample" onclick="loadSample('fake')">&#x26A0;&#xFE0F; Fake News Sample</button>
            </div>
            <div class="err" id="errBox"><span>&#x26A0;</span><span id="errMsg"></span></div>
          </div>
        </div>

        <!-- Result panel -->
        <div class="result-panel">
          <!-- Placeholder -->
          <div class="placeholder-card" id="placeholder">
            <div class="ph-icon">&#x1F9E0;</div>
            <p>Enter a news article and click <strong>Analyze Article</strong> to see the AI credibility verdict, probability scores, and confidence level.</p>
          </div>

          <!-- Loading -->
          <div class="loading-card" id="loadingCard">
            <div class="spinner"></div>
            <p>Analyzing with AI<span class="dots"></span></p>
          </div>

          <!-- Verdict -->
          <div class="verdict-card" id="verdictCard">
            <div class="verdict-header">
              <div class="verdict-badge" id="vBadge"></div>
              <div class="verdict-info">
                <h2 id="vTitle"></h2>
                <p id="vSub"></p>
              </div>
            </div>

            <div class="prob-section">
              <div class="prob-row">
                <div class="prob-top">
                  <span class="prob-name">Real Probability</span>
                  <span class="prob-num real" id="realNum">–</span>
                </div>
                <div class="bar"><div class="bar-inner bar-real" id="realBar"></div></div>
              </div>
              <div class="prob-row">
                <div class="prob-top">
                  <span class="prob-name">Fake Probability</span>
                  <span class="prob-num fake" id="fakeNum">–</span>
                </div>
                <div class="bar"><div class="bar-inner bar-fake" id="fakeBar"></div></div>
              </div>
            </div>

            <div class="conf-box">
              <div class="conf-top">
                <span class="conf-lbl">Confidence Score</span>
                <span class="conf-val" id="confVal">–</span>
              </div>
              <div class="conf-bar"><div class="conf-fill" id="confBar"></div></div>
            </div>

            <div class="tag-row" id="tagRow"></div>
          </div>
        </div>
      </div>
    </div>

    <!-- Footer -->
    <div class="page-footer">
      <p>Built with Flask &middot; scikit-learn &middot; Random Forest &middot; TF-IDF &nbsp;|&nbsp; <a href="/api/stats" target="_blank">API Stats</a></p>
      <p>&#x26A0;&#xFE0F; Always cross-reference with trusted sources.</p>
    </div>
  </div>
</div>

<script>
const SAMPLES = {
  real: "The Federal Reserve announced a quarter-point interest rate hike on Wednesday, citing persistent inflation concerns and a resilient labor market. Fed Chair Jerome Powell stated that the committee remains data-dependent and will carefully monitor economic indicators before making further adjustments. Economists broadly anticipated the move, noting that core inflation has remained above the 2 percent target for several consecutive months.",
  fake: "BREAKING: Scientists have discovered a miracle cure for ALL diseases that has been deliberately suppressed by pharmaceutical companies for decades! A whistleblower from inside Big Pharma has leaked documents proving that a simple combination of household items eliminates cancer, diabetes, and heart disease in just 72 hours. The government is desperate to hide this information before it goes viral. Share this before it gets deleted!"
};

function onInput(){
  const t=document.getElementById('newsInput').value.trim();
  document.getElementById('wc').textContent=t?t.split(/\\s+/).length:0;
}

function loadSample(type){
  document.getElementById('newsInput').value=SAMPLES[type];
  onInput();hideError();
}

function showError(msg){
  document.getElementById('errMsg').textContent=msg;
  document.getElementById('errBox').classList.add('show');
}
function hideError(){document.getElementById('errBox').classList.remove('show');}

function setState(state){
  document.getElementById('placeholder').style.display=state==='idle'?'block':'none';
  document.getElementById('loadingCard').className='loading-card'+(state==='loading'?' show':'');
  document.getElementById('verdictCard').className='verdict-card'+(state==='result'?' show':'');
}

async function analyze(){
  const text=document.getElementById('newsInput').value.trim();
  if(!text){showError('Please enter a news article.');return;}
  hideError();
  setState('loading');
  document.getElementById('analyzeBtn').disabled=true;
  try{
    const res=await fetch('/api/analyze',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({text})});
    const data=await res.json();
    if(!data.success){showError(data.error||'Analysis failed.');setState('idle');return;}
    render(data.result);
  }catch(e){
    showError('Network error. Is the server running?');setState('idle');
  }finally{
    document.getElementById('analyzeBtn').disabled=false;
  }
}

function render(r){
  const fake=r.is_fake;
  // badge
  const badge=document.getElementById('vBadge');
  badge.className='verdict-badge '+(fake?'fake':'real');
  badge.textContent=fake?'⚠️':'✅';
  // title
  const title=document.getElementById('vTitle');
  title.className=fake?'fake':'real';
  title.textContent=fake?'LIKELY FAKE NEWS':'LIKELY REAL NEWS';
  // sub
  document.getElementById('vSub').textContent=r.credibility+' · '+r.word_count+' words analyzed';
  // probs
  document.getElementById('realNum').textContent=r.real_probability+'%';
  document.getElementById('fakeNum').textContent=r.fake_probability+'%';
  document.getElementById('confVal').textContent=r.confidence+'%';
  // bars animate
  setTimeout(()=>{
    document.getElementById('realBar').style.width=r.real_probability+'%';
    document.getElementById('fakeBar').style.width=r.fake_probability+'%';
    document.getElementById('confBar').style.width=r.confidence+'%';
  },80);
  // tags
  const tags=document.getElementById('tagRow');
  tags.innerHTML=[
    '🎯 '+r.credibility,
    '📊 Confidence: '+r.confidence+'%',
    '🌲 Random Forest',
    '📝 TF-IDF · N-grams'
  ].map(t=>`<span class="tag">${t}</span>`).join('');
  setState('result');
  document.getElementById('verdictCard').scrollIntoView({behavior:'smooth',block:'nearest'});
}

function showAbout(){
  alert('TruthLens uses a Random Forest classifier trained on TF-IDF features.\\n\\nPipeline:\\n1. Text cleaning (URLs, mentions, special chars removed)\\n2. TF-IDF vectorization (5,000 features, 1-3 word n-grams)\\n3. Random Forest (200 trees) predicts Real vs Fake\\n4. Confidence score from tree vote probabilities');
}

// load stats
(async()=>{
  try{
    const d=await(await fetch('/api/stats')).json();
    if(d.accuracy){document.getElementById('sAcc').textContent=d.accuracy+'%';}
  }catch{}
})();

setState('idle');
</script>
</body>
</html>
"""
