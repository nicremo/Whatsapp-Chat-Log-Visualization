# WhatsApp Chat/Log Visualization 📊

This application provides a simple web interface to visualize WhatsApp chat logs. Users can locally upload their chat files, and the application will display the chat messages with the option to toggle the alignment and color theme for better readability.

## Features 🌟

- 📁 Upload WhatsApp chat logs/files.
- 💬 Display chat messages with timestamps and senders.
- 🎨 Toggle message alignment and color themes for a personalized view.

## Getting Started 🚀

Follow these instructions to set up the project on your local machine for development and testing purposes.

### Prerequisites 📋

Before you begin, ensure you have the following installed:
- Python 3
- Flask
- Werkzeug

You can install Flask and Werkzeug using pip:

```bash
pip install Flask Werkzeug
```

### Installation 🔧

1. Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/whatsapp-chat-visualization.git
cd whatsapp-chat-visualization
```

2. Create a virtual environment (optional):

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Start the Flask server:

```bash
flask run
```

5. Open your web browser and navigate to `http://127.0.0.1:5000/` to view the application.

## Usage 📝

To use the application, follow these steps:

1. Click on the 'Upload Chat File' button and select your WhatsApp chat file.
2. The chat will be displayed on the page.
3. Use the 'Toggle Alignment and Color' button to switch between different view modes.

## Exporting WhatsApp Chats 📤

To visualize your WhatsApp chats using this application, you need to first export them from your phone. Follow these steps to export a chat:

1. Open WhatsApp on your phone.
2. Go to 'Settings' > 'Chats' > 'Chat History'.
3. Select 'Export chat' and choose the chat you wish to export.
4. You will be prompted to export with or without media. Choose your preferred option.
5. Send the exported chat to your email or save it to your phone's storage.

Once you have the exported chat, you need to extract it if it's in a compressed format (such as a zip file) and ensure it is in a `.txt` file format.

### Preparing the Chat File 📄

If the exported chat is compressed (e.g., a `.zip` file), you need to extract the contents:

1. Locate the exported `.zip` file on your phone/computer.
2. Use a file extraction tool to unzip the contents.
3. Find the `.txt` file within the extracted folder.

Now you're ready to upload the `.txt` file to the application:

1. Click the 'Upload Chat File' button to select the file manually.
2. The application will process the file and display the chat messages.

## License 📜

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments 🙌

- [Flask](https://flask.palletsprojects.com/)
- [Werkzeug](https://werkzeug.palletsprojects.com/)
