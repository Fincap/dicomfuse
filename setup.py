from setuptools import setup, find_packages

setup(
  name='dicomfuse',
  version='0.0.1',
  description='Simple library for finding affine translation matrix between two DICOM images.',
  url='https://github.com/Fincap/dicomfuse',
  author='Matthew Archer',
  author_email='matthew.e.archer9@gmail.com',
  packages=find_packages(where='dicomfuse'),
  python_requires='>=3.5'
)
