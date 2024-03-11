# -*- mode: python ; coding: utf-8 -*-
import sys ; sys.setrecursionlimit(sys.getrecursionlimit() * 5)

a = Analysis(
    ['GUI.py'],
    pathex=[],
    binaries=[],
    datas=[("venv/Lib/site-packages/pyopenms", "./pyopenms/"),('Endogenius_Thumbnail.ico', '.'),('assets', 'assets')],
    hiddenimports=[],
    hookspath=['C:\\Users\\lawashburn\\Documents\\EndoGeniusDistributions\\EndoGenius_v1.0.2\\hooks'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='EndoGenius',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['EndoGenius.ico'],
)
