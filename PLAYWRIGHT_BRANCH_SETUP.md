# Playwright Test Automation Branch Setup

This document explains how to clone and checkout the Playwright automation branch into a separate Windows directory.

## Repository

```text
https://github.com/netvarth/JaldeeUI.Automation
```

## Branch

```text
playwright-tests
```

## Target Directory

```text
F:\UI Automation\JaldeeUI.Playwright
```

---

## 1. Prerequisites

Make sure Git and Python are installed.

Check Git from PowerShell:

```powershell
git --version
```

Check Python:

```powershell
python --version
```

If Git is installed but PowerShell does not recognize it, make sure this path is added to Windows PATH:

```text
C:\Program Files\Git\cmd
```

Alternatively, use Git Bash.

---

## 2. Create the Base Directory

Open PowerShell and run:

```powershell
mkdir "F:\UI Automation" -Force
cd "F:\UI Automation"
```

---

## 3. Clone Only the Playwright Branch

Run:

```powershell
git clone --branch playwright-tests --single-branch https://github.com/netvarth/JaldeeUI.Automation.git JaldeeUI.Playwright
```

This will create the local checkout at:

```text
F:\UI Automation\JaldeeUI.Playwright
```

and checkout the `playwright-tests` branch automatically.

---

## 4. Go Into the Project Directory

```powershell
cd "F:\UI Automation\JaldeeUI.Playwright"
```

Verify the current branch:

```powershell
git branch
```

Expected output:

```text
* playwright-tests
```

---

## 5. Create Local `.env` File

The `.env` file is usually not committed to Git because it may contain login credentials or environment-specific values.

Create it from `.env.example`:

```powershell
Copy-Item ".env.example" ".env"
```

Then open `.env` and update the required values:

```powershell
notepad .env
```

---

## 6. Create and Activate Python Virtual Environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, run:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Then activate again:

```powershell
.\.venv\Scripts\Activate.ps1
```

---

## 7. Install Required Packages

Install Python dependencies from `requirements.txt`:

```powershell
pip install -r requirements.txt
```

Install the Playwright browser:

```powershell
playwright install chromium
```

---

## 8. Run Tests

```powershell
pytest
```

---

## 9. Pull Latest Changes Later

To update your local copy with the latest changes from the Playwright branch:

```powershell
cd "F:\UI Automation\JaldeeUI.Playwright"
git pull origin playwright-tests
```

---

## 10. Common Issue: Folder Already Exists

If this folder already exists:

```text
F:\UI Automation\JaldeeUI.Playwright
```

either delete it, rename it, or clone into another folder.

Example:

```powershell
git clone --branch playwright-tests --single-branch https://github.com/netvarth/JaldeeUI.Automation.git JaldeeUI.Playwright-New
```
