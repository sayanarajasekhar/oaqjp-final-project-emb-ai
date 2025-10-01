from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

# Route for root
@app.route("/")
def hello_world():
    return render_template("index.html")

# Route for emotionDetector
@app.route("/emotionDetector")
def emotionDetector():
    text_to_analyze = request.args.get('textToAnalyze')
    emotion_scores = emotion_detector(text_to_analyze)
    return emotion_scores

# Run the app in debug mode if the script is executed directly.
if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)