# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['JP.py', 'JP_UI.py'],
             pathex=['E:\\JP2'],
             binaries=[],
             datas=[('.\\data','.\\data'),(HOMEPATH + '\\PyQt5\\Qt\\bin\Qt5Core.dll','PyQt5\\Qt\\bin'),(HOMEPATH + '\\PyQt5\\Qt\\plugins\\platforms', 'PyQt5\\Qt\\plugins\\platforms'),(HOMEPATH + '\\PyQt5\\Qt\\plugins\\imageformats', 'PyQt5\\Qt\\plugins\\imageformats')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='日文词频助手',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          upx_exclude=['C:\\Users\\Administrator\\Downloads\\upx-3.95-win64\\upx-3.95-win64'],
          runtime_tmpdir=None,
          console=False , icon='.\\data\\c.ico')
