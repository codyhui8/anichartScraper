# -*- mode: python -*-

block_cipher = None


a = Analysis(['seleniumMain.py'],
             pathex=['C:\\Users\\cody.hui\\PycharmProjects\\anichartScrapper'],
             binaries=[],
             datas=[('C:\\Users\\cody.hui\\PycharmProjects\\anichartScrapper\\drivers\\chromedriver.exe','.')],
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
          name='seleniumMain',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
