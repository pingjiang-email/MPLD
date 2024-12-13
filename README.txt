Multi-scale Pyramid Deformable Registration with Accurate Similarity Measure for Medical Image Analysis

This is a pytorch unofficial implementation of MPLD paper.


Requirements
CUDA 12.6 
torch 2.0 
Python 3.10

Data

To download the brain data at  https://learn2reg.grand-challenge.org/Datasets/
The training data is placed in the trainmoving1 and trainfixed1 files under the Data folder
The test data is placed in the testBANBEN1 file in the data folder

Training

Python train.py 

Configuration parameters for train can be found in configs_MPLDconfigs_MPLD under the models folder

Testing

Python test.py 