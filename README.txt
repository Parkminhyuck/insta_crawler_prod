## insta_crawler_auto - Production Package

1. Activate virtual environment:
   ```
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

2. Install dependencies:
   ```
   install_deps.bat
   ```

3. Run full pipeline:
   ```
   run_all.bat
   ```

All logs & reports are stored in the `logs/` directory.
4. Quick health check:
   ```
   powershell -ExecutionPolicy Bypass -File check.ps1
   ```
