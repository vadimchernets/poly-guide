# Poly A2 — working material from everyday files

Use `open_formats.py` only on a file copy explicitly chosen by the person. Work locally; no account or API key is needed. Python 3 and the appropriate installed converter are required. Nothing is installed automatically. Explain the useful result, not these commands, to a non-programmer.

Start with `python3 tools/open_formats.py doctor`. Discovery is not a functional test. If a tool is missing, ask before installation or use the file capabilities of the person's existing AI. Check the source, licence, platform and permissions first. This kit does not bundle the external binaries; availability on another computer must be checked there.

Examples (replace example filenames with the person's approved copies; never overwrite originals):

```sh
python3 tools/open_formats.py pdf-text --input copies/report.pdf --output results/report.txt
python3 tools/open_formats.py scan-text --input copies/page.png --output results/page.txt --language eng
python3 tools/open_formats.py document --input copies/notes.md --output results/notes.docx
python3 tools/open_formats.py audio --input copies/recording.mp4 --output results/recording.wav
```

The output folder must already exist; output must have a new name. Files are limited to 64 MB and conversions to 60 seconds. Audio output may be much larger than compressed input: choose a short recording. An existing file is refused, including symbolic links. The tool makes no edits to the original and does not install, publish or send files. Local file parsers still process the provided content: use trusted copies and maintained converter versions.

- **PDF:** pdftotext extracts embedded text; it does not read scanned pages. Verify names, figures and reading order against the PDF. Empty output is not success.
- **Scan:** Tesseract OCR uses installed language data. `eng+rus` requires both languages to be installed. Verify names, numbers and missing text against the picture. Recognition is fallible.
- **Notes → document:** Pandoc converts Markdown/text to DOCX or HTML in sandbox mode. Raw HTML/TeX interpretation is disabled. No user filters, extra resource downloads or arbitrary commands are accepted by this wrapper. Formatting may change; inspect the output. Do not treat HTML from untrusted notes as safe to publish or execute.
- **Recording → sound:** FFmpeg keeps audio only, in WAV. Verify duration and listen to a sample. This is neither transcription nor a check of what was said.

Record tool version, environment, command outcome and an actual comparison to the source. A created file alone does not prove the content is correct. Return a usable result to the person, report any gaps, then offer one relevant next possibility.

Official references, checked 2026-11-07:
- Pandoc: https://pandoc.org/MANUAL.html
- FFmpeg: https://ffmpeg.org/ffmpeg.html
- Tesseract: https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html
- Poppler pdftotext: https://manpages.debian.org/trixie/poppler-utils/pdftotext.1.en.html
