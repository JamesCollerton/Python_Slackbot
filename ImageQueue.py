class ImageQueue:

    def run(self):
        """
        This gets the oldest image from the images_input folder and then sends
        it to the neural network to get combined. Once it has been combined it
        deletes the image from the images input folder and looks for the next
        one to do. This should be done on its own thread so it can run while
        the slackbot looks for images.
        """
