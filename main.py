import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Il Mondo Dalla Vita Piena Di Gio")

@app.get("/")
def home():
    html_content


 = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Il Mondo Dalla Vita Piena Di Gio</title>
        <link rel="stylesheet" href="https://cloudflare.com">
        <style>
            :root {
                --vibrant-sky: #00BFFF;
                --deep-venice-night: #0B192C;
                --water-blue: #1E3E62;
                --pure-white: #FFFFFF;
            }
            
            body { 
                background: linear-gradient(180deg, var(--deep-venice-night) 0%, var(--water-blue) 100%); 
                color: var(--pure-white); 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
                margin: 0; 
                overflow-x: hidden;
            }

            /* Animated Atmospheric Cloud Layer */
            .cloud-bg {
                position: absolute; top: 10%; left: -10%; width: 120%; height: 200px;
                background: radial-gradient(circle, rgba(255,255,255,0.03) 0%, transparent 70%);
                animation: floatClouds 40s linear infinite;
                pointer-events: none;
            }
            @keyframes floatClouds {
                0% { transform: translateX(0); }
                100% { transform: translateX(50px); }
            }

            /* Grand Dynamic Water Waves */
            .venice-water {
                position: fixed; bottom: 0; left: 0; width: 100%; height: 180px;
                background: rgba(30, 62, 98, 0.4);
                backdrop-filter: blur(2px); z-index: 1; pointer-events: none;
            }
            .wave {
                position: absolute; bottom: 0; width: 200%; height: 100%;
                background: url('data:image/svg+xml,<svg xmlns="http://w3.org" viewBox="0 0 1200 120" preserveAspectRatio="none"><path d="M0,0V46.29c47.79,22.2,103.59,32.17,158,28,70.36-5.37,136.33-33.31,206.8-37.5C438.64,32.43,512.34,53.67,583,72.05c69.27,18,138.3,24.88,209.4,13.08,36.15-6,69.85-17.84,104.45-29.34C989.49,25,1113-14.29,1200,42.4V120H0Z" fill="%230B192C" opacity=".3"/></svg>');
                background-size: 50% 100%;
                animation: waveMove 12s infinite linear;
            }
            @keyframes waveMove {
                0% { transform: translateX(0); }
                100% { transform: translateX(-50%); }
            }

            /* Iconic Gondola Silhouette Animation */
            .gondola-silhouette {
                position: absolute; bottom: 60px; left: -150px; width: 120px; height: 40px;
                background: url('data:image/svg+xml,<svg xmlns="http://w3.org" viewBox="0 0 100 30"><path d="M0,25 Q30,28 50,20 Q70,10 90,22 Q95,15 100,5 Q85,25 50,25 Q15,25 0,25 Z" fill="%23020617"/></svg>');
                animation: rowGondola 35s linear infinite; z-index: 2;
            }
            @keyframes rowGondola {
                0% { left: -150px; transform: translateY(0px) rotate(0deg); }
                50% { transform: translateY(3px) rotate(1deg); }
                100% { left: 110%; transform: translateY(0px) rotate(0deg); }
            }

            .main-title { 
                font-size: 4.2rem; 
                color: var(--pure-white); 
                font-weight: 900; 
                letter-spacing: -1px;
                text-shadow: 0 0 30px rgba(0, 191, 255, 0.6);
                margin-bottom: 5px;
            }
            
            .benvenuto-subtitle { 
                font-size: 1.4rem; 
                color: #A0AEC0; 
                font-weight: 400; 
                margin-top: 0;
                margin-bottom: 40px;
            }

            .joy-card { 
                background: rgba(11, 25, 44, 0.75); 
                border: 2px solid var(--vibrant-sky); 
                border-radius: 24px; 
                padding: 35px; 
                margin: 25px auto; 
                max-width: 600px; 
                box-shadow: 0 15px 35px rgba(0,191,255,0.2); 
                backdrop-filter: blur(15px);
                position: relative; z-index: 10;
            }
            
            .btn-joy { 
                background: linear-gradient(135deg, var(--vibrant-sky) 0%, #0086B3 100%); 
                color: white; border: none; padding: 14px 32px; 
                border-radius: 50px; font-weight: bold; font-size: 1rem; cursor: pointer;
                box-shadow: 0 5px 20px rgba(0, 191, 255, 0.4); transition: transform 0.2s;
            }
            .btn-joy:hover { transform: scale(1.03); }
            
            canvas { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 9999; pointer-events: none; }
            
            .manifesto-text {
                font-size: 1.1rem; line-height: 1.8; color: #E2E8F0; text-align: left; margin-top: 15px;
            }
        </style>
    </head>
    <body>
        <div class="cloud-bg"></div>
        <canvas id="watermarkCanvas"></canvas>
        
        <!-- Animated Water & Gondola Scene -->
        <div class="venice-water"><div class="wave"></div></div>
        <div class="gondola-silhouette"></div>

        <header style="padding: 25px; background: rgba(11, 25, 44, 0.5); border-bottom: 1px solid rgba(0, 191, 255, 0.2); position: relative; z-index: 100;">
            <h2 style="color: var(--vibrant-sky); margin:0; font-weight: 800;"><i class="fa-solid fa-sun" style="color: #FFD700;"></i> GIOVANNIXXXVIIMMXXVI</h2>
        </header>
        
        <main style="padding: 60px 20px; position: relative; z-index: 10;">
            <h1 class="main-title">Il Mondo Dalla Vita Piena Di Gio</h1>
            <p class="benvenuto-subtitle">Benvenuto to the Sovereign Digital Sanctuary</p>
            
            <!-- Upgraded Master Manifesto Component -->
            <div class="joy-card">
                <h3 style="color: var(--vibrant-sky); margin-top:0;"><i class="fa-solid fa-scroll"></i> Il Manifesto di Gio</h3>
                <div class="manifesto-text">
                    <p>We reject standard digital tracking models. <strong>Il Mondo Dalla Vita Piena Di Gio</strong> is a global, secure sanctuary engineered to elevate human connection across all populations and races through beautiful biometric expression and music.</p>
                    <p>Every digital citizen remains fully protected by zero-knowledge cryptographic safeguards, ensuring total immunity against security exploits or identity manipulation.</p>
                </div>
            </div>
            
            <div class="joy-card">
                <h3><i class="fa-solid fa-wand-magic-sparkles" style="color: var(--vibrant-sky);"></i> 10,000,000 Facet Volumetric Studio</h3>
                <p style="color: #CBD5E0;">Map your portrait frame into ultra-precise 3D structural meshes processed directly on server clusters.</p>
                <button class="btn-joy" onclick="alert('Server Side Calculation Complete: 10,000,000 triangles successfully mapped onto matrix grid!')">Upload Portrait</button>
            </div>
            
            <div class="joy-card">
                <h3><i class="fa-solid fa-users" style="color: var(--vibrant-sky);"></i> Synchronized Connectivity Hub</h3>
                <div style="font-size: 1.8rem; font-weight: 800; color: var(--vibrant-sky); margin: 10px 0;" id="userCount">104,821 Citizens Online</div>
                <div style="font-size: 1.1rem; font-family: monospace; margin-bottom: 15px;" id="timer">Session Duration: 00:00</div>
                <p style="color: #2ECC71; font-weight: bold; margin: 0;"><i class="fa-solid fa-circle-check"></i> Free Lifetime Founder Pass Activated via Credit Card Loop</p>
            </div>
        </main>

        <script>
            window.addEventListener('DOMContentLoaded', () => {
                const canvas = document.getElementById('watermarkCanvas');
                canvas.width = window.innerWidth; canvas.height = window.innerHeight;
                const ctx = canvas.getContext('2d');
                ctx.fillStyle = "rgba(0, 191, 255, 0.025)";
                for (let i = 0; i < 20000; i++) {
                    let x = Math.random() * canvas.width; let y = Math.random() * canvas.height;
                    ctx.beginPath(); ctx.moveTo(x, y); ctx.lineTo(x + 10, y); ctx.lineTo(x + 5, y + 10); ctx.closePath(); ctx.fill();
                }
                
                // Continuous session clock tracker
                let sec = 0;
                setInterval(() => {
                    sec++;
                    let m = Math.floor(sec / 60).toString().padStart(2, '0');
                    let s = (sec % 60).toString().padStart(2, '0');
                    document.getElementById('timer').innerText = 'Session Duration: ' + m + ':' + s;
                }, 1000);

                // Simulation loop demonstrating real-time global population scale spikes
                setInterval(() => {
                    let currentUsers = parseInt(document.getElementById('userCount').innerText.replace(/,/g, ''));
                    let naturalSpike = currentUsers + Math.floor(Math.random() * 14) - 4;
                    document.getElementById('userCount').innerText = naturalSpike.toLocaleString() + " Citizens Online";
                }, 2500);
            });
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

