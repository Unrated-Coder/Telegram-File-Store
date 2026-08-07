<p align="center">
  <a href="#!">
    <img src="https://imgyx.pages.dev/FNoiO" alt="Telegram File Store Bot Banner" width="100%" style="border-radius: 12px; border: 1px solid rgba(255,255,255,0.08); box-shadow: 0 20px 50px rgba(0, 114, 255, 0.25);" />
  </a>
</p>

<h1 align="center">🤖 Telegram File Store Bot</h1>

<p align="center">
  <b>A hyper-fast, secure, and modern Telegram File Storage engine built on Hydrogram (API Layer 223). Bypasses ads, handles dynamic auto-deletion, and forces community subscriptions automatically.</b>
</p>

<p align="center">
  <a href="#!"><img src="https://img.shields.io/badge/Maintained%20With-❤️-blue?style=for-the-badge&labelColor=111111" alt="Maintained with Love"></a>
  <a href="#!"><img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white&labelColor=111111" alt="Python Version"></a>
  <a href="#!"><img src="https://img.shields.io/badge/Framework-Hydrogram--223-26A69A?style=for-the-badge&logo=telegram&logoColor=white&labelColor=111111" alt="Framework"></a>
  <a href="#!"><img src="https://img.shields.io/badge/Database-MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white&labelColor=111111" alt="Database"></a>
</p>

<hr style="border: 0; height: 1px; background: linear-gradient(to right, rgba(255,255,255,0), rgba(255,255,255,0.15), rgba(255,255,255,0)); margin: 30px 0;" />

## 📡 Live System Diagnostics & Flowchart

<p align="center">
  <a href="#!"><img src="https://img.shields.io/badge/SYSTEM_STATUS-ONLINE-00E5FF?style=flat-square&labelColor=111111" alt="System Status"></a>
  <a href="#!"><img src="https://img.shields.io/badge/DATABASE_LINK-CONNECTED-00E676?style=flat-square&labelColor=111111" alt="DB Status"></a>
</p>

```mermaid
graph TD
    %% System Flow & Integration Diagram
    Bot[🤖 File Store Bot] -->|⚡ Hydrogram Engine| TG[💬 Telegram Gateways]
    Bot -->|↔️ Read/Write Metadata| DB[(🍃 MongoDB Atlas DB)]
    Bot -->|🔐 Gate User Request| FSub{🛡️ Force Sub Check}
    
    FSub -->|✖️ Not Subscribed| Join[📢 Redirect: Join Channel]
    FSub -->|✔️ Subscribed| Access[📂 Grant Temporary Link]
    
    Bot -->|❤️ Health Status| Web[🌐 Flask Server on Port 8080]

    %% Color Coding & Styling
    style Bot fill:#1e293b,stroke:#3b82f6,stroke-width:2px,color:#fff
    style DB fill:#064e3b,stroke:#10b981,stroke-width:2px,color:#fff
    style TG fill:#0c4a6e,stroke:#0ea5e9,stroke-width:2px,color:#fff
    style FSub fill:#78350f,stroke:#f59e0b,stroke-width:2px,color:#fff
    style Join fill:#991b1b,stroke:#f43f5e,stroke-width:2px,color:#fff
    style Access fill:#14532d,stroke:#22c55e,stroke-width:2px,color:#fff
    style Web fill:#311042,stroke:#8b5cf6,stroke-width:2px,color:#fff
```

<hr style="border: 0; height: 1px; background: linear-gradient(to right, rgba(255,255,255,0), rgba(255,255,255,0.15), rgba(255,255,255,0)); margin: 30px 0;" />

## ⚡ Core Features

*   **🎨 Custom Button Background Colors**
    Seamlessly style buttons with background colors (Primary, Danger, Success) using `style="primary"`, `style="danger"`, or `style="success"` keyword arguments natively, achieved by global monkey-patches on `InlineKeyboardButton.__init__` and `InlineKeyboardButton.write`.
*   **📂 Dynamic File Indexing**
    Securely upload, store, and automatically index files sent to designated private database channels.
*   **🔗 Instant Link Engine**
    Generates secure, direct, and custom-formatted batch or single links in milliseconds.
*   **⏳ Automatic File Purge**
    Customizable auto-delete timers secure shared materials from being leaked permanently.
*   **🛡️ Force Join Controller**
    Gates file links until users actively subscribe to configured target update channels.
*   **🌐 Built-in KeepAlive Web Server**
    Integrated Flask micro-service ensures cloud deployments survive health checks without entering sleep mode.
*   **🐳 Multi-Platform Deployment**
    Optimized to run on Docker, Heroku Procfiles, Koyeb, VPS systems, and Render with ease.

<hr style="border: 0; height: 1px; background: linear-gradient(to right, rgba(255,255,255,0), rgba(255,255,255,0.15), rgba(255,255,255,0)); margin: 30px 0;" />

## 🛠 Commands Deck

<details>
<summary><b>👤 Click to Expand User Commands</b></summary>
<br>

*   `/start` — Initialize the bot interface and check system availability.
*   `/help` — Display detailed commands list and usage tutorial.
*   `/ping` — View Bot Database Connection Speed.

</details>

<details>
<summary><b>👑 Click to Expand Admin Commands</b></summary>
<br>

### 📡 Broadcast & Performance
*   `/commands` — View a comprehensive quick list of administrative commands.
*   `/stats` — Monitor server metrics like CPU/RAM usages and user volume.
*   `/users` — Get precise counts of active registered users in the database.
*   `/broadcast` — Broadcast a targeted global text message to all users.
*   `/retrieve_on ` — Toggle on Auto-Delete Msg Alert.
*   `/retrieve_off` — Toggle off Auto-Delete Msg Alert
*   `/pbroadcast` — Broadcast photos with customized HTML captions.
*   `/dbroadcast` — Broadcast direct videos, audios, or generic files.

### 🔗 Link & Parameter Settings
*   `/genlink` — Generate a secure unique shareable link for a single file.
*   `/batch` — Bundle several file components into one single access key.
*   `/custom_batch` — Generate highly customized multi-file access routes.
*   `/dlt_time` — Set global delay timers before shared files are purged.
*   `/check_dlt_time` — Read current file auto-delete timer configuration.

### 🛡️ Access & Moderation Tools
*   `/ban` — Revoke a specific user ID's access to the bot engine.
*   `/unban` — Re-authorize blocked users in the system database.
*   `/banlist` — Inspect all restricted users currently locked out of service.
*   `/addchnl` — Add a channel to the mandatory subscriber verification checks.
*   `/delchnl` — Remove a channel from force-subscription verification.
*   `/listchnl` — List all channels currently enforcing active membership checks.
*   `/fsub_mode` — Globally toggle the force-subscription requirement on or off.

### 🔑 Security Privileges
*   `/add_admin` — Promote a user to authorized administrator status.
*   `/deladmin` — Revoke administrative rights from a specific user.
*   `/admins` — Fetch the directory of registered system administrators.

</details>

<hr style="border: 0; height: 1px; background: linear-gradient(to right, rgba(255,255,255,0), rgba(255,255,255,0.15), rgba(255,255,255,0)); margin: 30px 0;" />

## ⚙️ Configuration Variables Blueprint

Below is the structured table representation of required configuration keys to link your services successfully:

| Variable | Type | Description | Required | Reference / Source |
| :--- | :--- | :--- | :--- | :--- |
| `APP_ID` | Integer | API identifier obtained from the portal. | **Yes** | [Telegram Developer Portal](https://my.telegram.org) |
| `API_HASH` | String | API Hash key companion matching the `API_ID`. | **Yes** | [Telegram Developer Portal](https://my.telegram.org) |
| `TG_BOT_TOKEN` | String | Bot token generated by BotFather. | **Yes** | [@BotFather](https://t.me/BotFather) |
| `DATABASE_URL` | Connection String | Your MongoDB Atlas or local deployment database URL. | **Yes** | [MongoDB Atlas Cluster](https://www.mongodb.com/cloud/atlas) |
| `CHANNEL_ID` | Integer | Destination database channel ID where files are stored. | **Yes** | Telegram Storage Channel |
| `OWNER_ID` | Integer | Your personal Telegram User ID to bypass authorization. | **Yes** | Owner Control Center |

```mermaid
graph LR
    subgraph ConfigVariables ["Environment Variables Map"]
        TK[TG_BOT_TOKEN]
        AID[APP_ID]
        AH[API_HASH]
        DB_URL[DATABASE_URL]
        CID[CHANNEL_ID]
        OID[OWNER_ID]
    end

    subgraph ServiceTargets ["Authorized Targets & APIs"]
        BotFather[💬 Telegram BotFather API]
        Telegram[🚀 Telegram Developer Portal]
        Mongo[🍃 MongoDB Atlas Cluster]
        Channel[📁 Storage Channel database]
        Admin[👑 Owner Control Center]
    end

    TK --> BotFather
    AID --> Telegram
    AH --> Telegram
    DB_URL --> Mongo
    CID --> Channel
    OID --> Admin

    style ConfigVariables fill:#111111,stroke:#333333,color:#fff
    style ServiceTargets fill:#111111,stroke:#333333,color:#fff
    style TK fill:#1e293b,stroke:#3b82f6,color:#fff
    style AID fill:#1e293b,stroke:#3b82f6,color:#fff
    style AH fill:#1e293b,stroke:#3b82f6,color:#fff
    style DB_URL fill:#064e3b,stroke:#10b981,color:#fff
    style CID fill:#0c4a6e,stroke:#0ea5e9,color:#fff
    style OID fill:#3b0764,stroke:#a855f7,color:#fff
```

<hr style="border: 0; height: 1px; background: linear-gradient(to right, rgba(255,255,255,0), rgba(255,255,255,0.15), rgba(255,255,255,0)); margin: 30px 0;" />

## 🚀 Easy Deployment

### 1. Cloud Deploy Support
Deploy directly using cloud services (Badges are active to open their respective setup pages, they do not trigger white raw image views):

<p align="left">
  <a href="https://dashboard.koyeb.com/deploy" target="_blank">
    <img src="https://img.shields.io/badge/Deploy%20To-Koyeb-000000?style=for-the-badge&logo=koyeb&logoColor=white" alt="Deploy to Koyeb" />
  </a>
  <a href="https://render.com/deploy" target="_blank">
    <img src="https://img.shields.io/badge/Deploy%20To-Render-4642C3?style=for-the-badge&logo=render&logoColor=white" alt="Deploy to Render" />
  </a>
  <a href="https://heroku.com/deploy" target="_blank">
    <img src="https://img.shields.io/badge/Deploy%20To-Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white" alt="Deploy to Heroku" />
  </a>
</p>

### 2. VPS Setup (Ubuntu/Debian)

```bash
# Clone the repository
git clone https://github.com/Unrated-Coder/Telegram-File-Store.git
cd telegram-file-store

# Install required dependencies
pip3 install -r requirements.txt

# Run the engine
python3 main.py
```

<hr style="border: 0; height: 1px; background: linear-gradient(to right, rgba(255,255,255,0), rgba(255,255,255,0.15), rgba(255,255,255,0)); margin: 30px 0;" />

## ⭐️ Credits & Developer
Modified, optimized, and maintained with ❤️ by **[@UNRATED_CODER](https://t.me/UNRATED_CODER)**. 

Join our official channel for instant support, updates, and more elite open-source projects:

<p align="left">
  <a href="https://t.me/UNRATED_CODER">
    <img src="https://img.shields.io/badge/Telegram-Channel-blue?style=for-the-badge&logo=telegram&logoColor=white&labelColor=111111" alt="Telegram Channel" />
  </a>
</p>
