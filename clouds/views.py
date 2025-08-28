from django.shortcuts import render
from .utils import generate_word_cloud 

def word_cloud_view(request):
    """
    This view handles both the initial page load and the HTMX request 
    to generate the word cloud.
    """
    
    # Text source for the word cloud. In a real app, this could come from a form submission.
    sample_text = """
    Django framework works along with HTMX which is a library that allows you to access modern browser features directly 
    from HTML, rather than using javascript. It gives you access to AJAX, CSS Transitions, 
    WebSockets and Server Sent Events directly in HTML, using attributes, 
    so you can build modern user interfaces with the simplicity and power of hypertext.
    API driven functions can be integrated as well.
    Bootstrap is a powerful, feature-packed frontend toolkit that be used with Django page template. 
    Build anything—from prototype to production—in minutes with Django.
    Django is a high-level Python Web framework that encourages API driven, rapid development and clean, pragmatic design.
    """

    # HTMX requests include a 'HTTP_HX_REQUEST' header, which Django
    # makes available as request.htmx.
    if request.htmx:
        # If it's an HTMX request, generate the word cloud and return the partial template.
        image_data = generate_word_cloud(sample_text)
        context = {'image_data': image_data}
        # This partial template contains only the image.
        return render(request, 'clouds/partials/wordcloud_image.html', context)

    # For a standard, full-page load, just render the main template.
    return render(request, 'clouds/index.html')
