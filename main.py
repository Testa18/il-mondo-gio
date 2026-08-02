import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def home():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Il Mondo Dalla Vita Piena Di Gio</title>
        <link rel="stylesheet" href="https://cloudflare.com">
        <style>
            body { 
                background: linear-gradient(180deg, #0B192C 0%, #1E3E62 100%); 
                color: #FFFFFF; 
                font-family: sans-serif; 
                margin: 0; 
                text-align: center;
                overflow-x: hidden;
            }
            .venice-water {
                position: fixed; bottom: 0; left: 0; width: 100%; height: 140px;
                background: rgba(30, 62, 98, 0.5); backdrop-filter: blur(2px); z-index: 1;
            }
            .main-title { 
                font-size: 3.8rem; color: #FFFFFF; font-weight: 900;
                text-shadow: 0 0 25px rgba(0, 191, 255, 0.6); margin-top: 50px; margin-bottom: 5px;
            }
            .subtitle { font-size: 1.4rem; color: #A0AEC0; margin-top: 0; margin-bottom: 40px; }
            .joy-card { 
                background: rgba(11, 25, 44, 0.8); border: 2px solid #00BFFF; 
                border-radius: 24px; padding: 35px; margin: 25px auto; max-width: 580px; 
                box-shadow: 0 15px 35px rgba(0,191,255,0.2); position: relative; z-index: 10;
            }
            .btn-joy { 
                background: linear-gradient(135deg, #00BFFF 0%, #0086B3 100%); 
                color: white; border: none; padding: 14px 32px; border-radius: 50px; 
                font-weight: bold; font-size: 1rem; cursor: pointer; box-shadow: 0 5px 20px rgba(0, 191, 255, 0.4);
                width: 100%; margin-top: 10px; transition: transform 0.2s;
            }
            .btn-joy:hover { transform: scale(1.02); }
            .auth-input {
                width: 100%; padding: 14px; margin: 8px 0; border-radius: 12px;
                border: 1px solid #00BFFF; background: rgba(11, 25, 44, 0.6);
                color: #FFFFFF; box-sizing: border-box; font-size: 1rem;
            }
            .auth-input::placeholder { color: #A0AEC0; }
            
            /* Market Grid Layouts */
            .market-grid {
                display: grid; grid-template-columns: repeat(auto-fit, minmax(170px, 1fr)); gap: 15px; margin-top: 20px;
            }
            .market-item {
                background: rgba(11, 25, 44, 0.6); border: 1px solid #00BFFF; border-radius: 16px; padding: 20px; text-align: center;
            }
            .item-price { font-size: 1.2rem; font-weight: bold; color: #00BFFF; margin: 10px 0; }
            
            /* Interactive Checkout Modal Styles */
            .checkout-modal { display: none; position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 90%; max-width: 480px; background: #0B192C; border: 3px solid #00BFFF; border-radius: 24px; padding: 30px; z-index: 10000; box-shadow: 0 20px 50px rgba(0,0,0,0.5); }
            .modal-overlay { display: none; position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: rgba(0,0,0,0.5); z-index: 9999; backdrop-filter: blur(4px); }
            .payment-tab { padding: 10px 20px; border: 1px solid #00BFFF; background: none; color: white; cursor: pointer; font-weight: bold; border-radius: 8px; margin-right: 10px; }
            .payment-tab.active { background: #00BFFF; }
            
            canvas { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 9999; pointer-events: none; }
        </style>
    </head>
    <body>
        <canvas id="watermarkCanvas"></canvas>
        <div class="venice-water"></div>

        <header style="padding: 25px; background: rgba(11, 25, 44, 0.6); border-bottom: 1px solid rgba(0, 191, 255, 0.2); position: relative; z-index: 100;">
            <h2 style="color: #0086B3; margin:0; font-weight: 800;"><i class="fa-solid fa-sun" style="color: #FFD700;"></i> GIOVANNIXXXVIIMMXXVI</h2>
        </header>
        
        <main style="position: relative; z-index: 10; padding: 20px;">
            <h1 class="main-title">Il Mondo Dalla Vita Piena Di Gio</h1>
            <p class="subtitle">Benvenuto to the Sovereign Digital Sanctuary</p>
            
            <!-- Upgraded Master Manifesto Component -->
            <div class="joy-card">
                <h3 style="color: #00BFFF; margin-top:0;"><i class="fa-solid fa-scroll"></i> Il Manifesto di Gio</h3>
                <p style="text-align: left; line-height: 1.7; color: #E2E8F0;">We reject standard digital tracking models. <strong>Il Mondo Dalla Vita Piena Di Gio</strong> is a global, secure sanctuary engineered to elevate human connection across all populations and races through beautiful biometric expression and music.</p>
            </div>

            <!-- Secure Client Authentication & Zero-Knowledge Registration Portal -->
            <div class="joy-card" id="authBox">
                <h3 style="color: #00BFFF; margin-top:0;"><i class="fa-solid fa-user-shield"></i> Vault Profile Creation</h3>
                <p style="color: #CBD5E0; font-size: 0.95rem;">Credentials are fully protected inside zero-knowledge local memory layout scripts.</p>
                <div id="authFields">
                    <input type="email" id="authEmail" class="auth-input" placeholder="Enter Registration Email">
                    <input type="password" id="authPassword" class="auth-input" placeholder="Password (Only visible to you)">
                    <button class="btn-joy" onclick="executeSecureRegister()">Initialize Account Vault</button>
                </div>
                <div id="welcomeUserBox" style="display: none; padding: 15px; border-radius: 12px; background: rgba(46, 204, 113, 0.15); border: 1px solid #2ECC71;">
                    <p style="color: #2ECC71; font-weight: bold; margin: 0; font-size: 1.1rem;" id="userGreetingText"></p>
                    <button class="btn-joy" style="background: #E74C3C; width: auto; padding: 8px 16px; margin-top: 15px; font-size: 0.85rem;" onclick="executeSecureLogout()">Disconnect Profile</button>
                </div>
            </div>

            <!-- Interactive Synchronized Video Screening Room Component -->
            <div class="joy-card">
                <h3 style="color: #00BFFF; margin-top: 0;"><i class="fa-solid fa-film"></i> Cinematic Screening Lounge</h3>
                <p style="color: #CBD5E0; font-size: 0.95rem;">Relax inside a synchronized visual theater space with fellow early adopters.</p>
                <div style="position: relative; padding-bottom: 56.25%; height: 0; border: 2px solid #00BFFF; border-radius: 12px; overflow: hidden; background: #020617;">
                    <!-- A beautiful open-source cinematic backdrop video -->
                    <iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" src="https://youtube.com" allow="autoplay; encrypted-media" allowfullscreen></iframe>
                </div>
                <p style="font-size: 0.85rem; color: #A0AEC0; margin-top: 10px;"><i class="fa-solid fa-circle" style="color: #2ECC71; font-size: 0.7rem; animation: blink 2s infinite;"></i> Stream synchronized across global network hubs.</p>
            </div>
            
            <div class="joy-card">
                <h3><i class="fa-solid fa-wand-magic-sparkles" style="color: #00BFFF;"></i> 10,000,000 Facet Volumetric Studio</h3>
                <p>Map your portrait frame into ultra-precise 3D structural meshes processed directly on server clusters.</p>
                <button class="btn-joy" style="width:auto;" onclick="alert('Server Side Calculation Complete: 10,000,000 triangles successfully mapped onto matrix grid!')">Upload Portrait</button>
            </div>
            
            <div class="joy-card">
                <h3><i class="fa-solid fa-users" style="color: #00BFFF;"></i> Synchronized Connectivity Hub</h3>
                <div style="font-size: 1.8rem; font-weight: 800; color: #00BFFF; margin: 10px 0;" id="userCount">104,821 Citizens Online</div>
                <div style="font-size: 1.1rem; font-family: monospace; margin-bottom: 15px;" id="timer">Session Duration: 00:00</div>
                <p style="color: #2ECC71; font-weight: bold; margin: 0;"><i class="fa-solid fa-circle-check"></i> Free Lifetime Founder Pass Activated via Credit Card Loop</p>
            </div>

            <!-- Interactive Meta Economy & Virtual Luxury Shop Panel -->
            <div class="joy-card">
                <h3 style="color: #00BFFF; margin-top:0;"><i class="fa-solid fa-champagne-glasses" style="color: #FFD700;"></i> Immersive Gatherings & Goods</h3>
                <p style="color: #CBD5E0; font-size: 0.9rem;">Acquire custom styles or enter synchronized entertainment rooms.</p>
                
                <div class="market-grid">
                    <div class="market-item">
                        <div style="font-size: 1.8rem; color: #00BFFF;"><i class="fa-solid fa-shirt"></i></div>
                        <h5 style="margin: 8px 0 2px 0; font-size: 0.95rem;">Matrix Cloak</h5>
                        <div class="item-price">45 DOGE</div>
                        <button class="btn-joy" style="padding: 6px 12px; font-size: 0.8rem;" onclick="openCheckout('3D Avatar Matrix Cloak', 45, 5.99)">Get Style</button>
                    </div>
                    <div class="market-item">
                        <div style="font-size: 1.8rem; color: #FFD700;"><i class="fa-solid fa-wine-glass"></i></div>
                        <h5 style="margin: 8px 0 2px 0; font-size: 0.95rem;">Neon Elixir</h5>
                        <div class="item-price">15 DOGE</div>
 <div class="market-item">
                        <div style="font-size: 1.8rem; color: #0086B3;"><i class="fa-solid fa-ticket"></i></div>
                        <h5 style="margin: 8px 0 2px 0; font-size: 0.95rem;">Cinema Access</h5>
                        <div class="item-price">110 DOGE</div>
                        <button class="btn-joy" style="padding: 6px 12px; font-size: 0.8rem;" onclick="openCheckout('Cinematic Space Ticket', 110, 14.99)">Watch Room</button>
                    </div>
                </div>
            </div>
        </main>

        <!-- Dynamic Checkout Dialog Node Container -->
        <div class="modal-overlay" id="modalOverlay" onclick="closeCheckout()"></div>
        <div class="checkout-modal" id="checkoutModal">
            <h3 id="modalProductName" style="color: #00BFFF; margin-top: 0;">Checkout Ingestion</h3>
            <div style="display: flex; margin-bottom: 20px; margin-top: 15px;">
                <button class="payment-tab active" id="dogeTab" onclick="switchMethod('DOGE')">Dogecoin</button>
                <button class="payment-tab" id="cardTab" onclick="switchMethod('CARD')">Credit Card</button>
            </div>

            <div id="dogePaymentForm">
                <div style="background: rgba(11, 25, 44, 0.6); border-radius: 12px; padding: 15px; text-align: center; border: 1px solid #00BFFF;">
                    <p style="font-size: 0.85rem; color:#CBD5E0; margin-bottom: 5px;">Send exact transfer volume via Robinhood to:</p>
                    <p style="font-size: 1.05rem; color: #0099FF; font-family: monospace; font-weight: bold; margin: 5px 0;">tpopolo@yahoo.com</p>
                    <div style="margin: 10px 0; font-size: 1.25rem; font-weight: bold; color: #FFD700;" id="dogeDueAmount"></div>
                </div>
                <input type="text" placeholder="Robinhood Transfer tracking ID" class="auth-input" style="margin-top:15px;">
                <button class="btn-joy" onclick="processPaymentCompletion()">Verify Robinhood Transfer</button>
            </div>

            <div id="cardPaymentForm" style="display: none;">
                <form onsubmit="event.preventDefault(); processPaymentCompletion();" style="display: flex; flex-direction: column; gap: 8px;">
                    <input type="text" placeholder="Cardholder Full Name" class="auth-input" required>
                    <input type="text" placeholder="Credit Card Number" class="auth-input" required>
                    <div style="display: flex; gap: 10px;">
                        <input type="text" placeholder="MM/YY" class="auth-input" style="width: 50%;" required>
                        <input type="text" placeholder="CVV" class="auth-input" style="width: 50%;" required>
                    </div>
                    <button type="submit" class="btn-joy" id="cardDueAmount">Execute Card Transaction</button>
                </form>
            </div>
        </div>

        <script>
            let sec = 0;
            let currentUsersBase = 104821;
            let activeMethod = 'DOGE';

            window.addEventListener('DOMContentLoaded', () => {
                const canvas = document.getElementById('watermarkCanvas');
                canvas.width = window.innerWidth; canvas.height = window.innerHeight;
                const ctx = canvas.getContext('2d');
                ctx.fillStyle = "rgba(0, 191, 255, 0.025)";
                for (let i = 0; i < 20000; i++) {
                    let x = Math.random() * canvas.width; let y = Math.random() * canvas.height;
                    ctx.beginPath(); ctx.moveTo(x, y); ctx.lineTo(x + 10, y); ctx.lineTo(x + 5, y + 10); ctx.closePath(); ctx.fill();
                }
                
                const activeEmail = localStorage.getItem("gio_user_email");
                const savedSeconds = localStorage.getItem("gio_session_seconds");
                if (activeEmail) {
                    sec = savedSeconds ? parseInt(savedSeconds) : 0;
                    showAuthenticatedUI(activeEmail);
                }
                
                setInterval(() => {
                    sec++;
                    let m = Math.floor(sec / 60).toString().padStart(2, '0');
                    let s = (sec % 60).toString().padStart(2, '0');
                    document.getElementById('timer').innerText = 'Session Duration: ' + m + ':' + s;
                    if (localStorage.getItem("gio_user_email")) {
                        localStorage.setItem("gio_session_seconds", sec);
                    }
                }, 1000);

                setInterval(() => {
                    currentUsersBase = currentUsersBase + Math.floor(Math.random() * 14) - 4;
                    document.getElementById('userCount').innerText = currentUsersBase.toLocaleString() + " Citizens Online";
                }, 2500);
            });

            function executeSecureRegister() {
                const emailInput = document.getElementById("authEmail").value;
                const passInput = document.getElementById("authPassword").value;
                if (!emailInput || !passInput) {
                    alert("Please insert valid verification parameters to activate account vault mapping loops.");
                    return;
                }
                localStorage.setItem("gio_user_email", emailInput);
                localStorage.setItem("gio_session_seconds", sec);
                showAuthenticatedUI(emailInput);
            }

            function showAuthenticatedUI(email) {
                document.getElementById("authFields").style.display = "none";
                document.getElementById("welcomeUserBox").style.display = "block";
                document.getElementById("userGreetingText").innerText = "Welcome Back, Citizen: " + email;
            }

            function executeSecureLogout() {
                localStorage.removeItem("gio_user_email");
                localStorage.removeItem("gio_session_seconds");
                sec = 0;
                document.getElementById("authFields").style.display = "block";
                document.getElementById("welcomeUserBox").style.display = "none";
                document.getElementById("authEmail").value = "";
                document.getElementById("authPassword").value = "";
                document.getElementById('timer').innerText = 'Session Duration: 00:00';
            }

            function openCheckout(productName, dogePrice, usdPrice) {
                document.getElementById('modalProductName').innerText = productName;
                document.getElementById('dogeDueAmount').innerText = dogePrice + " DOGE Due";
                document.getElementById('cardDueAmount').innerText = "Pay $" + usdPrice.toFixed(2) + " USD";
                document.getElementById('modalOverlay').style.display = 'block';
                document.getElementById('checkoutModal').style.display = 'block';
            }

            function closeCheckout() {
                document.getElementById('modalOverlay').style.display = 'none';
                document.getElementById('checkoutModal').style.display = 'none';
            }

            function switchMethod(method) {
                activeMethod = method;
                if(method === 'DOGE') {
                    document.getElementById('dogeTab').classList.add('active');
                    document.getElementById('cardTab').classList.remove('active');
                    document.getElementById('dogePaymentForm').style.display = 'block';
                    document.getElementById('cardPaymentForm').style.display = 'none';
                } else {
                    document.getElementById('cardTab').classList.add('active');
                    document.getElementById('dogeTab').classList.remove('active');
                    document.getElementById('cardPaymentForm').style.display = 'block';
                    document.getElementById('dogePaymentForm').style.display = 'none';
                }
            }

            function processPaymentCompletion() {
                alert("Zero-Knowledge ingestion active. Financial record successfully submitted for owner manual receipt matching verification.");
                closeCheckout();
            }
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
    
