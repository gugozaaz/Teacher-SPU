#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
HTML to Landscape PDF Converter (with Reveal.js support)
Uses Playwright for pixel-perfect browser rendering and Thai font fidelity.
"""

import sys
import os
import io
import asyncio
import argparse
from pathlib import Path

# Force UTF-8
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')


async def convert_html_to_landscape_pdf(html_path: str, pdf_path: str, format_size: str = "16:10"):
    from playwright.async_api import async_playwright
    
    html_abs = os.path.abspath(html_path).replace("\\", "/")
    # Add ?print-pdf for Reveal.js compatibility
    url = f"file:///{html_abs}?print-pdf"
    
    # Determine viewport and pdf dimensions based on format_size (Base scale: 1280x800 / 1280x720)
    size_norm = format_size.upper().strip()
    if size_norm in ["16:10", "DEFAULT"]:
        v_width, v_height = 1280, 800
        pdf_params = {
            "width": "1280px",
            "height": "800px",
            "print_background": True,
            "prefer_css_page_size": True,
            "margin": {"top": "0px", "right": "0px", "bottom": "0px", "left": "0px"}
        }
    elif size_norm in ["16:9", "SCREEN"]:
        v_width, v_height = 1280, 720
        pdf_params = {
            "width": "1280px",
            "height": "720px",
            "print_background": True,
            "prefer_css_page_size": True,
            "margin": {"top": "0px", "right": "0px", "bottom": "0px", "left": "0px"}
        }
    elif size_norm == "A4":
        v_width, v_height = 1280, 905 # 297 x 210 proportion
        pdf_params = {
            "format": "A4",
            "landscape": True,
            "print_background": True,
            "prefer_css_page_size": False,
            "margin": {"top": "0px", "right": "0px", "bottom": "0px", "left": "0px"}
        }
    else:
        # Default fallback to 16:10 (1280x800)
        v_width, v_height = 1280, 800
        pdf_params = {
            "width": "1280px",
            "height": "800px",
            "print_background": True,
            "prefer_css_page_size": True,
            "margin": {"top": "0px", "right": "0px", "bottom": "0px", "left": "0px"}
        }

    print(f"Opening: {url}")
    print(f"Engine Settings: Viewport {v_width}x{v_height} (Base Scale) | Target Ratio: {format_size}")
    
    async with async_playwright() as p:
        try:
            browser = await p.chromium.launch(channel="msedge", headless=True)
        except Exception:
            try:
                browser = await p.chromium.launch(channel="chrome", headless=True)
            except Exception:
                browser = await p.chromium.launch(headless=True)

        context = await browser.new_context(
            viewport={"width": v_width, "height": v_height},
            device_scale_factor=2
        )
        page = await context.new_page()
        
        await page.goto(url, wait_until="networkidle", timeout=60000)
        
        # Wait for web fonts (Noto Sans Thai, Outfit, FontAwesome)
        await page.evaluate("() => document.fonts.ready")
        
        # Wait for Reveal.js ready state if present (with safety timeout)
        await page.evaluate("""() => {
            return new Promise((resolve) => {
                let attempts = 0;
                const check = () => {
                    attempts++;
                    const deckInstance = (window.deck && typeof window.deck.isReady === 'function') ? window.deck : null;
                    const revealInstance = (window.Reveal && typeof window.Reveal.isReady === 'function') ? window.Reveal : null;
                    const r = deckInstance || revealInstance;
                    
                    if (r && r.isReady()) {
                        resolve();
                    } else if (attempts > 50) { // Fallback after ~5s
                        console.warn('Reveal ready check timed out, proceeding anyway...');
                        resolve();
                    } else {
                        setTimeout(check, 100);
                    }
                };
                check();
            });
        }""")
        
        # Extra wait for Reveal.js layout & pagination calculations
        await asyncio.sleep(1.5)
        
        # Hide any debug overlays, toasts, or legacy controls if present
        await page.evaluate("""() => {
            const ids = ['test-report-overlay', 'aspect-ratio-toast', 'aspect-toggle'];
            ids.forEach(id => {
                const el = document.getElementById(id);
                if (el) el.style.display = 'none';
            });
            const footers = document.querySelectorAll('.deck-footer');
            footers.forEach(f => f.style.display = 'none');
        }""")
        
        # Print to Landscape PDF
        await page.pdf(path=pdf_path, **pdf_params)
            
        await browser.close()
        print(f"Successfully generated Landscape PDF ({format_size}): {pdf_path}")


def main():
    parser = argparse.ArgumentParser(description="Convert HTML/Reveal.js to Landscape PDF")
    parser.add_argument("html_file", help="Input HTML file path")
    parser.add_argument("pdf_file", help="Output PDF file path")
    parser.add_argument("--size", default="16:10", choices=["16:10", "16:9", "A4"], help="PDF format/aspect ratio (default: 16:10)")
    
    args = parser.parse_args()
    asyncio.run(convert_html_to_landscape_pdf(args.html_file, args.pdf_file, args.size))


if __name__ == "__main__":
    main()
