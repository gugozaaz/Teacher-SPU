import asyncio
import os
from playwright.async_api import async_playwright

async def run_audit():
    html_path = os.path.abspath("session/session-04/session-04-presentation.html")
    file_url = f"file:///{html_path.replace(os.sep, '/')}"

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": 1280, "height": 800})
        page = await context.new_page()

        print(f"Loading {file_url}...")
        await page.goto(file_url, wait_until="networkidle")

        # Wait for Reveal to be ready
        await page.wait_for_function("() => window.deck && window.deck.isReady()")

        # Configure 1280x800
        await page.evaluate("() => window.deck.configure({ width: 1280, height: 800, margin: 0.04 })")
        await asyncio.sleep(0.5)

        total_slides = await page.evaluate("() => window.deck.getTotalSlides()")
        print(f"Total slides found: {total_slides}")

        results = []
        all_passed = True

        for i in range(total_slides):
            await page.evaluate(f"() => window.deck.slide({i})")
            await asyncio.sleep(0.1)

            slide_info = await page.evaluate(f"""() => {{
                const sec = window.deck.getSlides()[{i}];
                const h1 = sec.querySelector('h1, h2, h3');
                const title = h1 ? h1.innerText.trim().replace(/\\n/g, ' ') : 'Slide ' + ({i}+1);
                const scrollHeight = sec.scrollHeight;
                const offsetHeight = sec.offsetHeight;
                const clientHeight = sec.clientHeight;
                return {{
                    index: {i} + 1,
                    title: title.substring(0, 45),
                    scrollHeight: scrollHeight,
                    offsetHeight: offsetHeight,
                    clientHeight: clientHeight,
                    passed: scrollHeight <= 800
                }};
            }}""")

            status = "PASS" if slide_info["passed"] else "FAIL"
            if not slide_info["passed"]:
                all_passed = False
            results.append(slide_info)
            print(f"Slide {slide_info['index']:2d}: [{status}] scrollHeight={slide_info['scrollHeight']:3d}px | {slide_info['title']}")

        passed_count = sum(1 for r in results if r["passed"])
        print("-" * 60)
        print(f"Summary: {passed_count}/{total_slides} PASS (Pass Rate: {passed_count/total_slides*100:.1f}%)")

        await browser.close()
        return all_passed

import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

if __name__ == "__main__":
    asyncio.run(run_audit())
