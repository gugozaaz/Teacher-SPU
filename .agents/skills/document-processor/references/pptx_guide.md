# PowerPoint (.pptx) Reference Guide

## Essential Python Snippets

### 1. Extracting slides, titles, shapes, and speaker notes
```python
from pptx import Presentation

prs = Presentation("presentation.pptx")
for idx, slide in enumerate(prs.slides, start=1):
    title = slide.shapes.title.text if slide.shapes.title else "No Title"
    print(f"Slide {idx}: {title}")
    
    for shape in slide.shapes:
        if shape.has_text_frame and shape != slide.shapes.title:
            for p in shape.text_frame.paragraphs:
                if p.text.strip():
                    print(f"  - {p.text.strip()}")
```

### 2. Creating modern 16:9 widescreen slides
```python
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

blank_layout = prs.slide_layouts[6]
slide = prs.slides.add_slide(blank_layout)

# Add text box
txBox = slide.shapes.add_textbox(Inches(1), Inches(1), Inches(11.333), Inches(2))
tf = txBox.text_frame
p = tf.paragraphs[0]
p.text = "Modern Slide Title"
p.font.size = Pt(40)
p.font.bold = True
p.font.color.rgb = RGBColor(0x38, 0xBD, 0xF8)

prs.save("modern_presentation.pptx")
```
