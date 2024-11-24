from flask import Flask, render_template, request
from EmotionDetector.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('text_to_analyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the label and score from the response
    label = response['dominant_emotion'][0]  
    score = response[response['dominant_emotion'][0]]

    if score == None:
        return "Invalid text! Please try again!"

    # Return a formatted string with the emotion label and score
    return "The given text has been identified as " + label + " with a score of " + str(score)

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)