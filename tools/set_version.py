'''Set the version-dependent link in the project homepage.
'''
import sys

INDEX_FILES = ('../docs/index.md', '../docs/index-en.md')
PLACEHOLDER = '0.99.0'


def set_version(version):

    for indexFile in INDEX_FILES:

        with open(indexFile, 'r', encoding='utf-8') as f:
            text = f.read()

        with open(indexFile, 'w', encoding='utf-8') as f:
            f.write(text.replace(PLACEHOLDER, version))


if __name__ == '__main__':
    version = sys.argv[1]
    set_version(version)
