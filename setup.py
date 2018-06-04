from distutils.core import setup

if __name__== '__main__':
    setup(include_package_data=True,
          description='TF MOtif Discovery from Importance SCOres',
          url='NA',
          download_url='NA',
          version='0.1',
          packages=['modisco', 'modisco.cluster','modisco.backend',
                    'modisco.visualization', 'modisco.affinitymat',
                    'modisco.tfmodisco_workflow'],
          setup_requires=[],
          install_requires=['numpy>=1.9', 'psutil', 'theano>=0.9', 'scikit-learn>=0.19'],
          scripts=[],
          name='modisco')
