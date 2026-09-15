---
title: "Uni Freiburg Digital Service Guide"
date: 2025-09-24
draft: false
---

# 帳號設定 Uni Freiburg myAccount

在完成首次註冊後，你會收到學校寄來的帳號密碼通知信，故事從這裡開始。以下將你收到的帳號（英文與數字組合）以 \[你的帳號\] 或 \[Username\] 表示。

# 網路 Network

## 無線網路設定 Wifi/WLAN

在最初收到的信件中，帳號由學校提供，密碼則需進入 myAccount 自行設定。在學校的帳號管理網站 [myAccount](https://myaccount.uni-freiburg.de/uadmin/login) 中，你也可以設定泛歐洲科研與教育網路協會的學術無線網路 eduroam 的密碼。eduroam 的帳號固定為 \[你的帳號\]@uni-freiburg.de。

學校提供的網路說明文件入口網站：[德文版 WLAN an der Universität Freiburg](https://www.rz.uni-freiburg.de/de/services/netztel/wlan-vpn) 與 [英文版 WLAN at Freiburg University](https://www.rz.uni-freiburg.de/en/services/netztel-en/wlan-vpn-en?set_language=en)。該頁面也提供非大學成員的訪問使用指引。

關於 eduroam 的設定說明文件 [WLAN mit eduroam](https://wiki.uni-freiburg.de/rz/doku.php?id=wlan-eduroam)，請依照你的設備系統類型參考相應步驟進行設定。

**一般系統 Wi-Fi 設定應包含以下內容：**

**General setup within system Wi-Fi settings should contain the following:**

- 安全性 Security: WPA & WPA2 Enterprise
- 認證方式 Authentication: PEAP
- 網域 Domain: uni-freiburg.de
- CA 憑證 CA certificate: (無 None)
- \[v\] 不需要 CA 憑證 No CA certificate is required
- PEAP 版本 PEAP version: 自動 Automatic
- 內部認證 Inner authentication: MSCHAPv2
- 使用者名稱 Username: \[你的帳號\]@uni-freiburg.de
- 密碼 Password: \[你在 myAccount 中設定的密碼 The one you set in myAccount\]

## VPN

使用校內網路服務時，必須連線至校園網路。常見的校內網路服務包含但不限於：圖書館特定電子書與論文資料庫、Web of Science 付費論文搜尋引擎、ChatGPT 等。

當設備連線至外部網路時，可以透過 VPN 連線至校園網路。

若設備系統為 Windows 或 Mac，請依照 [步驟](https://wiki.uni-freiburg.de/rz/doku.php?id=vpn_fuer_windows) 下載對應版本的 FortiClient 軟體。若設備系統為 Linux/Unix，請透過「設定」內的網路設定介面或終端機使用 `openconnect` 以及 `network-manager-openconnect`。若有錯誤發生，請確認兩者是否已完成安裝。

根據 Freiburg 大學計算中心的建議，`openconnect` 和 `network-manager-openconnect` 在 Linux 系統上運作較佳。Windows 和 Mac 使用者請改為依照 [這些步驟](https://wiki.uni-freiburg.de/rz/doku.php?id=vpn_fuer_windows) 下載 FortiClient。

**一般設定 General:**

- VPN 協定 VPN Protocol: Fortinet SSL VPN
- 閘道器 Gateway: fortivpn.uni-freiburg.de
- 使用者代理 User Agent: \[你的帳號\]@email.uni-freiburg.de
- CA 憑證 CA certificate: (無 none)

**軟體權杖認證 Software Token Authentication:**

- 權杖模式 Token Mode: RSA SecurID -- 手動輸入 manually entered

**透過登入連線 Connect via login:**

- 使用者 User: \[你的帳號\]@uni-freiburg.de
- 密碼 Password: \[eduroam 密碼 eduroam password\]

# 校內網路服務 Intranet Services

## AI/KI Service

在校園網路中，學校提供 AI 服務。未連線校園網路時，必須使用學校提供的 VPN 連線至校園網路。

**Update: 從31.07.2026起，每人每天只能使用\$20價值的用量。From 31.07.2026 onwards, \$20 limit is applied to every uni account per day.**

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

對於資料中心在其自有硬體上運作的模型，採用基於所需硬體和電力資源的名目價格。目前，每個使用的 GPU 收費 0.05 美分（GLM 5.2 \> 8 個 GPU：每百萬代幣輸入 0.40 美元 / 輸出 0.40 美元）。

Bei Modellen, die vom RZ auf eigener Hardware betrieben werden, wird ein fiktiver Preis gemäß der benötigten Hardware und Stromressourcen verwendet. Aktuell wird pro verwendeter GPU ein Preis von ¢0,05 verbucht (GLM 5.2 \> 8 GPUs: Input \$0,40 / Output \$0,40 pro Mio Token).

學校提供的使用者介面為 [OpenWebUI](https://openwebui.uni-freiburg.de/) 網頁，登入時會跳轉至大學帳戶的登入畫面。一般使用者可以直接使用該網頁向 AI 諮詢。

若要在其他工具或平台上使用本服務，可以在該介面左下角的齒輪符號（設定）內找到一組 API 金鑰。該組字串可應用於第三方服務，但因為 OpenWebUI 與一般 OpenAI 帳號結構不同，該組字串不可用於 OpenAI 的 Codex 終端機服務介面。例如，在文字編輯器 VSCode 使用 [Continue.dev](https://marketplace.visualstudio.com/items?itemName=Continue.continue) 提供的 [工具](https://marketplace.visualstudio.com/items?itemName=Continue.continue)，或是類似的開源編輯器 [Codium](https://open-vsx.org/extension/Continue/continue) 時，須將 AI 模型的資訊寫入設定檔案中。

- 基礎 URL Base URL: `https://openwebui.uni-freiburg.de/api`
- 你可以使用以下終端機指令來查看模型名稱列表：`curl -L -v -H "Authorization: Bearer [api_key]" -H "Accept: application/json" https://openwebui.uni-freiburg.de/api/models >> openwebui.json`。此指令會產生一個 `openwebui.json` 檔案，請使用文字編輯器開啟該檔案，並在輸出結果中尋找 `id` 欄位。

若要在 [VSCode](https://marketplace.visualstudio.com/items?itemName=Continue.continue) 或 [Codium](https://open-vsx.org/extension/Continue/continue) 中使用 [Continue.dev](https://www.continue.dev/) 擴充功能，請點擊視窗左側的「Continue」分頁，然後依序點擊「Configs」與「Main Config」。這會在編輯面板中開啟 `config.yaml` 檔案，請將該檔案設定為以下格式：

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

學校或 OpenAI 會定期更新、更名 OpenWebUI 裡面使用的模型，因此必須不定時使用 [這個腳本](../ufr_models/#update-models-with-this-python-script) 更新 agent 裡面註冊的模型。這個腳本會直接覆寫 `~/.continue/config.yaml` 裡面的內容。

The university or OpenAI will periodically update and rename the models used in OpenWebUI. Therefore, you must regularly update the models registered in the third-party agent (Continue.dev in this case) using [this script](../ufr_models/#update-models-with-this-python-script). This script will directly overwrite the contents of `~/.continue/config.yaml`.

首先，下載這個程式並用文字編輯器開啟。檔案中寫的路徑 `~/.continue/config.yaml` 是 Linux 系統通用的路徑。Windows 使用者需要從 Continue 擴充功能裡面開啟 Configs 側欄，點選 Main Config 旁邊的齒輪就會打開 config.yaml。右鍵點擊編輯器上方的檔名，選擇「開啟檔案位置」，找到該檔案的位置並開啟這個腳本，將 `~/.continue/config.yaml` 更改為正確的路徑。同時，你必須將自己的 API key 寫入這個腳本第 10 行的 `OPENWEBUI_TOKEN`。設定完成後，請回到「Continue」分頁中的首頁嘗試進行對話，確保設定運行順暢。請務必確認本機位於大學網路之下或使用 VPN。

**目前測試情況 Current tested situation:**

**UFR 開頭的模型可以正常使用，但 OpenAI 開頭的會有 handling error**

## 校內儲存伺服器 Connecting to Your Account at the Uni Storage Server (Netzlaufwerk)

在校園網路中，學校提供一個 Samba 架構的伺服器（20GB），供你儲存檔案。未連線校園網路時，必須使用學校提供的 VPN 連線至校園網路。

大學 Wiki 說明文件「Netzlaufwerk verbinden」適用於 [Win10](https://wiki.uni-freiburg.de/rz/doku.php?id=netzlaufwerk_verbinden_windows)、[Mac](http://wiki.uni-freiburg.de/rz/doku.php?id=smb_mac) 和 [Linux](http://wiki.uni-freiburg.de/rz/doku.php?id=smb_linux)。

**在 Linux 的 GNOME 檔案管理員中，前往「網路」分頁。**

**In GNOME file manager in Linux, go to the "Network" tab.**

在文字框中輸入：`smb://[你的帳號].files.uni-freiburg.de/home/[你的帳號]`

會出現一個視窗，請輸入以下資訊：

- 使用者名稱 Username: \[你的帳號\]@uni-freiburg.de
- 網域 Domain: PUBLIC
- 密碼 Password: \[eduroam 密碼 eduroam-password\]

## BwUniCluster（仍在進行中 Still Working on It!）

BwUniCluster 是由巴登 - 符騰堡邦透過大學網路提供的通用高效能運算叢集。伺服器位於卡爾斯魯厄理工學院（KIT）。

請閱讀 [說明文件](https://wiki.bwhpc.de/e/Main_Page) 以註冊和使用此服務。與伺服器建立連線的方式有多種，以下是我的解決方案，應適用於所有 Linux 環境。

### 1. 使用 SSH 登入 Login with SSH

``` bash
ssh [你的帳號]@uc3.scc.kit.edu
```

輸入 OTP 碼和你的密碼。

- 此連線需要雙重認證（2FA）。它使用的是 eduMFA，但在我手機上註冊不正確，所以我必須下載另一個應用程式 Google Authenticator，在每次登入時產生 OTP 碼。

### 2. 載入模組 Load Modules

- 設定在 `.bash_profile` 中，讓每次呼叫 bash 時自動載入常用的模組
- 例如：C 編譯器 **gcc**（用於安裝某些 R 套件）、**conda**（用於 tidyverse）

**Shell 腳本範例 Shell script example:**

``` bash
# .bash_profile Contents
module load math/R/4.5.1
module load compiler/gnu/14.2
module load devel/miniforge/25.3.1-python-3.12
```

### 3. 使用 SSH 連線上傳檔案至伺服器 Upload Files to the Server with SSH Connection

- 指令為：`sftp [你的帳號]@uc3.scc.kit.edu`，透過提示輸入 OTP 碼和你的密碼
- 從本機上傳檔案至伺服器：`put [本機檔案路徑/名稱] [伺服器檔案路徑]`
- 從伺服器下載檔案至本機：`get [伺服器檔案路徑/名稱] [本機檔案路徑]`
- 使用 sftp 進入伺服器時，你無法編輯或刪除檔案

### 4. 提交工作至高效能運算節點 Submit Jobs to High Performance Computing Nodes

- 系統僅接受 bash 腳本
- 我的 R 程式碼提交腳本範例

```bash 
script.sh #!/bin/bash \# #SBATCH --partition=dev_cpu #SBATCH --job-name=myJob #SBATCH --time=00:20:00 #SBATCH --nodes=1 #SBATCH --ntasks-per-node=1 #SBATCH --cpus-per-task=16 #SBATCH --error=error.log #SBATCH --mem=32gb #SBATCH --mail-type=ALL #SBATCH --mail-user=yk112\@email.uni-freiburg.de

module load math/R/4.5.1 module load compiler/gnu/14.2 module load devel/miniforge/25.3.1-python-3.12 conda activate r_ragg_env

Rscript rcode.r 2\>&1 \| tee run.log
```

bash 腳本必須在腳本開頭指明 bash 語言的位置 `#!/bin/bash`。此路徑適用於所有 Linux 環境。接著，我向叢集排隊工具 SBATCH 介紹此工作的詳細資訊。我要求 SBATCH 將腳本帶至 `dev_cpu` 叢集（請根據你的需求 [在此選擇](https://wiki.bwhpc.de/e/BwUniCluster3.0/Running_Jobs#Regular_Queues) 叢集，或使用指令 `sinfo_t_idle` 檢查目前哪個叢集處於閒置狀態）。

請注意，當你連線至伺服器時，僅處於登入節點，尚未進入高效能叢集。因此，不要在登入後直接執行測試案例。請將測試程式碼發送至具有「dev」字樣的節點，例如 dev_cpu 或 [其他](https://wiki.bwhpc.de/e/BwUniCluster3.0/Running_Jobs#Development_Queues) 發展節點。這些發展節點僅允許少於 30 分鐘的工作。因此，你不會像在一般排隊中那樣等待太久。

![bwUniCluster 3.0 Hardware and Architecture](https://wiki.bwhpc.de/e/File:Uc3.png)

繼續說明 sbatch 參數。我將此工作命名為「myJob」。工作名稱不會影響執行結果，僅會顯示在通知電子郵件的標題中。工作名稱過長時會被截斷。請保持工作名稱簡單，並與你可能同時提交的其他工作區分開來。

節點數量取決於你的程式碼是否使用平行運算。由於此 R 腳本是 DADA2 流程管線，它僅使用一個節點。DADA2 的 `assignTaxonomy` 函數在 Linux 中支援多執行緒。因此，我們可以在這個工作中使用 16 個 CPU（或更多）。如果有錯誤發生，會在目前資料夾中建立 `error.log` 檔案。每當工作開始、結束、停止或執行任何動作時，會發送電子郵件通知我。

腳本載入 R 版本 4.5.1、C 編譯器、Python 版本 3.12、conda 環境 r_ragg_env（這是我安裝 tidyverse 的環境）。這些是我經常使用的模組。然後，我們终于可以執行 R 腳本。執行 R 腳本時，如果有任何輸出（stdout），會建立文字檔案並將它們帶入目前資料夾中的 `run.log`。每次執行此程式碼時，run log 檔案會被覆寫。

- 使用 `{bash} sbatch script.sh` 將此 bash 腳本提交至 SBATCH
- 使用指令 `squeue` 檢查你自己的工作排隊
- 複製工作編號並使用 `scancel [工作編號]` 停止叢集繼續排隊或執行腳本
- Submit this bash script to SBATCH with `{bash} sbatch script.sh`
- Check your own job queue with the command `squeue`
- Copy the job number and use `scancel [job_number]` to stop the cluster from continuing to queue or execute the script

# 學校信箱設定 Uni Freiburg Email Third-Party Client Setup

> 2025-09-24 發布於台灣 Freiburg 同學會

由於最近重新設定了電腦，重新在電腦的信箱程式裡面登入學校信箱，想起第一次設定的惡夢，供新年度同學們參考。一開始當然可以直接前往 email.uni-freiburg.de 這個網站（也就是 \@ 之後的那一串網址），用網頁登入學校信箱。但是要設定到電腦跟手機裡面超級頭痛。

首先，你要前往哥廷根大學的系統（[GWDG IDM 入口網站](https://idm.gwdg.de/Account/Login?ReturnUrl=%2F)）申請一組使用者名稱以及密碼。這個系統使用學校帳密登入，然後需要下載 eduMFA Authenticator 到手機，進行二段式認證登入。

進入 [GWDG IDM 入口網站](https://idm.gwdg.de/Account/Login?ReturnUrl=%2F)，選擇 "Anmeldung mit single sign-on"，然後點擊 "Anmelden"。

使用大學電子郵件登入（需要二段式認證）。

點擊右上角的頭像以切換選單，選擇第二個帶有鑰匙圖示的選項。

在左側面板中，選擇 \[DE\] APP-ZUGANGSDATEN / \[EN\] APPLICATION CREDENTIALS（需要再次進行二段式認證）。

在 Open-Xchange 下方，點擊 "ADD +" 申請使用者名稱和密碼。這組 uid 和密碼用於電子郵件伺服器設定。

在左側選單選擇 \[DE\] APP-ZUGANGSDATEN / \[EN\] APPLICATION CREDENTIALS，為這個連結取個名字（Bezeichnung）跟使用期限（Ablaufdatum）之後，就會產生一組帳號密碼（uid & Passwort）。右邊各有一個複製貼上按鈕，一定要開個編輯器馬上存起來，離開頁面就再也看不到這組帳密了。

另外要說明，學校帳號跟名字連在一起是兩個信箱名稱的「同義詞」。以我的帳號來說，yk112 跟 yu-chen.kuo 都是同一個信箱的名字。你可以在裡面設定 Information \> Primäre E-Mail-Adresse 擇一。預設是名字的那個。可能只有像我在入學前有更改過護照拼寫，會偏好使用學校帳號的那個信箱名稱。

附帶一提，要跟學校更改學生證名字的方法是直接去註冊處二樓的外籍生櫃台，給他們看護照（或是其他證明文件）以及現有的學生證就可以申請。等幾天之後收到通知再去一樓領新的學生證。不需要繳費，但是要重新申請 SWFR 帳號以及 Autoload，不會自動轉移。

扯遠了，總之現在可以開始在自己的裝置上面設定登入資訊了。在自己選擇的信箱程式登入頁面輸入信箱，密碼是 GWDG 系統產生的那個密碼。

- 電子郵件 Email: \[你的帳號\]@email.uni-freiburg.de
- 密碼 Password: \[GWDG 產生的密碼 password from GWDG\]

**收信伺服器 Incoming Server:**

- 協定 Protocol: IMAP
- 主機名稱 Hostname: email.uni-freiburg.de
- 連接埠 Port: 993
- 加密方式 Encryption: SSL/TLS
- 使用者名稱 Username: \[GWDG 申請到的帳號 uid from GWDG\]

**發信伺服器 Outgoing Server:**

- 連接埠 Port: 587
- 加密方式 Encryption: STARTTLS
- 使用者名稱 Username: \[GWDG 申請到的帳號 uid from GWDG\]

這樣就可以完成登入了。