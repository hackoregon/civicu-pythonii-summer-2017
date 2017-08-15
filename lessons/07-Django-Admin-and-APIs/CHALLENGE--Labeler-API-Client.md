# API Client Challenge

Now that you have DRF API to our Image Labeling app, lets use it!

1. write a function in `bot.py` that returns a `response` object for a GET request to your API to retrieve an image
2. write a function in `bot.py` that inserts a "vote" for that image (one argument should be the image ID and the other should be the label)
3. add an option (using argparse) to your `bot.py` to use these #1 to display an image from the API
4. add an option (or options) to your `bot.py` to insert a vote for an image (you'll need the image ID and label name string)

Your GET requests will likely need to "hit" the endpoint at `http://localhost:8000/labeler/api/download`
