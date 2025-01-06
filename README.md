# Centrifugo Dashboard

## Description
The Telegram bot integrates with Centrifugo to provide a lightweight, user-friendly dashboard that allows users to monitor and manage Centrifugo directly from Telegram. This feature is designed to simplify operations by making essential Centrifugo metrics and controls accessible via a chat interface.

## Prerequisites
Before running the project, ensure you have the following installed:
- [Centrifugo](https://centrifugal.dev/docs/getting-started/)
- A Telegram bot token ([How to create a Telegram bot](https://core.telegram.org/bots#creating-a-new-bot))

## Getting Started

### 1. Download and Start Centrifugo
- Visit the [Centrifugo download page](https://centrifugal.dev/download) to download the latest version.
- Install and start Centrifugo by following the installation guide.

### 2. Edit the `config.json` File
- Locate the `config.json` file in your Centrifugo directory.
- Add `"admin": true, "http_stream": true,` to your configuration.

### 3. Run Centrifugo
- Start Centrifugo with the updated configuration:
  ```bash
  centrifugo --config=config.json --debug
  ```

### 4. Run Pocketbase
- Navigate to the pocketbase folder in the project repository:
  ```bash
  cd pocketbase
  ```
- Run Pocketbase:
  ```bash
  ./pocketbase serve
  ```
- Log in to the Pocketbase admin panel:
    Visit: http://127.0.0.1:8090/_/#/
    Use the following credentials:
      Email: admin@admin.admin
      Password: adminadmin

### 5. Add `.env` Variables
- Create a `.env` file in your project root directory if it doesn't already exist.
- Add the necessary environment variables required by your project. Example:
  ```
  export BOT_TOKEN='<YOUR_BOT_TOKEN>'
  export CENTRIFUGO_TOKEN_SECRET="<YOUR_CENTRIFUGO_TOKEN_SECRET>"
  export CENTRIFUGO_API_KEY="<YOUR_CENTRIFUGO_API_KEY>"
  export SECRET_KEY='<YOUR_SECRET_JWT_KEY>'
  export POCKETBASE_ADMIN_EMAIL='admin@admin.admin'
  export POCKETBASE_ADMIN_PASSWORD='adminadmin'
  ```

### 6. Run the Telegram Bot
- Start the Telegram bot:
  ```bash
  python main.py
  ```
