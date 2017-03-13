# This is to act as a set of notes for how to install
# the required dependencies for the project. The first
# required ones are numpy, theano and filelock which can 
# be installed using the below.

# pip install numpy
# pip install filelock

# The second one that is needed is DeepPy. To install that
# run the below:

# git clone https://github.com/zomux/deepy
# cd deepy
# pip install -r requirements.txt

# At this point you might end up with some problems installing 
# scipy, so will need to use miniconda, which is found at the
# below:

# https://conda.io/miniconda.html

# Download that and then run 

# conda install scipy

# Once scipy is installed you need to install theano using the
# below

# pip install theano

# The final stage is to run the two below commands from inside 
# deepy directory

# source bin/cpu_env.sh
# python experiments/mnist/mlp_dropout.py

