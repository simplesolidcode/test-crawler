from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse
import streamlit as st
import uvicorn
from datetime import datetime
import os

app = FastAPI()

# Project settings documentation
@app.get("/doc/project-settings", response_class=HTMLResponse)
async def project_settings():
    return """
    <html>
        <head>
            <title>Project Settings Documentation</title>
        </head>
        <body>
            <h1>Project Settings</h1>
            <p>This is a simple documentation page for project settings.</p>
            <h2>Configuration</h2>
            <ul>
                <li>Base URL: http://localhost:8000</li>
                <li>API Version: 1.0</li>
                <li>Environment: Development</li>
            </ul>
        </body>
    </html>
    """

# Get started documentation
@app.get("/doc/get-started", response_class=HTMLResponse)
async def get_started():
    return """
    <html>
        <head>
            <title>Get Started with FastAPI</title>
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
        </body>
    </html>
    """

# Sitemap endpoint
@app.get("/sitemap.xml")
async def sitemap():
    urls = [
        "/doc/project-settings",
        "/doc/get-started",
        "/robots.txt"
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

# Streamlit interface
def main():
    st.title("CursorAI Crawler Interface")
    
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Documentation", "Sitemap", "Robots.txt"])
    
    if page == "Home":
        st.header("Welcome to CursorAI Crawler")
        st.write("This is a simple interface for managing the CursorAI crawler.")
        
    elif page == "Documentation":
        st.header("Documentation")
        st.write("Available documentation pages:")
        st.markdown("- [Project Settings](/doc/project-settings)")
        st.markdown("- [Get Started](/doc/get-started)")
        
    elif page == "Sitemap":
        st.header("Sitemap")
        st.write("View the sitemap at: [Sitemap XML](/sitemap.xml)")
        
    elif page == "Robots.txt":
        st.header("Robots.txt")
        st.write("View the robots.txt at: [Robots.txt](/robots.txt)")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)