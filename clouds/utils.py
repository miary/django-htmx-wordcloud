from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import io
import urllib, base64

def generate_word_cloud(text):
    """
    Generates a word cloud image from text and returns it as a Base64 encoded URI.
    """
    stopwords = set(STOPWORDS)
    stopwords.update(["said", "ask", "told", "says", "it"])

    # --- Generate the Word Cloud ---
    wordcloud = WordCloud(
        stopwords=stopwords,
        background_color="white",
        width=800,
        height=400, # Adjusted height for better fit
        max_words=150,
        contour_width=3,
        contour_color='steelblue',
        colormap='viridis' # Added a colormap for more visual appeal
    ).generate(text)

    # --- Convert to an image that can be sent in the response ---
    plt.figure(figsize=(12, 6), facecolor=None)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.tight_layout(pad=0)

    # Save the image to a memory buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight')
    buffer.seek(0)
    
    # Encode the image in Base64 and create a data URI
    string = base64.b64encode(buffer.read())
    uri = string.decode('utf-8')
    
    # Free up memory by closing the plot
    plt.close()
    
    return uri
