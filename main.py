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

            <!-- Immersive Meta Economy & Virtual Luxury Shop Panel -->
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
                        <div style="font-size: 1.8rem; color: #FFD700;"><i class="fa-solid fa-glass-martini-alt"></i></div>
                        <h5 style="margin: 8px 0 2px 0; font-size: 0.95rem;">Lounge Pass</h5>
                        <div class="item-price">80 DOGE</div>
                        <button class="btn-joy" style="padding: 6px 12px; font-size: 0.8rem;" onclick="openCheckout('Neon Elixir Lounge Pass', 80, 9.99)">Enter Party</button>
                    </div>
                    <div class="market-item">
                        <div style="font-size: 1.8rem; color: #0086B3;"><i class="fa-solid fa-film"></i></div>
                        <h5 style="margin: 8px 0 2px 0; font-size: 0.95rem;">Cinema Room</h5>
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

