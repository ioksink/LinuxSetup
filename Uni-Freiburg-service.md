# 帳號設定 Uni Freiburg myAccount

在第一次註冊之後的某一天會收到學校寄來的帳號密碼信，故事從這裡開始～以下將你收到的帳號英文與數字組合以[你的帳號]或[Username]表示。

The story starts from getting an account per email after the first immatriculation. The username of this account should replace [Username] in the following manual.

# 網路

## 無線網路協定 Wifi/WLAN

我記得在一開始收到的信中，帳號是固定由學校提供，密碼則是進到myAccount自行設定的。在學校的帳密設定網站 [myAccount](https://myaccount.uni-freiburg.de/uadmin/login) 中，同樣可以設定泛歐洲科研與教育網路協會的學術無線網路協定 eduroam 的密碼。帳號固定為 [你的帳號]@uni-freiburg.de。

學校提供的網路說明書入口網站[德文版WLAN an der Universität Freiburg](https://www.rz.uni-freiburg.de/de/services/netztel/wlan-vpn)與[英文版WLAN at Freiburg University](https://www.rz.uni-freiburg.de/en/services/netztel-en/wlan-vpn-en?set_language=en)。該頁面也提供非大學成員訪問時的使用指引。

關於eduroam的設定說明書[WLAN mit eduroam](https://wiki.uni-freiburg.de/rz/doku.php?id=wlan-eduroam)，請參考連線設備的系統類型依照步驟設定。

Modify settings and receive eduroam password in [myAccount](https://myaccount.uni-freiburg.de/uadmin/login). The username is always [Username]@uni-freiburg.de for eduroam. Follow the instructions in [WLAN mit eduroam](https://wiki.uni-freiburg.de/rz/doku.php?id=wlan-eduroam) to setup eduroam in different systems. 

General setup within system wifi setting should contain the followings:
- Security: WPA & WPA2 Enterprise
- Authentication: PEAP
- Domain: uni-freiburg.de
- CA certificate: (None)
- [v] No CA certificate is required
- PEAP version: Automatic
- Inner authentication: MSCHAPv2
- Username: [Username]@uni-freiburg.de
- Password: [The one you set in myAccount]

## VPN

使用校內網路服務時，必須連線至校園網路。常用的校內網路服務包含但不限於圖書館特定電子書與論文提供廠商、Web of Science付費論文搜尋引擎、ChatGPT等。

設備連線至外部網路時，可以透過VPN連線至校園網路。

設備系統為Windows或是Mac時，請依照[步驟](https://wiki.uni-freiburg.de/rz/doku.php?id=vpn_fuer_windows)下載對應版本的FortiClient軟體。設備系統為Linux/Unix時，請透過「設定」內的網路設定界面或終端機使用`openconnect` 以及 `network-manager-openconnect`。若有錯誤發生，請確定兩者是否有完成安裝。

According to the Beratung Rechenzentrum der Universität Freiburg, `openconnect` and `network-manager-openconnect` works better in Linux. For Windows and Mac, download FortiClient following [these steps](https://wiki.uni-freiburg.de/rz/doku.php?id=vpn_fuer_windows) instead.

General
- VPN Protocol: Fortinet SSL VPN
- Gateway: fortivpn.uni-freiburg.de
- User Agent: [Username]@email.uni-freiburg.de
- CA certificate (none)
Software Token Authentication
- Token Mode: RSA SecurID -- manually entered

Connect via login
- User: [Username]@uni-freiburg.de
- Password: [eduroam password]

# 校內網路服務 Intranet services

## AI service/KI 

在校園網路中，提供AI服務。非連結校園網路時，必須使用學校提供的VPN連到校園網路。

學校提供的使用者界面為[OpenWebUI](https://openwebui.uni-freiburg.de/)，登入時會跳轉到大學帳戶的登入畫面。在該界面左下角的齒輪符號（設定）內可以找到一組API碼，該組字串可應用於第三方服務，但因為OpenWebUi與一般OpenAI帳號結構不同，該組字串不可用於OpenAI的codex終端機服務界面。

Within Uni network, chatGPT and Mistral models are provided in [OpenWebUI](https://openwebui.uni-freiburg.de/)

API key can be retrieved from the setting of the webpage and used in tools such as vscode extensions.
- Base URL = https://openwebui.uni-freiburg.de/api
- List of model names can be found via `bash curl -L -v -H "Authorization: Bearer [api_key]" -H "Accept: application/json" https://openwebui.uni-freiburg.de/api/models >> openwebui.json`. Look for "id" in the output file `openwebui.json`. 

## 校內儲存伺服器 Connecting to my account at the Uni storage server (Netzlaufwer)

在校園網路中，學校提供一個Samba架構的伺服器，20GB，供諸君儲存檔案。非連結校園網路時，必須使用學校提供的VPN連到校園網路。

Uni wiki manual "Netzlaufwerk verbinden" for [Win10](https://wiki.uni-freiburg.de/rz/doku.php?id=netzlaufwerk_verbinden_windows), [Mac](http://wiki.uni-freiburg.de/rz/doku.php?id=smb_mac), and [Linux](http://wiki.uni-freiburg.de/rz/doku.php?id=smb_linux).

In GNOME file manager in linux, go to tab "Network".

Input `smb://[Username].files.uni-freiburg.de/home/[Username]` in text box.

A window would appear...
- Username: [Username]@uni-freiburg.de
- Profile: PUBLIC
- Password: [eduroam-password]

# 學校信箱設定 Uni Freiburg email third-party client setup

> 2025-09-24 發布於台灣Freiburg同學會, ENG below

由於最近重新設定了電腦，重新在電腦的信箱程式裡面登入學校信箱，想起第一次設定的惡夢，供新年度菜雞們參考。一開始當然可以直接去email.uni-freiburg.de這個網站，也就是＠之後的那一串網址，用網頁登入學校信箱。但是要設定到電腦跟手機裡面超級頭痛。

首先，要去哥廷根大學的系統（[GWDG IDM portal](https://idm.gwdg.de/Account/Login?ReturnUrl=%2F)）裡面申請一組使用者名字以及密碼。這個系統是用學校帳密登入，然後要下載eduMFA Authenticator到手機，二段式認證登入。

左側選單選[DE]APP-ZUGANGSDATEN/[EN]APPLICATION CREDENTIALS，為這個連結取個名字(Bezeichnung)跟使用期限(Ablaufdatum)之後就會產生一組帳號密碼(uid&Passwort)。右邊各有一個複製貼上按鈕，一定要開個編輯器馬上存起來，離開就再也看不到這組帳密了。

另外要說明，學校帳號跟名字連在一起是兩個信箱名稱的Alias，拿我的帳號來說yk112跟yu-chen.kuo都是同一個信箱的名字。可以在裡面設定Information > Primäre E-Mail-Adresse擇一。預設是名字的那個。可能只有像我在入學前有更改過護照拼寫會偏好使用學校帳號的那個信箱名稱。附帶一提，要跟學校更改學生證名字的方法是直接去註冊處二樓的外籍生櫃台，給他看護照（或是其他證明文件）以及現有的學生證就可以申請。等幾天之後收到通知再去一樓領新的學生證，不需要繳費，但是要重新申請SWFR帳號以及Autoload，不會自動轉移。

扯遠了，總之現在可以開始在自己的裝置上面設定登入資訊了。在自己選擇的信箱程式登入頁面輸入信箱，密碼是GWDG系統產生的那個密碼。

收信伺服器 Incoming server
- Protokoll/Protocol: IMAP
- Hostname: email.uni-freiburg.de
- Port: 993
- SSL/TLS 加密
- Benutzername/UID/User: (GWDG申請到的帳號)

發信伺服器 Outgoing server
- Port: 587
- STARTTLS 加密

這樣就可以完成登入了。

## Uni Freiburg email third-party client setup (ENG)

Enter [GWDG IDM portal](https://idm.gwdg.de/Account/Login?ReturnUrl=%2F), choose  "Anmeldung mit single sign-on", "Anmelden".

Login with uni email (requires 2-step authentication).

Click on top-right corner avatar for toggle list. Choose the second option with a key.

At the left panel, choose [DE]APP-ZUGANGSDATEN/[EN]APPLICATION CREDENTIALS (requires 2-step authentication again).

Under Open-Xchange, click "ADD +" to apply for user name and password. This uid and password is used for email server setup.

### Take Thunderbird email client as example:

Email: [Username]@email.uni-freiburg.de

Password: [password from GWDG]

Incoming server
- Protokoll/Protocol: IMAP
- Hostname: email.uni-freiburg.de
- Port: 993
- SSL/TLS
- Benutzername/UID/User: [uid from GWDG]

Outgoing server
- Port: 587
- STARTTLS
- Benutzername/UID/User: [uid from GWDG]
