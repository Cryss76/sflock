# Copyright (C) 2016-2017 Jurriaan Bremer.
# This file is part of SFlock - http://www.sflock.org/.
# See the file 'docs/LICENSE.txt' for copying permission.

from sflock.abstracts import File

def test_package():
    assert File(filename="a.pdf").package == "pdf"
    assert File(filename="a.rtf").package == "doc"
    assert File(filename="a.doc").package == "doc"
    assert File(filename="a.docx").package == "doc"
    assert File(filename="a.docm").package == "doc"
    assert File(filename="a.dot").package == "doc"
    assert File(filename="a.dotx").package == "doc"
    assert File(filename="a.docb").package == "doc"
    assert File(filename="a.mht").package == "ie"
    assert File(filename="a.mhtml").package == "ie"
    assert File(filename="a.mso").package == "doc"
    assert File(filename="a.xls").package == "xls"
    assert File(filename="a.xlsx").package == "xls"
    assert File(filename="a.xlm").package == "xls"
    assert File(filename="a.xlsx").package == "xls"
    assert File(filename="a.xlt").package == "xls"
    assert File(filename="a.xltx").package == "xls"
    assert File(filename="a.xlsm").package == "xls"
    assert File(filename="a.xltm").package == "xls"
    assert File(filename="a.xlsb").package == "xls"
    assert File(filename="a.xla").package == "xls"
    assert File(filename="a.xlam").package == "xls"
    assert File(filename="a.xll").package == "xls"
    assert File(filename="a.xlw").package == "xls"
    assert File(filename="a.ppt").package == "ppt"
    assert File(filename="a.pptx").package == "ppt"
    assert File(filename="a.pps").package == "ppt"
    assert File(filename="a.ppsx").package == "ppt"
    assert File(filename="a.pptm").package == "ppt"
    assert File(filename="a.potm").package == "ppt"
    assert File(filename="a.potx").package == "ppt"
    assert File(filename="a.ppsm").package == "ppt"
    assert File(filename="a.pot").package == "ppt"
    assert File(filename="a.ppam").package == "ppt"
    assert File(filename="a.sldx").package == "ppt"
    assert File(filename="a.sldm").package == "ppt"
    assert File(filename="a.pub").package == "pub"
    assert File(filename="a.jar").package == "jar"
    assert File(filename="a.py").package == "python"
    assert File(filename="a.pyc").package == "python"
    assert File(filename="a.pyo").package == "python"
    assert File(filename="a.vbs").package == "vbs"
    assert File(filename="a.js").package == "js"
    assert File(filename="a.jse").package == "js"
    assert File(filename="a.msi").package == "msi"
    assert File(filename="a.ps1").package == "ps1"
    assert File(filename="a.ps1xml").package == "ps1"
    assert File(filename="a.psc1").package == "ps1"
    assert File(filename="a.psm1").package == "ps1"
    assert File(filename="a.wsf").package == "wsf"
    assert File(filename="a.wsc").package == "wsf"
    assert File(filename="a.htm").package == "ie"
    assert File(filename="a.html").package == "ie"
    assert File(filename="a.bat").package == "generic"
    assert File(filename="a.cmd").package == "generic"
    assert File(filename="a.lnk").package == "generic"
    assert File(filename="a.hta").package == "ie"

def test_case():
    assert File(filename="A.PDF").package == "pdf"
    assert File(filename="A.RTF").package == "doc"
    assert File(filename="A.DOC").package == "doc"
    assert File(filename="A.PUB").package == "pub"
    assert File(filename="A.JAR").package == "jar"

def test_platform():
    assert File(filename="a.pdf").platform is None
    assert File(filename="a.rtf").platform == "windows"
    assert File(filename="a.doc").platform == "windows"
    assert File(filename="a.docx").platform == "windows"
    assert File(filename="a.docm").platform == "windows"
    assert File(filename="a.dot").platform == "windows"
    assert File(filename="a.dotx").platform == "windows"
    assert File(filename="a.docb").platform == "windows"
    assert File(filename="a.mht").platform == "windows"
    assert File(filename="a.mhtml").platform == "windows"
    assert File(filename="a.mso").platform == "windows"
    assert File(filename="a.xls").platform == "windows"
    assert File(filename="a.xlsx").platform == "windows"
    assert File(filename="a.xlm").platform == "windows"
    assert File(filename="a.xlsx").platform == "windows"
    assert File(filename="a.xlt").platform == "windows"
    assert File(filename="a.xltx").platform == "windows"
    assert File(filename="a.xlsm").platform == "windows"
    assert File(filename="a.xltm").platform == "windows"
    assert File(filename="a.xlsb").platform == "windows"
    assert File(filename="a.xla").platform == "windows"
    assert File(filename="a.xlam").platform == "windows"
    assert File(filename="a.xll").platform == "windows"
    assert File(filename="a.xlw").platform == "windows"
    assert File(filename="a.ppt").platform == "windows"
    assert File(filename="a.pptx").platform == "windows"
    assert File(filename="a.pps").platform == "windows"
    assert File(filename="a.ppsx").platform == "windows"
    assert File(filename="a.pptm").platform == "windows"
    assert File(filename="a.potm").platform == "windows"
    assert File(filename="a.potx").platform == "windows"
    assert File(filename="a.ppsm").platform == "windows"
    assert File(filename="a.pot").platform == "windows"
    assert File(filename="a.ppam").platform == "windows"
    assert File(filename="a.sldx").platform == "windows"
    assert File(filename="a.sldm").platform == "windows"
    assert File(filename="a.pub").platform == "windows"
    assert File(filename="a.jar").platform is None
    assert File(filename="a.py").platform is None
    assert File(filename="a.pyc").platform is None
    assert File(filename="a.pyo").platform is None
    assert File(filename="a.vbs").platform == "windows"
    assert File(filename="a.js").platform is None
    assert File(filename="a.jse").platform is None
    assert File(filename="a.msi").platform == "windows"
    assert File(filename="a.ps1").platform == "windows"
    assert File(filename="a.ps1xml").platform == "windows"
    assert File(filename="a.psc1").platform == "windows"
    assert File(filename="a.psm1").platform == "windows"
    assert File(filename="a.wsf").platform == "windows"
    assert File(filename="a.wsc").platform == "windows"
    assert File(filename="a.htm").platform == "windows"
    assert File(filename="a.html").platform == "windows"
    assert File(filename="a.bat").platform is None
    assert File(filename="a.cmd").platform is None
    assert File(filename="a.lnk").platform is None
    assert File(filename="a.hta").platform == "windows"
