from flask import Flask, render_template

app = Flask(__name__)

# Route for the fake download page
@app.route('/')
def home():
    return render_template('download_page.html')  # This serves the fake download page

# Route that simulates the download action and triggers the malware
@app.route('/download')
def download():
    print("Fake antivirus download started!")  # Print message to the terminal
    return "Download started... but malware is being injected in the background!"  # Message to show in the browser

if __name__ == "__main__":
    app.run(debug=True)  # Run the app in debug mode
