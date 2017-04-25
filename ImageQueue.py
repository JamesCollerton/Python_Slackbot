from NeuralNetwork import NeuralNetwork

import os
import time

class ImageQueue:

    __path = 'images_input_temp/';

    def run(self):
        """
        This gets the oldest image from the images_input folder and then sends
        it to the neural network to get combined. Once it has been combined it
        deletes the image from the images input folder and looks for the next
        one to do. This should be done on its own thread so it can run while
        the slackbot looks for images.
        """
        oldestImage = self.getOldestImage();
        print(oldestImage);
        # self.runNeuralNetwork(oldestImage);
        self.deleteOldestFile(oldestImage);

        self.run();


    def getOldestImage(self):
        """
        This gets the oldest image in the folder. Gets the current time in
        seconds since the epoch, then loops through all files in the folder to
        find the oldest one.
        """
        path = 'images_input_temp';
        earliestTime = time.time();
        earliestFile = None;

        for filename in os.listdir('images_input_temp'):

            fileName = os.path.join(path, filename)
            fileTime = os.path.getmtime(fileName);

            if fileTime < earliestTime:
                earliestTime = fileTime;
                earliestFile = fileName

        return(os.path.split(earliestFile)[1])

    def runNeuralNetwork(self, oldestImage):
        """
        This is used to actually run the neural network on the file we have
        found to be the first one in the queue.
        """
        neuralNetwork = NeuralNetwork();
        neuralNetwork.runNeuralNetwork(oldestImage);

    def deleteOldestFile(self, oldestImage):
        """
        This is used to delete the oldest file once we've created the neural
        network image from it. It really copies the file so we can have two to
        work with while we're testing.
        """
        os.remove(self.__path + oldestImage)
