"""
This module contains the Flask application for the emotion detection service.
It handles web requests, processes text for emotion analysis, and displays results.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """
    This function deploys the HTML file
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def emo_detector():
    """
    This function performs emotion analysis
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} "
        f"and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
        )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
