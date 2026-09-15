---
title: "Uni Freiburg Digital Service Guide"
date: 2025-09-24
draft: false
---

# Uni Freiburg myAccount

The story begins after you receive your account credentials via email following your first immatriculation. Replace \[Username\] with the username from this account throughout this manual.

# Network

## Wifi/WLAN

In the initial email, the username is provided by the university, while the password must be set by yourself in myAccount. In the university account management portal [myAccount](https://myaccount.uni-freiburg.de/uadmin/login), you can also set the password for eduroam, the academic wireless network of the pan-European research and education networking association. The eduroam username is always \[Username\]@uni-freiburg.de.

The university provides network documentation portals: [German version WLAN an der Universität Freiburg](https://www.rz.uni-freiburg.de/de/services/netztel/wlan-vpn) and [English version WLAN at Freiburg University](https://www.rz.uni-freiburg.de/en/services/netztel-en/wlan-vpn-en?set_language=en). These pages also provide usage guidelines for non-university members.

For eduroam setup instructions, please refer to [WLAN mit eduroam](https://wiki.uni-freiburg.de/rz/doku.php?id=wlan-eduroam) and follow the steps according to your device's operating system.

**General setup within system Wi-Fi settings should contain the following:**

- Security: WPA & WPA2 Enterprise
- Authentication: PEAP
- Domain: uni-freiburg.de
- CA certificate: (None)
- \[v\] No CA certificate is required
- PEAP version: Automatic
- Inner authentication: MSCHAPv2
- Username: \[username\]@uni-freiburg.de
- Password: \[The one you set in myAccount\]

## VPN

When using university internal network services, you must connect to the campus network. Common university network services include but are not limited to: library-specific e-books and thesis databases, Web of Science paid thesis search engine, ChatGPT, etc.

When your device is connected to an external network, you can connect to the campus network via VPN.

For Windows or Mac systems, please download the corresponding version of FortiClient software following [these steps](https://wiki.uni-freiburg.de/rz/doku.php?id=vpn_fuer_windows). For Linux/Unix systems, please use `openconnect` and `network-manager-openconnect` through the network settings interface in "Settings" or via terminal. If errors occur, please verify that both packages are properly installed.

According to the Beratung Rechenzentrum der Universität Freiburg, `openconnect` and `network-manager-openconnect` work better on Linux. For Windows and Mac, download FortiClient following [these steps](https://wiki.uni-freiburg.de/rz/doku.php?id=vpn_fuer_windows) instead.

**General:**

- VPN Protocol: Fortinet SSL VPN
- Gateway: fortivpn.uni-freiburg.de
- User Agent: \[ysername\]@email.uni-freiburg.de
- CA certificate: (none)

**Software Token Authentication:**

- Token Mode: RSA SecurID -- manually entered

**Connect via login:**

- User: \[username\]@uni-freiburg.de
- Password: \[eduroam password\]

# Intranet Services

## AI/KI Service

**From 31.07.2026 onwards, \$20 limit is applied to every uni account per day.**

Externe modelle

| Anbieter  | Modell        | input | output |
|-----------|---------------|-------|--------|
| OpenAI    | GPT 5.6 Sol   | \$5   | \$30   |
|           | GPT 5.6 Terra | \$2   | \$12   |
|           | GPT 5.6 Luna  | \$0.2 | \$1.2  |
| MistralAI | Mistral Large | \$0.5 | \$1.5  |
|           | Codestral     | \$0.3 | \$0.9  |

Lokale Modelle

| Modell                                                    | input | output |
|-----------------------------------------------------------|-------|--------|
| GLM 5.2 (ufr/coding-complex)                              | \$0.4 | \$0.4  |
| Qwen 3.5 397b (ufr/reasoning-complex, ufr/vision-complex) | \$0.1 | \$0.1  |

Bei Modellen, die vom RZ auf eigener Hardware betrieben werden, wird ein fiktiver Preis gemäß der benötigten Hardware und Stromressourcen verwendet. Aktuell wird pro verwendeter GPU ein Preis von ¢0,05 verbucht (GLM 5.2 \> 8 GPUs: Input \$0,40 / Output \$0,40 pro Mio Token).

Within the university network, AI services are provided. When not connected to the university network, you must use the university-provided VPN to connect to the campus network.

The user interface provided by the university is the [OpenWebUI](https://openwebui.uni-freiburg.de/) webpage, which redirects to the university account login page upon access. General users can directly use this webpage to consult with AI.

To use this service in other tools or platforms, you can find an API key in the settings (gear icon) at the bottom left corner of the interface. This key can be used with third-party services. However, because OpenWebUI has a different account structure from standard OpenAI accounts, this key cannot be used with OpenAI's official Codex terminal service interface. For example, when using the [Continue.dev](https://marketplace.visualstudio.com/items?itemName=Continue.continue) [extension](https://marketplace.visualstudio.com/items?itemName=Continue.continue) in the VSCode text editor, or similar open-source editors like [Codium](https://open-vsx.org/extension/Continue/continue), you need to write the AI model information into the configuration file.

- URL Base URL: `https://openwebui.uni-freiburg.de/api`
- You can use the following terminal command to view the list of model names: `curl -L -v -H "Authorization: Bearer [api_key]" -H "Accept: application/json" https://openwebui.uni-freiburg.de/api/models >> openwebui.json`. This command generates an `openwebui.json` file. Open the file in a text editor and look for the `id` field in the output.

To use the [Continue.dev](https://www.continue.dev/) extension in [VSCode](https://marketplace.visualstudio.com/items?itemName=Continue.continue) or [Codium](https://open-vsx.org/extension/Continue/continue), click on the "Continue" tab on the left side of the window, then click "Configs" and "Main Config" in sequence. This will open the `config.yaml` file in the editor panel. Set the file to the following format:

``` yaml
  - name: "UFR: Standard Chat"
    provider: openai
    model: "standard-chat-ufr"
    apiBase: https://openwebui.uni-freiburg.de/api
    apiKey: sk-your-api-key-here
    roles:
      - chat
      - edit
      - apply
```

### Agent file system tools

When asking the AI agent to complete tasks in the local file system, a local MCP server is required.

Go to the setting of cotinue.dev extension side panel, navigate to "Tools", and see if there is anything under the header "MCP Servers". If not, click on the "+" sign. It creates and opens up a YAML file. Edit the file according to your environment.

``` yaml
name: New MCP server
version: 0.0.1
schema: v1

mcpServers:
  - name: filesystem
    command: npx
    args:
      - -y
      - @modelcontextprotocol/server-filesystem
      - /home/USERNAME/DIRECTORY
    env: {}
```

Type `which npx` and check if `npx` is in PATH. Or simply, copy and paste the absolute path produced by `which npx`.

Put the path of your project's directory in `/home/USERNAME/DIRECTORY`. The filesystem server can usually accept multiple directories, but if one of those folders doesn't exist, the server may fail.

Another option is to call the npx through bash commands.

``` yaml
name: New MCP server
version: 0.0.1
schema: v1

mcpServers:
  - name: filesystem
    command: /bin/bash
    args:
      - -lc
      - source /home/USERNAME/.nvm/nvm.sh && npx -y @modelcontextprotocol/server-filesystem /home/USERNAME/DIRECTORY
    env: {}
```

This explicitly loads `nvm` before running `npx`, which works better for my environment.

### Receive model names

The university or OpenAI will periodically update and rename the models used in OpenWebUI. Therefore, you must regularly update the models registered in the third-party agent (Continue.dev in this case) using [this script](../ufr_models/#update-models-with-this-python-script). This script will directly overwrite the contents of `~/.continue/config.yaml`.

First, download the Python code to your local device and open the file with a text editor. The path `~/.continue/config.yaml` written in the file is the general path for Linux systems. If you are a Windows user, change your config.yaml path. The correct path can be found by clicking on the settings of the Continue.dev extension side panel, entering "Configs", and clicking the gear icon beside "Main Config". You will now enter the config.yaml file. Right-click the tab of config.yaml and select "Open Containing Folder". You will now know the correct path to this file. Update the script with the correct path. Additionally, you must put your API key in line 10 of the script, after `OPENWEBUI_TOKEN`.

After setting up everything with the script, run the Python code in whichever way you prefer, or simply use `python3 update_models.py` in the terminal.

Please make sure your device is connected to the university network or using VPN when using the service.

**Current tested situation:**

**Models that have names starting with "UFR" work just fine, whereas models starting with "OpenAI" have handling errors in this agent. This may be caused by incompatibility between OpenAI and OpenWebUI.**

## Connecting to Your Account at the Uni Storage Server (Netzlaufwerk)

Within the university network, the university provides a Samba-based server (20GB) for you to store files. When not connected to the university network, you must use the university-provided VPN to connect to the campus network.

Uni wiki manual "Netzlaufwerk verbinden" for [Win10](https://wiki.uni-freiburg.de/rz/doku.php?id=netzlaufwerk_verbinden_windows), [Mac](http://wiki.uni-freiburg.de/rz/doku.php?id=smb_mac), and [Linux](http://wiki.uni-freiburg.de/rz/doku.php?id=smb_linux).

**In GNOME file manager in Linux, go to the "Network" tab.**

Input in the text box: `smb://[Username].files.uni-freiburg.de/home/[Username]`

A window will appear. Please enter the following information:

- Username: \[username\]@uni-freiburg.de
- Domain: PUBLIC
- Password: \[eduroam-password\]

## BwUniCluster

BwUniCluster is the general-purpose high-performance computing cluster provided by the State of Baden-Württemberg through the university network. The servers are located at Karlsruhe Institute of Technology (KIT).

Read the [manual](https://wiki.bwhpc.de/e/Main_Page) to register and use the service. There are many ways to establish a connection with the server. The following is my solution, which should work for all Linux environments.

### 1. Login with SSH

``` bash
ssh [username]@uc3.scc.kit.edu
```

Input the OTP code and your password through the prompt.

- The connection requires two-factor authentication (2FA). It uses eduMFA, but it did not register correctly on my phone, so I had to download another app, Google Authenticator, to generate an OTP code whenever I log in.

### 2. Load Modules

- Set regularly used modules to load whenever bash is called in `.bash_profile`
- e.g., C compiler **gcc** for installing some R packages, **conda** for tidyverse

**Shell script example:**

``` bash
# .bash_profile Contents
module load math/R/4.5.1
module load compiler/gnu/14.2
module load devel/miniforge/25.3.1-python-3.12
```

### 3. Upload Files to the Server with SSH Connection

- The command is: `sftp [Username]@uc3.scc.kit.edu`, input the OTP code and your password through the prompt
- Upload files from local to server: `put [local_file_path/name] [server_file_path]`
- Download files from server to local: `get [server_file_path/name] [local_file_path]`
- You cannot edit or remove files when entering the server with sftp

### 4. Submit Jobs to High Performance Computing Nodes

- The system only accepts bash scripts
- My submitting script template for R code

```bash
script.sh #!/bin/bash \# #SBATCH --partition=dev_cpu #SBATCH --job-name=myJob #SBATCH --time=00:20:00 #SBATCH --nodes=1 #SBATCH --ntasks-per-node=1 #SBATCH --cpus-per-task=16 #SBATCH --error=error.log #SBATCH --mem=32gb #SBATCH --mail-type=ALL #SBATCH --mail-user=yk112\@email.uni-freiburg.de

module load math/R/4.5.1 module load compiler/gnu/14.2 module load devel/miniforge/25.3.1-python-3.12 conda activate r_ragg_env

Rscript rcode.r 2\>&1 \| tee run.log 
```

A bash script must always indicate the location of the bash language at the start of the script `#!/bin/bash`. This path is general for all Linux environments. Then, I introduce the details of this job to the cluster queuing tool SBATCH. I ask SBATCH to bring the script to the `dev_cpu` cluster (choose the cluster according to your needs [here](https://wiki.bwhpc.de/e/BwUniCluster3.0/Running_Jobs#Regular_Queues) or check which cluster is currently idle with the command `sinfo_t_idle`).

Have in mind that when you connect to the server, you are only in the login node and not yet in the high-performance cluster. Therefore, do not run test cases directly after login. Send the test codes to nodes with "dev" in their names, such as dev_cpu or [others](https://wiki.bwhpc.de/e/BwUniCluster3.0/Running_Jobs#Development_Queues). These development nodes only allow jobs less than 30 minutes. Because of that, you won't be queuing too long as with the regular queues.

![bwUniCluster 3.0 Hardware and Architecture](https://wiki.bwhpc.de/e/File:Uc3.png)

Let's continue with the sbatch parameters. I name this job "myJob". The job name will not affect execution but will show in the notification email title. Job names will be cut off when too long. Just keep the job name simple and distinctive from other jobs you might submit at the same time.

The number of nodes depends on whether your code uses parallel computing. Since this R script is a DADA2 pipeline, it will only use one node. The `assignTaxonomy` function of DADA2 supports multi-threads in Linux. Therefore, we can use 16 CPUs (or more) in this job. If there's an error, a file `error.log` will be created in the current folder. Whenever the job starts, ends, stops, or performs any action, an email will be sent to notify me.

The script loads R version 4.5.1, C compiler, Python version 3.12, and conda environment r_ragg_env (this is the environment where I installed tidyverse). These are the modules I frequently used. Then, we can finally run the R script. When running the R script, if there is anything printed out (stdout), a text file will be created and saved as `run.log` in the current folder. The run log file will be overwritten every time this code is executed.

- Submit this bash script to SBATCH with `{bash} sbatch script.sh`
- Check your own job queue with the command `squeue`
- Copy the job number and use `scancel [job_number]` to stop the cluster from continuing to queue or execute the script

# Uni Freiburg Email Third-Party Client Setup

> 2025-09-24 發布於台灣 Freiburg 同學會 Published on 2025-09-24 at Taiwan Freiburg Student Association

Since I recently reconfigured my computer and logged into the university email through the email client again, I recalled the nightmare of the first setup. This guide is for new students' reference. Of course, you can directly go to the website email.uni-freiburg.de (the part after \@ in your email address) and log in to the university email via the webpage. However, setting it up on your computer and mobile phone is somehow troublesome.

First, you need to go to the University of Göttingen's system ([GWDG IDM portal](https://idm.gwdg.de/Account/Login?ReturnUrl=%2F)) to apply for a username and password. This system requires logging in with your university credentials, then downloading eduMFA Authenticator to your mobile phone for two-factor authentication.

Enter [GWDG IDM portal](https://idm.gwdg.de/Account/Login?ReturnUrl=%2F), choose "Anmeldung mit single sign-on", then click "Anmelden".

Log in with your university email (requires two-factor authentication).

Click on the top-right corner avatar to toggle the list. Choose the second option with a key icon.

In the left panel, choose \[DE\] APP-ZUGANGSDATEN / \[EN\] APPLICATION CREDENTIALS (requires two-factor authentication again).

Under Open-Xchange, click "ADD +" to apply for a username and password. This uid and password are used for email server setup.

In the left panel, select \[DE\] APP-ZUGANGSDATEN / \[EN\] APPLICATION CREDENTIALS. After giving this credential a name (Bezeichnung) and an expiration date (Ablaufdatum), a username and password (uid & Passwort) will be generated. There are copy buttons on the right side for each. You must open a text editor and save them immediately—you will not be able to see this credential again after leaving the page.

Additionally, please note that your university username and your name combined are two alias names for the same email account. For example, both yk112 and yu-chen.kuo are my usernames for the my university email. You can set your preferred primary email address under Information \> Primäre E-Mail-Adresse. The default is the name-based one. Perhaps only those like me, who changed their passport spelling before enrollment, would prefer to use the username-based email address.

By the way, if you need to change the name on your student ID, go directly to the international student counter on the second floor of the Registrar's Office. Show them your passport (or other supporting documents) and your current student ID to apply. After a few days, you will receive a notification to pick up your new student ID on the first floor. There is no fee, but you need to reapply for your SWFR account and Autoload—they will not be transferred automatically.

Getting back on track, now you can start setting up the login information on your device. Enter your email address on the login page of your chosen email client. The password is the one generated by the GWDG system.

- Email: \[username\]@email.uni-freiburg.de
- Password: \[password from GWDG\]

**Incoming Server:**

- Protocol: IMAP
- Hostname: email.uni-freiburg.de
- Port: 993
- Encryption: SSL/TLS
- Username: \[uid from GWDG\]

**Outgoing Server:**

- Port: 587
- Encryption: STARTTLS
- Username: \[uid from GWDG\]

Complete!