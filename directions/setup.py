from setuptools import setup

setup(
    name='Your Application',
    version='1.0',
    long_description=__doc__,
    packages=['text-direction'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask', 'requests', 'twilio']
)