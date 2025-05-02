from setuptools import setup, find_packages

setup(
    name='pheonix',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'langgraph',
        'langchain',
        'google-cloud-bigquery',
        'pandas',
        'plotly',
        'fastapi',
        'streamlit',
        'python-dotenv',
        'vertexai',
    ],
    author='Your Name',
    description='LangGraph AI application for financial data analysis',
)