#!/usr/bin/env python3
"""
generate_repo.py — Builds addons.xml and addons.xml.md5 for DepotQuebecPerso.
Run this script whenever you update a plugin version.
"""

import hashlib
from pathlib import Path
from xml.etree import ElementTree as ET

REPO_ROOT = Path(__file__).parent
ADDONS_XML = REPO_ROOT / 'addons.xml'
ADDONS_MD5 = REPO_ROOT / 'addons.xml.md5'


def build():
    root_el = ET.Element('addons')

    for addon_xml in sorted(REPO_ROOT.glob('*/addon.xml')):
        try:
            tree = ET.parse(addon_xml)
            addon_el = tree.getroot()
            if addon_el.tag == 'addon':
                root_el.append(addon_el)
                print(f'  ✓ {addon_xml.parent.name}')
        except ET.ParseError as e:
            print(f'  ✗ Skipped {addon_xml.parent.name}: {e}')

    ET.indent(root_el, space='  ')
    content = '<?xml version="1.0" encoding="UTF-8"?>\n' + ET.tostring(root_el, encoding='unicode')

    ADDONS_XML.write_text(content, encoding='utf-8')
    md5 = hashlib.md5(content.encode('utf-8')).hexdigest()
    ADDONS_MD5.write_text(md5)

    print(f'\nWritten: addons.xml + addons.xml.md5 ({md5})')


if __name__ == '__main__':
    print('Building addons.xml...\n')
    build()
