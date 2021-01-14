from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='pymongo_cursor_json_encoder',
    packages=['pymongo_cursor_json_encoder'],
    version='0.2.0',
    license='MIT',
    description='Convert pymongo Cursor objects to JSON',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Roger Vilà',
    author_email='rogervila@me.com',
    url='https://github.com/rogervila/pymongo-cursor-json-encoder',
    download_url='https://github.com/rogervila/pymongo-cursor-json-encoder/archive/0.2.0.tar.gz',
    keywords=['pymongo', 'cursor', 'json', 'encoder'],
    install_requires=[
        'isodate',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
)
