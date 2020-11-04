Sub ExtractSpecificTables()
  Dim objTable As Table
  Dim objDoc As Document
  Dim objNewDoc As Document
  Dim objRange As Range
  Dim strTable As String
 
  strTable = InputBox("Enter the table number: ")
  Set objDoc = ActiveDocument
  Set objNewDoc = Documents.Add
 
  objDoc.Tables(strTable).Range.Select
  Selection.Copy
 
  Set objRange = objNewDoc.Range
  objRange.Collapse Direction:=wdCollapseEnd
  objRange.PasteSpecial DataType:=wdPasteRTF
 
End Sub