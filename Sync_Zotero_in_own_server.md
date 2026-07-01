


---

# Merging two (or more) computer's Zotero together

If you already have Zotero in your computers, the build-in Zotero sync can sometimes create fake links of attached file on your computers. That is because the build-in sync function only syncs the local file location, which means the file is not there in another computer locally to be opened. Here, I would like to guide you through how to solve this problem using any server without paying fees to sync files with the Zotero sync.

Any server type or NAS can also do the job. However, I am using the samba server provided by my university as the bidirectional backup storage of my own Zotero library between a debian linux working desktop and a fedora linux personal laptop. The server is logged-in on both computers (guideline for the uni Freiburg samba server is in [Uni-Freiburg-service.md](Uni-Freiburg-service.md).

## Step 1: Install tools

The tools used here are all based in Linux environment, including packages of `rsync`, `ssh`, and `sshpass`. 

`rsync` is the main syncing tool. `ssh` builds a secure and fast connection with the server and `sshpass` pass the password to them so that you won't need to input the password every time. For security reasons, one can neglect the use of `sshpass` as well.

Please install them using your package manager:
- Debian-based distro such as Ubuntu runs `sudo apt install <packageName>`
- Fedora-based distro runs `sudo dnf install <packageName>`
- Arch-based distro runs `sudo pacman -i <packageName>`. There is also an ArchWiki page for `rsync` [here](https://wiki.archlinux.org/title/Rsync).
- Windows user might need to search through sync packages or use WSL to work like a linux distro.

## Step 2: check connection

Before using `sshpass`, you at least need to connect to the server with ssh once to build fingerprint. Uni-Freiburg users run `<UserID>@login.uni-freiburg.de` in the terminal. The prompt would ask for the password. Give the uni account password and press Enter. You will now enter the storage university grants you. Enter "exit" when you want to close the connection.

Now you can use sshpass. You can either directly show your password in every usage like: `sshpass <password> ssh <UserID>@login.uni-freiburg.de` or store the password in a file and link to it whenever used: `sshpass -f <passFile> ssh <UserID>@login.uni-freiburg.de`.

Alternatively, use `ssh-keygen`.
1. Generate a key in the prompt `ssh-keygen -t ed25519`
2. Copy the key to your university server `ssh-copy-id yk112@login.uni-freiburg.de`

Once you set this up, you can sync your Zotero files with a single command without password prompt.

## Step 2: pool papers from both computers into the server.

First, turn on the Zotero sync without file inside the Zotero program.

---

Since you are already using **Zotero's built-in sync for the database**, your metadata (titles, authors, tags) is already being handled by Zotero's cloud. The only thing "split" between your two machines right now is the **`storage` folder** (the actual PDFs).

To integrate them into one common library on your server, you need to perform a **one-time merge** to ensure no files are lost, and then start the `rsync` cycle.

### Step 1: The "Grand Merge" (One-Time Only)
You currently have PDFs on your Debian machine and PDFs on your Fedora machine. Some might be the same, and some might be unique to one machine. You need to bring them all together into one "Master" folder on the server.

**1. On your Debian Desktop:**
Upload everything you have to the server.
```bash
rsync -av --no-perms --no-owner --no-group ~/Zotero/storage/ "/run/user/1001/gvfs/smb-share:server=yk112.files.uni-freiburg.de,share=home/yk112/storage/"
```
*Now the server has everything from your Desktop.*

**2. On your Fedora Laptop:**
Upload everything you have to the server. **CRITICAL: Remove the `--delete` flag for this step.**
```bash
rsync -av --no-perms --no-owner --no-group ~/Zotero/storage/ "/run/user/1001/gvfs/smb-share:server=yk112.files.uni-freiburg.de,share=home/yk112/storage/"
```
*By removing `--delete`, `rsync` will simply add the files from your laptop to the server without deleting the files you just uploaded from the desktop. Now the server is the "Master" containing all PDFs from both machines.*

---

### Step 2: Synchronize Local Folders to the Master
Now that the server has every file from both machines, you need to make sure your local folders match that master list.

**1. On Debian Desktop:**
Pull everything from the server. (Put `--delete` back in to remove any duplicates/old versions).
```bash
rsync -av --no-perms --no-owner --no-group --delete "/run/user/1001/gvfs/smb-share:server=yk112.files.uni-freiburg.de,share=home/yk112/storage/" ~/Zotero/storage/
```

**2. On Fedora Laptop:**
Pull everything from the server.
```bash
rsync -av --no-perms --no-owner --no-group --delete "/run/user/1001/gvfs/smb-share:server=yk112.files.uni-freiburg.de,share=home/yk112/storage/" ~/Zotero/storage/
```

---

### Step 3: Maintain the "Common" State
Now that you are integrated, you simply follow the daily routine we discussed previously. 

**The Workflow moving forward:**
1. **Start of Session:** Always `rsync` **FROM** Server $\rightarrow$ **TO** Local.
2. **End of Session:** Always `rsync` **FROM** Local $\rightarrow$ **TO** Server.

### Why this works:
*   **Database:** Zotero's built-in sync handles the "integration" of the citations. If you added a book on Fedora, Zotero Cloud tells Debian "Here is a new book," and it creates a folder in `~/Zotero/storage/` with a random ID (e.g., `ABC1234`).
*   **Files:** When you `rsync` from the server, the PDF inside `ABC1234` is downloaded to your local machine. Zotero then sees the file is there and the link is restored.

### Summary of the Integration Process
| Step | Machine | Command | Goal |
| :--- | :--- | :--- | :--- |
| **1** | Debian | `rsync` $\rightarrow$ Server | Push Desktop files to Server |
| **2** | Fedora | `rsync` (no delete) $\rightarrow$ Server | Add Laptop files to Server (Merge) |
| **3** | Debian | `rsync` Server $\rightarrow$ Local | Get all merged files on Desktop |
| **4** | Fedora | `rsync` Server $\rightarrow$ Local | Get all merged files on Laptop |

# Write the command as an alias in .zshrc for future usage

Use ssh connection instead of SMB and mounting. The ssh link to Netzlaufwerk is [userID]@login.uni-freiburg.de

Then, input your uni account password to the prompt. 

```zsh
# Zotero Storage Sync Aliases
# Use these to sync PDF attachments via the SMB server
# Replace the path below if the server ID (1001) changes on your laptop

# PUSH: Local Zotero storage TO the SMB Server
alias zpush='sshpass -f ".mypass" rsync -avz --progress --no-perms --no-owner --no-group --delete ~/Zotero/storage/ yk112@login.uni-freiburg.de:/home/yk112/Zotero_storage/'

# PULL: SMB Server TO Local Zotero storage
alias zpull='sshpass -f ".mypass" rsync -avz --progress --no-perms --no-owner --no-group --delete yk112@login.uni-freiburg.de:/home/yk112/Zotero_storage/ ~/Zotero/storage/'
```
