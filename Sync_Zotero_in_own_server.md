# Merging two (or more) Zotero in server

If you already have Zotero in your computers, the build-in Zotero sync can sometimes create fake links of attached file on your computers. That is because the build-in sync function only syncs the local file location, which means the file is not there in another computer locally to be opened. Here, I would like to guide you through how to solve this problem using any server without paying fees to sync files with the Zotero sync.

Any server type or NAS can also do the job. However, I am using the samba server provided by my university as the bidirectional backup storage of my own Zotero library between a debian linux working desktop and a fedora linux personal laptop. The server is logged-in on both computers (guideline for the uni Freiburg samba server is in [Uni-Freiburg-service.md](Uni-Freiburg-service.md).

## ⚠️ The Golden Rule of Zotero
**Never put your active Zotero database folder directly on the NAS.** 
Doing so can corrupt your library and cause you to lose your citations. Instead, we use a **"Hybrid Sync"** method:
1. **Zotero Cloud:** Syncs your citations, tags, and notes (Fast and Free).
2. **NAS Server:** Syncs your actual PDF files and large attachments (Safe and High Capacity).

# For MAC or Linux users

## Step 1: Install tools

The tools used here are all based in Linux environment, including packages of `rsync`, `ssh`, and `sshpass`. 

`rsync` is the main syncing tool. `ssh` builds a secure and fast connection with the server and `sshpass` pass the password to them so that you won't need to input the password every time. For security reasons, one can neglect the use of `sshpass` as well.

Please install them using your package manager:
- Debian-based distro such as Ubuntu runs `sudo apt install <packageName>`
- Fedora-based distro runs `sudo dnf install <packageName>`
- Arch-based distro runs `sudo pacman -i <packageName>`. There is also an ArchWiki page for `rsync` [here](https://wiki.archlinux.org/title/Rsync).
- Windows users cannot run `rsync` natively, so the best way to achieve the same result is using a tool called **FreeFileSync**. It is free, open-source, visual (GUI), and does exactly what `rsync` does but with buttons and colors.

## Step 2: check connection

Before using `sshpass`, you at least need to connect to the server with ssh once to build fingerprint. Uni-Freiburg users run `<UserID>@login.uni-freiburg.de` in the terminal. The prompt would ask for the password. Give the uni account password and press Enter. You will now enter the storage university grants you. Enter "exit" when you want to close the connection.

Now you can use sshpass. You can either directly show your password in every usage like: `sshpass <password> ssh <UserID>@login.uni-freiburg.de` or store the password in a file and link to it whenever used: `sshpass -f <passFile> ssh <UserID>@login.uni-freiburg.de`.

Alternatively, use `ssh-keygen`.
1. Generate a key in the prompt `ssh-keygen -t ed25519`
2. Copy the key to your university server `ssh-copy-id <UserID>@login.uni-freiburg.de`

Once you set this up, you can sync your Zotero files with a single command without password prompt.

## A more detailed guide for ssh key generate

### 1. What does `ed25519` mean?
`ed25519` is the **algorithm** used to create the key. Think of it as the "brand" or "style" of the lock.
*   **RSA:** The old standard. It creates very long keys and is slower.
*   **ED25519:** The modern standard. It is much smaller, faster, and more secure than RSA.

If you already have a key for GitHub, it is likely either an `id_rsa` or an `id_ed25519` key. You can use the same algorithm for your university server; it doesn't conflict with GitHub.

### 2. Will it overwrite your GitHub key?
When you run `ssh-keygen`, the program asks you:
`Enter file in which to save the key (/home/user/.ssh/id_ed25519):`

*   **If you just press ENTER:** It will try to save the key as `id_ed25519`. If you already have a key with that name for GitHub, the terminal will say: **"Overwrite (o)k / (n)o?"**
*   **IF YOU TYPE `n` (No):** It will cancel, and your GitHub key remains safe.
*   **IF YOU TYPE `o` (Yes):** It will **delete your GitHub key** and replace it with a new one. Your GitHub connection will break immediately.

### 3. The Best Practice: Create a "Named Key"
Since you are using this computer for multiple different things (GitHub, University Server, etc.), the professional way to do this is to give each key a **unique name**.

Instead of pressing Enter, give the key a specific name for the university.

**Run this command:**
```bash
ssh-keygen -t ed25519 -f ~/.ssh/id_university
```
*   `-t ed25519`: Sets the secure algorithm.
*   `-f ~/.ssh/id_university`: Tells the computer to save the key as `id_university` instead of the default `id_ed25519`.

**Now you have two separate keys:**
1. `id_ed25519` $\rightarrow$ for GitHub.
2. `id_university` $\rightarrow$ for your Zotero server.

### 4. How to use the Named Key
Because you gave the key a custom name, you need to tell the server to use it.

**Step A: Copy the new key to the server**
```bash
ssh-copy-id -i ~/.ssh/id_university.pub <UserID@login.uni-freiburg.de
```

**Step B: Tell SSH to use this key automatically**
You don't want to tell `rsync` which key to use every time. To automate this, create (or edit) a file called `config` in your `.ssh` folder:

```bash
nano ~/.ssh/config
```

**Paste this inside:**
```text
Host login.uni-freiburg.de
    HostName login.uni-freiburg.de
    User <UserID>
    IdentityFile ~/.ssh/id_university
```

### Why this is the best setup:
1. **Safety:** Your GitHub key is untouched and safe.
2. **Organization:** You know exactly which key is for which server.
3. **Simplicity:** Your `zpull` and `zpush` aliases will now work **instantly** without asking for a password, because the `config` file tells the computer: *"Whenever I connect to this university server, use the `id_university` key."*

## Step 2: pool papers from both computers into the server.

First, turn on the Zotero sync without file inside the Zotero program.

### What you are going to do:

| Step | Machine | Command | Movement | Goal |
| :--- | :--- | :--- | :--- | :--- |
| **1** | Working Desktop | `rsync` $\rightarrow$ Server | Push | Push Desktop files to Server |
| **2** | Personal Laptop | `rsync` (no delete) $\rightarrow$ Server | Push (no delete) | Add Laptop files to Server (Merge) |
| **3** | Working Desktop | `rsync` Server $\rightarrow$ Local | Pull | Get all merged files on Desktop |
| **4** | Personal Laptop | `rsync` Server $\rightarrow$ Local | Pull | Get all merged files on Laptop |

### The "Grand Merge" (One-Time Only)
You currently have PDFs on your working desktop and PDFs on your personal laptop. Some might be the same, and some might be unique to one machine. You need to bring them all together into one "Master" folder on the server.

**1. On your working desktop:**
Upload everything you have to the server.
```bash
rsync -avz --no-perms --no-owner --no-group ~/Zotero/storage/ "<serverLink>"
```
*Now the server has everything from your Desktop.*

**2. On your personal laptop:**
Upload everything you have to the server. **CRITICAL: Remove the `--delete` flag for this step.**
```bash
rsync -avz --no-perms --no-owner --no-group ~/Zotero/storage/ "<serverLink>"
```
*By removing `--delete`, `rsync` will simply add the files from your laptop to the server without deleting the files you just uploaded from the desktop. Now the server is the "Master" containing all PDFs from both machines.*

---

### Synchronize Local Folders to the Master
Now that the server has every file from both machines, you need to make sure your local folders match that master list.

**1. On your working desktop:**
Pull everything from the server. (Put `--delete` back in to remove any duplicates/old versions).
```bash
rsync -avz --no-perms --no-owner --no-group --delete "<serverLink>" ~/Zotero/storage/
```

**2. On your personal laptop:**
Pull everything from the server.
```bash
rsync -avz --no-perms --no-owner --no-group --delete "<serverLink>" ~/Zotero/storage/
```

---

### Maintain the "Common" State
Now that you are integrated, you simply follow the daily routine we discussed previously. 

**The Workflow moving forward:**
1. **Start of Session:** Always `rsync` **FROM** Server $\rightarrow$ **TO** Local.
2. **End of Session:** Always `rsync` **FROM** Local $\rightarrow$ **TO** Server.

### Why this works:
*   **Database:** Zotero's built-in sync handles the "integration" of the citations. If you added a book on one machine, Zotero Cloud tells the other machine "Here is a new book," and it creates a folder in `~/Zotero/storage/` with a random ID (e.g., `ABC1234`).
*   **Files:** When you `rsync` from the server, the PDF inside `ABC1234` is downloaded to your local machine. Zotero then sees the file is there and the link is restored.


# Write the command as an alias in .zshrc for future usage

Use ssh connection instead of SMB and mounting. The ssh link to Netzlaufwerk is [userID]@login.uni-freiburg.de

Then, input your uni account password to the prompt. 

**Recommended Aliases for your `.zshrc` or `.bashrc`:**
```bash
# Sync FROM Server TO Local (Start of session)
alias zpull='rsync -avz --no-perms --no-owner --no-group --delete user@server:/home/user/storage/ ~/Zotero/storage/'

# Sync FROM Local TO Server (End of session)
alias zpush='rsync -avz --no-perms --no-owner --no-group --delete ~/Zotero/storage/ user@server:/home/user/storage/'
```


# For Windows users

## Part 1: Zotero Setup (Do this on ALL computers)
Before syncing files, ensure Zotero is configured to handle the database in the cloud and the files locally.

1. Open Zotero $\rightarrow$ **Edit** $\rightarrow$ **Preferences** $\rightarrow$ **Sync**.
2. Create a free Zotero account and log in.
3. Under **File Syncing**, ensure that **"Sync attachment files in My Library"** is **UNCHECKED**. 
   * *(Why? We are using the NAS for files to save cloud space and increase speed.)*

---

## Part 2: Setting up the File Sync (Windows Users)
Since Windows doesn't have `rsync`, we use **FreeFileSync**, a free visual tool.

### 1. Installation
* Download and install **FreeFileSync** from [freefilesync.org](https://freefilesync.org/).

### 2. Create your Sync Task
1. **Connect to the NAS:** Open your File Explorer and map the Institute NAS drive to your computer (e.g., the `Z:` drive).
2. **Open FreeFileSync** and click the **New** icon.
3. **Left Side (Local):** Click **Browse** and select your Zotero storage folder. 
   * Path: `C:\Users\[YourName]\Zotero\storage`
4. **Right Side (NAS):** Click **Browse** and select the folder on the NAS where you want to store your papers.
   * Path: `Z:\YourUsername\Zotero_storage`
5. **Comparison Settings:** Click the blue gear icon $\rightarrow$ Select **"Two-Way"** (if you edit files on both machines) or **"Mirror"** (if the NAS is just a backup).

### 3. The "Sync Cycle" (The Routine)
To avoid conflicts, follow this simple habit:

*   **$\rightarrow$ When you START working:** Open FreeFileSync $\rightarrow$ Click **Compare** $\rightarrow$ Click **Synchronize**. (This pulls new papers from the NAS to your laptop).
*   **$\leftarrow$ When you FINISH working:** Open FreeFileSync $\rightarrow$ Click **Compare** $\rightarrow$ Click **Synchronize**. (This pushes your new papers to the NAS).


## 🚀 Quick Summary Table

| Task | Method | Frequency | Goal |
| :--- | :--- | :--- | :--- |
| **Citations/Notes** | Zotero Cloud | Automatic | Keeps library structure identical. |
| **PDFs/Files** | FreeFileSync / rsync | Start & End of day | Syncs heavy files via the NAS. |
| **NAS Access** | Mapped Drive / SSH | Once | Connection to Institute storage. |
