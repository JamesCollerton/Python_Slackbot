import os

class NeuralNetwork:

    def runNeuralNetwork(self):
        """
        Runs the neural network from the dependencies
        file.
        """
        os.chdir('dependencies/neural_artistic_style/');
        os.system('bash runPy.sh');
