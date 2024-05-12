from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

classifiers = [
    'Intended Audience :: Developers',
    'Programming Language :: Python :: 3.7',
    'License :: OSI Approved :: MIT License',
    "Operating System :: OS Independent"
]

setup(
     name='tigerbx',

     version='0.1.16',
     description='Processing MRI images based on deep-learning',
     long_description_content_type='text/markdown',
     url='https://github.com/htylab/tigerbx',

     author='Biomedical Imaging Lab, Taiwan Tech',
     author_email='',
     License='MIT',
     classifiers=classifiers,

     keywords='MRI brain segmentation',
     packages=find_packages(),
     package_data={
        '': ['*.nii.gz'],  # include the MNI152 template
     },
     include_package_data=True,

     entry_points={
        'console_scripts': [
            'tigerbx = tigerbx.bx:main',

        ]
    },
     python_requires='>=3.7',
     install_requires=[
             'numpy>=1.21.6',
             'nilearn>=0.9.2',
	     'SimpleITK>=2.0.0',
         ]
)
