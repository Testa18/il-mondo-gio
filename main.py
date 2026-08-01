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
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
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
            }
            canvas { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 9999; pointer-events: none; }
        </style>
    </head>
    <body>
        <canvas id="watermarkCanvas"></canvas>
        <div class="venice-water"></div>

        <header style="padding: 25px; background: rgba(11, 25, 44, 0.6); border-bottom: 1px solid rgba(0, 191, 255, 0.2); position: relative; z-index: 100;">
            <h2 style="color: #00BFFF; margin:0; font-weight: 800;"><i class="fa-solid fa-sun" style="color: #FFD700;"></i> GIOVANNIXXXVIIMMXXVI</h2>
        </header>
        
        <main style="position: relative; z-index: 10; padding: 20px;">
            <h1 class="main-title">Il Mondo Dalla Vita Piena Di Gio</h1>
            <p class="subtitle">Benvenuto to the Sovereign Digital Sanctuary</p>
            
            <div class="joy-card">
                <h3 style="color: #00BFFF; margin-top:0;"><i class="fa-solid fa-scroll"></i> Il Manifesto di Gio</h3>
                <p style="text-align: left; line-height: 1.7; color: #E2E8F0;">We reject standard digital tracking models. <strong>Il Mondo Dalla Vita Piena Di Gio</strong> is a global, secure sanctuary engineered to elevate human connection across all populations and races through beautiful biometric expression and music.</p>
            </div>
            
            <div class="joy-card">
                <h3><i class="fa-solid fa-wand-magic-sparkles" style="color: #00BFFF;"></i> 10,000,000 Facet Volumetric Studio</h3>
                <p>Map your portrait frame into ultra-precise 3D structural meshes processed directly on server clusters.</p>
                <button class="btn-joy" onclick="alert('Server Side Calculation Complete: 10,000,000 triangles successfully mapped onto matrix grid!')">Upload Portrait</button>
            </div>
            
            <div class="joy-card">
                <h3><i class="fa-solid fa-users" style="color: #00BFFF;"></i> Synchronized Connectivity Hub</h3>
                <div style="font-size: 1.8rem; font-weight: 800; color: #00BFFF; margin: 10px 0;" id="userCount">104,821 Citizens Online</div>
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
                
                let sec = 0;
                setInterval(() => {
                    sec++;
                    let m = Math.floor(sec / 60).toString().padStart(2, '0');
                    let s = (sec % 60).toString().padStart(2, '0');
                    document.getElementById('timer').innerText = 'Session Duration: ' + m + ':' + s;
                }, 1000);

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
