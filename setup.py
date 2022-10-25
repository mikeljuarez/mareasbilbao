from distutils.core import setup
setup(
  name = 'mareasbilbao',
  packages = ['mareasbilbao'],
  version = '0.1',
  license='MIT',
  description = 'Get to know the tides of bilbao',
  author = 'Mikel Juarez',
  author_email = 'mikel.juarez@alumni.mondragon.edu',
  url = 'https://github.com/mikeljuarez/mareasbilbao',
  download_url = 'https://github.com/mikeljuarez/mareasbilbao/archive/refs/tags/0.11.tar.gz',
  keywords = ['scraping', 'easy', 'scraper', 'website', 'download', 'links', 'images', 'videos'],
  install_requires=[
          'requests',
          'json',  
      ],
  classifiers=[  # Optional
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)
