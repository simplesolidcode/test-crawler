from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse
from datetime import datetime

app = FastAPI()

HOST = "http://20.199.24.227"

# Project settings documentation
@app.get("/doc/project-settings", response_class=HTMLResponse)
async def project_settings():
    return """
    <html>
        <head>
            <title>Project Settings Documentation</title>
        </head>
        <body>
            <h1>Project Settings Documentation</h1>
            <p>This is a simple documentation page for project settings.</p>
            <h2>Configuration</h2>
            <ul>
                <li>Base URL: http://localhost:8000</li>
                <li>API Version: 1.0</li>
                <li>Environment: Development</li>
            </ul>
            <a href="http://20.199.24.227/doc/get-started">Get Started</a>
        </body>
    </html>
    """

# Get started documentation
@app.get("/doc/get-started", response_class=HTMLResponse)
async def get_started():
    return """
    <html>
        <head>
            <title>Getting Started with FastAPI</title>
        </head>
        <body>
            <h1>Getting Started with FastAPI</h1>
            <p>Here's a simple guide to get started with FastAPI:</p>
            <ol>
                <li>Install FastAPI: <code>pip install fastapi uvicorn</code></li>
                <li>Create a new Python file (e.g., main.py)</li>
                <li>Import FastAPI: <code>from fastapi import FastAPI</code></li>
                <li>Create an app instance: <code>app = FastAPI()</code></li>
                <li>Define routes using decorators: <code>@app.get("/")</code></li>
                <li>Run the server: <code>uvicorn main:app --reload</code></li>
            </ol>
            <a href="http://20.199.24.227/doc/project-settings">Project Settings</a>
        </body>
    </html>
    """

# Sitemap endpoint
@app.get("/sitemap.xml")
async def sitemap():
    urls = [
        f"{HOST}/doc/project-settings",
        f"{HOST}/doc/get-started",
        f"{HOST}/robots.txt"
    ]
    
    sitemap_xml = """<?xml version="1.0" encoding="UTF-8"?>
    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    """
    
    for url in urls:
        sitemap_xml += f"""
        <url>
            <loc>{url}</loc>
            <lastmod>{datetime.now().strftime('%Y-%m-%d')}</lastmod>
            <changefreq>daily</changefreq>
            <priority>0.8</priority>
        </url>
        """
    
    sitemap_xml += """
    </urlset>
    """
    
    return Response(content=sitemap_xml, media_type="application/xml")

# Robots.txt endpoint
@app.get("/robots.txt")
async def robots_txt():
    robots_txt = """User-agent: *
Allow: /
Disallow: /private/
Sitemap: /sitemap.xml
"""
    return Response(content=robots_txt, media_type="text/plain")