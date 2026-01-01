# UI Automation (UIA) – Windows Environment Setup

This document explains how to set up the **UI Automation** environment on **Windows**, including Python, GitHub access, Java 21, and Allure Reports.

---

## 1. Prerequisites

### 1.1 Install Python

1. Download Python from:
   [https://www.python.org/](https://www.python.org/)
2. During installation, ensure:
   ✅ **Add Python to PATH**

### 1.2 Verify Python Installation

Open **PowerShell**:

```powershell
python --version
pip --version
```

---

## 2. Clone Project from GitHub using VS Code

### 2.1 Install Git

1. Download Git:
   [https://git-scm.com/download/win](https://git-scm.com/download/win)
2. Install with default options

Verify:

```powershell
git --version
```

---

### 2.2 Install Visual Studio Code

1. Download:
   [https://code.visualstudio.com/](https://code.visualstudio.com/)
2. Enable during install:

   * Add to PATH
   * Open with Code (context menu)

---

### 2.3 Sign in to GitHub in VS Code

1. Open **VS Code**
2. Press `Ctrl + Shift + P`
3. Select:

```text
GitHub: Sign in
```

4. Complete browser authentication

---

### 2.4 Clone the Repository

1. Press `Ctrl + Shift + P`
2. Select:

```text
Git: Clone
```

3. Paste repository URL
4. Choose workspace folder (example):

```text
E:\UI Workspace
```

5. Open the cloned project

---

## 3. Create Python Virtual Environment

### 3.1 Navigate to Project Folder

```powershell
cd "E:\UI Workspace\<project-folder>"
```

### 3.2 Create Virtual Environment

```powershell
python -m venv venv
```

---

## 4. Activate Virtual Environment (Windows)

```powershell
.\venv\Scripts\Activate.ps1
```

You should see `(venv)` in the prompt.

### Fix Execution Policy (If Required)

Run **PowerShell as Administrator**:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Restart PowerShell and activate again.

---

## 5. Install Python Dependencies

### 5.1 Upgrade pip

```powershell
python -m pip install --upgrade pip
```

### 5.2 Install Requirements

```powershell
pip install -r requirements.txt
```

---

## 6. Fix C++ Build Tools Error (If Required)

### Error

```text
Microsoft Visual C++ 14.0 or greater is required
```

### Solution

1. Download:
   [https://visualstudio.microsoft.com/visual-cpp-build-tools/](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
2. Select:

   * Desktop development with C++
3. Ensure:

   * MSVC v14.x build tools
   * Windows 10/11 SDK
4. Install and restart PowerShell
5. Re-run:

```powershell
pip install -r requirements.txt
```

---

## 7. Install Java 21 (Required)

### 7.1 Download Java 21 (LTS)

1. Download from:
   [https://adoptium.net/](https://adoptium.net/)
2. Select:

   * Version: **21 (LTS)**
   * Package: **JDK**
   * OS: **Windows**
3. Install with defaults

---

### 7.2 Set JAVA_HOME

Add **System Variable**:

```text
JAVA_HOME = C:\Program Files\Eclipse Adoptium\jdk-21
```

Add to **Path**:

```text
%JAVA_HOME%\bin
```

Restart PowerShell.

---

### 7.3 Verify Java

```powershell
java -version
javac -version
```

---

## 8. Install Allure Reports (Choose ONE Method)

---

### Option A: Install Allure using Scoop (Recommended)

#### 8A.1 Install Scoop

Open **PowerShell as Administrator**:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
irm get.scoop.sh | iex
```

Restart PowerShell.

---

#### 8A.2 Install Allure

```powershell
scoop install allure
```

Verify:

```powershell
allure --version
```

---

### Option B: Install Allure Manually (From Source)

Use this method if Scoop is not allowed or blocked.

#### 8B.1 Download Allure

1. Go to:
   [https://github.com/allure-framework/allure2/releases](https://github.com/allure-framework/allure2/releases)
2. Download the latest `allure-*-zip`

---

#### 8B.2 Extract Allure

Extract to a permanent location, for example:

```text
C:\allure
```

Folder structure:

```text
C:\allure
 ├── bin
 ├── config
 └── lib
```

---

#### 8B.3 Set ALLURE_HOME

Add **System Variable**:

```text
ALLURE_HOME = C:\allure
```

Add to **Path**:

```text
%ALLURE_HOME%\bin
```

Restart PowerShell.

---

#### 8B.4 Verify Installation

```powershell
allure --version
```

---

## 9. Generate & View Allure Report

After test execution creates `allure-results`:

```powershell
allure serve allure-results
```

---

## 10. Recommended VS Code Extensions

* Python
* Pylance
* GitHub Pull Requests and Issues
* Java Extension Pack
* Test Explorer UI

---

## 11. Setup Complete

Your **UI Automation (UIA)** environment on Windows is now ready.

---

---

## ⚠️ Important Note: Microsoft Store Python (Read This)

When Python is **not installed** and you run:

```powershell
python --version
```

Windows may suggest installing Python from the **Microsoft Store**.
While this works, **it is NOT recommended for this project**.

### Why Not?

* Installed inside a Windows App sandbox
* Unpredictable paths
* Problems with:

  * `venv`
  * Native dependencies
  * Build tools
  * CI and automation scripts
* Harder to manage Python versions

### Recommendation

🚫 **Do NOT use Microsoft Store Python for UI Automation**

✅ **Always install Python directly from python.org**

---

### If Python Was Installed from Microsoft Store

To avoid conflicts:

1. Open **Settings → Apps → Installed apps**
2. Uninstall **Python (Microsoft Store)**
3. Install Python from:
   [https://www.python.org/](https://www.python.org/)
4. Ensure during install:
   ✅ Add Python to PATH
5. Restart PowerShell
6. Verify:

```powershell
where python
python --version
```

Expected path example:

```text
C:\Users\<user>\AppData\Local\Programs\Python\Python3x\
```

---

### Final Word

Microsoft Store Python is fine for quick experiments.
For **UI Automation, test stability, and CI**, use the official Python installer.

---

