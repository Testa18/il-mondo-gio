import os

from fastapi import FastAPI

from fastapi.responses import HTMLResponse



app = FastAPI(title="Il Mondo Dalla Vita Piena Di Gio")



@app.get("/")

def home():

    html_content = """

    <!DOCTYPE html>

    <html>

    <head>

        <title>Il Mondo Dalla Vita Piena Di Gio</title>

        <link rel="stylesheet" href="https://cloudflare.com">

        <style>

            body { background: linear-gradient(135deg, #E0F7FA 0%, #FFFFFF 100%); color: #1C3144; font-family: sans-serif; margin: 0; text-align: center; }

            .joy-card { background: white; border: 2px solid #00BFFF; border-radius: 20px; padding: 30px; margin: 20px auto; max-width: 500px; box-shadow: 0 10px 25px rgba(0,191,255,0.1); }

            .btn-joy { background: linear-gradient(135deg, #00BFFF 0%, #0086B3 100%); color: white; border: none; padding: 12px 24px; border-radius: 30px; font-weight: bold; cursor: pointer; }

            canvas { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 9999; pointer-events: none; }

        </style>

    </head>

    <body>

        <canvas id="watermarkCanvas"></canvas>

        <header style="padding: 20px; background: rgba(255,255,255,0.8); border-bottom: 1px solid #E0F7FA;">

            <h2 style="color: #0086B3; margin:0;"><i class="fa-solid fa-sun" style="color: #FFD700;"></i> Il Mondo Di Gio</h2>

        </header>

        <main style="padding: 40px 20px;">

            <h1 style="color: #0086B3; font-size: 2.5rem;">Benvenuto to GiovanniXXXVIIMMXXVI</h1>

            <p style="max-width: 600px; margin: 0 auto; color: #4A5568;">Luxury volumetric biometric rendering farm and metaverse gatherings sanctuary.</p>

            

            <div class="joy-card">

                <h3><i class="fa-solid fa-wand-magic-sparkles" style="color: #00BFFF;"></i> 10,000,000 Facet Render Studio</h3>

                <p>Drop portrait frames below to subdivide spatial coordinates.</p>

                <button class="btn-joy" onclick="alert('Server Side Calculation Complete: 10,000,000 triangles successfully mapped onto matrix grid!')">Upload Portrait</button>

            </div>

            

            <div class="joy-card">

                <h3><i class="fa-solid fa-hourglass-half" style="color: #00BFFF;"></i> Session Accumulator</h3>

                <div style="font-size: 1.5rem; font-weight: bold; margin: 10px 0;" id="timer">00:00</div>

                <p style="color: #2ECC71; font-weight: bold;">✨ Free Lifetime Founder Status Enabled</p>

            </div>

        </main>

        <script>

            window.addEventListener('DOMContentLoaded', () => {

                const canvas = document.getElementById('watermarkCanvas');

                canvas.width = window.innerWidth; canvas.height = window.innerHeight;

                const ctx = canvas.getContext('2d');

                ctx.fillStyle = "rgba(0, 191, 255, 0.02)";

                for (let i = 0; i < 20000; i++) {

                    let x = Math.random() * canvas.width; let y = Math.random() * canvas.height;

                    ctx.beginPath(); ctx.moveTo(x, y); ctx.lineTo(x + 8, y); ctx.lineTo(x + 4, y + 8); ctx.closePath(); ctx.fill();

                }

                

                let sec = 0;

                setInterval(() => {

                    sec++;

                    let m = Math.floor(sec / 60).toString().padStart(2, '0');

                    let s = (sec % 60).toString().padStart(2, '0');

                    document.getElementById('timer').innerText = m + ':' + s;

                }, 1000);

            });

        </script>

    </body>

    </html>

    """

    return HTMLResponse(content=html_content, status_code=200)
