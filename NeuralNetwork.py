import os
import shutil

class NeuralNetwork:

    bashString = 'python neural_style.py --content ../images/dave_face.jpeg --styles ../images/style.jpg --output ../images/output.jpg --iterations 10'

    imageSourceLocation = 'images_input_temp/';
    imageDestLocation = 'dependencies/images/';
    imageDestFileName = 'style.jpg';

    imageOutputFileName = 'output.jpg'
    imageSlackBotLocation = 'images_output/';

    def moveImageIn(self, imageName):
        """
        This is used to move the named image from the images
        file into the temporary image folder and rename it to
        style.jpg for the neural network to work on.
        """
        shutil.move(self.imageSourceLocation + imageName, self.imageDestLocation + self.imageDestFileName);

    def executeNeuralNetwork(self):
        """
        Runs the neural network from the dependencies
        file.
        """
        os.chdir('dependencies/neural_artistic_style/');
        os.system(self.bashString);
        os.chdir('../../');

    def moveImageOut(self):
        """
        This is used to move the image out from the neural
        network folders into a top level folder to be used
        by the SlackBot
        """
        shutil.move(self.imageDestLocation + self.imageOutputFileName, self.imageSlackBotLocation + self.imageOutputFileName);

    def runNeuralNetwork(self, imageName):
        """
        Moves an image from the input folder to the neural
        networks folder, then runs the NN on it. Takes the
        output and moves it to an output folder.
        """
        self.moveImageIn(imageName);
        self.executeNeuralNetwork();
        self.moveImageOut();
