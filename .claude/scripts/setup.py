from setuptools import setup

setup(
    name='eventai-tools',
    version='0.1.0',
    py_modules=['gemini_generate'],
    install_requires=[
        'playwright>=1.40.0',
    ],
    entry_points={
        'console_scripts': [
            'gemini-generate=gemini_generate:main',
        ],
    },
    description='EventAI infographic generation tools',
    author='EventAI + Lemmy',
)