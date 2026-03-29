# SQL Injection Demo - Vulnerable vs. Secure Login

![Type](https://img.shields.io/badge/Type-Security%20Demo-red)
![No Backend](https://img.shields.io/badge/Backend-None%20Required-brightgreen)
![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Ready-blue)
![Status](https://img.shields.io/badge/Status-Complete-success)

## What is SQL Injection?

SQL Injection is one of the most common and dangerous web application vulnerabilities. It occurs when user input is inserted directly into a SQL query string without proper sanitization. An attacker can manipulate the query logic to bypass authentication, extract data, or even destroy entire databases.

It has been listed in the **OWASP Top 10** for over two decades and remains a leading cause of data breaches worldwide.

## What This Demo Shows

This is an interactive, browser-based demonstration that lets you **see and feel** how SQL injection works - and how one simple fix (parameterized queries) stops it completely.

The page displays two login forms side by side:

| Left Side | Right Side |
|-----------|------------|
| **Vulnerable Login** | **Secure Login** |
| Builds SQL query using string formatting | Uses parameterized query (? placeholders) |
| Injection payload bypasses authentication | Same payload is rejected |
| Returns all 5 users from the database | Returns 0 rows - no match found |
| Attacker gains admin access | Login fails as expected |

### The Attack Payload

```
Username: ' OR '1'='1' --
Password: anything
```

### What Happens - Vulnerable Side

The input is concatenated directly into the SQL string:

```sql
SELECT * FROM users WHERE username = '' OR '1'='1' --' AND password = 'anything'
```

- `' OR '1'='1'` - always evaluates to TRUE, matching every row
- `--` comments out the rest of the query (the password check)
- Result: all 5 users returned, attacker logs in as admin

### What Happens - Secure Side

The input is passed as a parameter - the database treats it as literal data:

```sql
SELECT * FROM users WHERE username = ? AND password = ?
-- Parameters: ["' OR '1'='1' --", "anything"]
```

- The database searches for a user literally named `' OR '1'='1' --`
- No such user exists
- Result: 0 rows, login rejected

## Live Demo

**Open `index.html` in any browser. No server, no installation, no dependencies.**

## Features

- **Side-by-side comparison** - vulnerable vs. secure login on the same screen
- **Quick-fill buttons** - valid credentials, wrong password, and injection payload
- **Run Both Sides** - single button that injects the payload into both forms simultaneously
- **Query animation** - the SQL query types out character by character with syntax highlighting
- **Injection highlighting** - the injected portion is underlined in red
- **Query diff view** - after sync attack, shows both queries side by side with annotations
- **Dashboard overlay** - successful login opens a simulated internal dashboard
- **Educational section** - code examples explaining vulnerable vs. secure approaches
- **Responsive design** - works on desktop and mobile

## Simulated Database

The demo includes 5 test users stored in JavaScript (simulating a real database):

| Username | Password | Role |
|----------|----------|------|
| admin | Secret123 | admin |
| maya_ben_ari | MayaBen98! | user |
| omer4 | Omer_HOME1111 | analyst |
| daniel.peretz | DanielKing7 | user |
| nina.sh | NinaOffice012026 | manager |

## How to Use

1. **Open `index.html`** in any modern browser
2. **Try a valid login** - click "maya_ben_ari" on the left, then "Attempt Login"
3. **Try a wrong password** - click "wrong pass", then "Attempt Login"
4. **Try the injection** - click "inject" on the left, then "Attempt Login" - you get in
5. **Try the same injection on the right** - click "inject", then "Attempt Login" - blocked
6. **Or click "Run Both Sides Simultaneously"** to see the full comparison in one click

## File Structure

```
sql-injection-demo/
  index.html     <- The entire demo (HTML + CSS + JS, single file)
  README.md      <- This file
```

That's it. One HTML file, zero dependencies.

## Why This Matters

SQL injection is not a theoretical risk. Real-world examples include:

- **2017 Equifax breach** - 147 million records exposed
- **2015 TalkTalk breach** - 157,000 customer records stolen
- **2008 Heartland Payment Systems** - 134 million credit cards compromised

The fix is simple: **never concatenate user input into SQL strings**. Use parameterized queries (prepared statements) instead. Every modern database and framework supports them.

## Tech Stack

- HTML5 / CSS3 / Vanilla JavaScript
- Zero external dependencies
- No backend required
- Works offline

## Limitations

This is an educational demo, not a real application:

- The "database" is a JavaScript array (no actual SQL engine)
- Passwords are stored in plain text (the focus is on injection, not password security)
- The vulnerable query simulation is simplified to demonstrate the concept
- No session management, rate limiting, or other production security features

## Author

**Nevo Ben Ami** - Security Analyst

---

## How to Upload to GitHub and Enable GitHub Pages

### Step 1 - Create a GitHub Account (if you don't have one)

Go to [github.com](https://github.com) and sign up.

### Step 2 - Create a New Repository

1. Click the **+** icon in the top-right corner
2. Click **New repository**
3. Fill in:
   - **Repository name:** `sql-injection-demo`
   - **Description:** `Interactive SQL Injection Demo - Vulnerable vs. Secure Login`
   - **Visibility:** Public
4. Do **NOT** check "Add a README file" (we already have one)
5. Click **Create repository**

### Step 3 - Upload the Files

1. On the new repository page, click the blue link **uploading an existing file**
2. Drag both files into the upload area:
   - `index.html`
   - `README.md`
3. In the "Commit changes" box, type: `Initial commit - SQL Injection Demo`
4. Click **Commit changes**

### Step 4 - Enable GitHub Pages

1. Go to your repository page
2. Click **Settings** (tab at the top)
3. In the left sidebar, click **Pages**
4. Under "Source", select **Deploy from a branch**
5. Under "Branch", select **main** and **/ (root)**
6. Click **Save**
7. Wait 1-2 minutes

### Step 5 - Access Your Live Demo

Your demo will be available at:

```
https://YOUR-USERNAME.github.io/sql-injection-demo/
```

Replace `YOUR-USERNAME` with your actual GitHub username.

You can now share this link in your resume, LinkedIn, or portfolio.
