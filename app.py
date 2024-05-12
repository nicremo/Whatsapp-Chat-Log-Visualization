from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from chat_parser import parse_chat
import os

app = Flask(__name__)
# Define the folder to store uploaded files
app.config['UPLOAD_FOLDER'] = 'uploads/'
# Set the maximum allowed payload to 10 megabytes (changeable by adjusting the number, e.g., 50*1024*1024 for 50 MB)
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

@app.route("/", methods=['GET', 'POST'])
def chat():
    # Handle file upload on POST request
    if request.method == 'POST':
        file = request.files['file']
        # Check if a file is selected
        if file and file.filename != '':
            # Secure the filename to prevent directory traversal attacks
            filename = secure_filename(file.filename)
            # Create a path to save the file
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            # Save the file to the filesystem
            file.save(file_path)
            # Parse the chat file and get the chat data
            chats = parse_chat(file_path)
            # Render the template with chat data
            return render_template('index.html', chats=chats)
        else:
            # Redirect to the same page if no file is selected
            return redirect(request.url)
    # Render the template with no chat data on a GET request
    return render_template('index.html', chats=[])

# Run the app
if __name__ == "__main__":
    app.run(debug=True)