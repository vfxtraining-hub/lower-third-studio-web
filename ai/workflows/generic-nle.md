# Workflow — Other NLEs (after Resolve)

Same exports work everywhere that reads **PNG sequences with alpha**.

## After Effects

1. File → Import → select first frame → **PNG Sequence**  
2. Interpret Footage → FPS = job FPS  
3. Drag over plate; blending Normal  

## Final Cut Pro

1. Import image sequence (or convert to ProRes 4444 with alpha via Finder/Compressor)  
2. Place above primary storyline  

## Premiere Pro

1. Import → image sequence  
2. Interpret Footage frame rate  
3. V2+ track  

## Conversion tip (if NLE hates huge PNG seq)

```bash
# Example: folder of PNGs → ProRes 4444 with alpha (macOS + ffmpeg)
ffmpeg -framerate 24 -i 'BASE_%05d.png' -c:v prores_ks -profile:v 4444 -pix_fmt yuva444p10le out.mov
```

Then import the single MOV into any NLE.

## AI order of preference

1. Resolve (this project’s primary)  
2. AE for package polish  
3. FCP / Premiere with same media  
