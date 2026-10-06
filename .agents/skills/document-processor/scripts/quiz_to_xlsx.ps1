<#
.SYNOPSIS
    Converts a Quiz markdown file into a Quizizz-compatible Excel (.xlsx) file using the Quizizz template.
#>

[CmdletBinding()]
param (
    [Parameter(Mandatory = $true)]
    [string]$InputMarkdown,

    [Parameter(Mandatory = $false)]
    [string]$OutputXlsx,

    [Parameter(Mandatory = $false)]
    [string]$TemplatePath
)

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8

Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem

# 1. Resolve paths
$mdFile = (Get-Item $InputMarkdown -ErrorAction Stop).FullName
$workspaceRoot = (Get-Location).Path

if (-not $TemplatePath) {
    $candidate = Join-Path $workspaceRoot "QuizizzSampleSpreadsheetUpdated_v2.xlsx"
    if (Test-Path $candidate) {
        $TemplatePath = $candidate
    } else {
        $candidate = "d:\งานโก้\teacher\QuizizzSampleSpreadsheetUpdated_v2.xlsx"
        if (Test-Path $candidate) {
            $TemplatePath = $candidate
        } else {
            throw "Quizizz template 'QuizizzSampleSpreadsheetUpdated_v2.xlsx' not found!"
        }
    }
} else {
    $TemplatePath = (Get-Item $TemplatePath -ErrorAction Stop).FullName
}

if (-not $OutputXlsx) {
    $OutputXlsx = [System.IO.Path]::ChangeExtension($mdFile, ".xlsx")
} else {
    $OutputXlsx = [System.IO.Path]::GetFullPath($OutputXlsx)
}

Write-Host "Processing: $mdFile" -ForegroundColor Cyan
Write-Host "Template  : $TemplatePath" -ForegroundColor Gray
Write-Host "Target    : $OutputXlsx" -ForegroundColor Gray

# 2. Parse Markdown Quiz
$mdContent = [System.IO.File]::ReadAllText($mdFile, [System.Text.Encoding]::UTF8)

# Split by question blocks e.g. "### " or "---"
$blocks = [System.Text.RegularExpressions.Regex]::Split($mdContent, "(?m)^(?=###\s+)")

$questions = [System.Collections.Generic.List[PSObject]]::new()

foreach ($block in $blocks) {
    $trimmed = $block.Trim()
    if ([string]::IsNullOrWhiteSpace($trimmed)) { continue }
    
    # Check if block contains options
    $optMatches = [System.Text.RegularExpressions.Regex]::Matches($trimmed, "(?m)^\s*-\s*\[([ xX])\]\s*([A-Da-d0-9\.\)]+)\s*(.+)$")
    if ($optMatches.Count -lt 2) { continue }

    $lines = $trimmed -split "\r?\n"
    $qText = ""
    $expText = ""
    $options = @()
    $correctIndex = 1

    # Extract question text (line containing **...:** before options)
    foreach ($line in $lines) {
        $l = $line.Trim()
        if ($l -match "^\s*-\s*\[") { break }
        if ($l -match "^\s*\*\*.*?\*\*\s*(.+)$") {
            $qText = $matches[1].Trim()
        } elseif ($l -match "^[^#\*\-\s].*?[?:\.]$" -and -not $qText) {
            $qText = $l
        }
    }

    # Extract options
    $oIdx = 1
    foreach ($m in $optMatches) {
        $isCheck = $m.Groups[1].Value.Trim()
        $optText = $m.Groups[3].Value.Trim()
        $options += $optText
        if ($isCheck -eq "x" -or $isCheck -eq "X") {
            $correctIndex = $oIdx
        }
        $oIdx++
    }

    # Extract explanation (line with **...:** occurring after options)
    $foundOptions = $false
    foreach ($line in $lines) {
        $l = $line.Trim()
        if ($l -match "^\s*-\s*\[") {
            $foundOptions = $true
            continue
        }
        if ($foundOptions -and $l -match "^\s*\*\*.*?\*\*\s*(.+)$") {
            $expText = $matches[1].Trim()
            break
        }
    }

    if ($qText -and $options.Count -ge 2) {
        $o1 = if ($options.Count -ge 1) { $options[0] } else { "" }
        $o2 = if ($options.Count -ge 2) { $options[1] } else { "" }
        $o3 = if ($options.Count -ge 3) { $options[2] } else { "" }

        $qObj = [PSCustomObject]@{
            QuestionText = $qText
            QuestionType = "Multiple Choice"
            Option1      = $o1
            Option2      = $o2
            Option3      = $o3
            CorrectAnswer= $correctIndex
            TimeSeconds  = 60
            ImageLink    = ""
            Explanation  = $expText
        }
        $questions.Add($qObj)
    }
}

if ($questions.Count -eq 0) {
    throw "No questions successfully parsed from $mdFile"
}

Write-Host "Parsed $($questions.Count) questions successfully." -ForegroundColor Green

# 3. Create Safe Copy of Template and Extract
$tempCopy = Join-Path $env:TEMP ("quiz_copy_" + [System.Guid]::NewGuid().ToString("N") + ".xlsx")
$inStream = New-Object System.IO.FileStream($TemplatePath, [System.IO.FileMode]::Open, [System.IO.FileAccess]::Read, [System.IO.FileShare]::ReadWrite)
$outStream = New-Object System.IO.FileStream($tempCopy, [System.IO.FileMode]::Create, [System.IO.FileAccess]::Write)
$inStream.CopyTo($outStream)
$inStream.Close()
$outStream.Close()

$extractDir = Join-Path $env:TEMP ("quiz_extract_" + [System.Guid]::NewGuid().ToString("N"))
[System.IO.Compression.ZipFile]::ExtractToDirectory($tempCopy, $extractDir)
Remove-Item $tempCopy -Force

$extractDirNorm = (Get-Item $extractDir).FullName.TrimEnd('\')

# 4. Process xl/sharedStrings.xml
$ssPath = Join-Path $extractDirNorm "xl\sharedStrings.xml"
$rawSsXml = [System.IO.File]::ReadAllText($ssPath, [System.Text.Encoding]::UTF8)
$ssXml = [xml]$rawSsXml

$script:stringList = [System.Collections.Generic.List[string]]::new()
$script:stringDict = [System.Collections.Generic.Dictionary[string, int]]::new()

# Preserve header strings
$idx = 0
foreach ($si in $ssXml.sst.si) {
    $tVal = $si.InnerText
    $script:stringList.Add($tVal)
    if (-not $script:stringDict.ContainsKey($tVal)) {
        $script:stringDict[$tVal] = $idx
    }
    $idx++
}

function Get-OrAddString([string]$text) {
    if ([string]::IsNullOrEmpty($text)) { $text = "" }
    if ($script:stringDict.ContainsKey($text)) {
        return $script:stringDict[$text]
    }
    $newIdx = $script:stringList.Count
    $script:stringList.Add($text)
    $script:stringDict[$text] = $newIdx
    return $newIdx
}

function Escape-Xml([string]$str) {
    if ([string]::IsNullOrEmpty($str)) { return "" }
    return [System.Security.SecurityElement]::Escape($str)
}

# 5. Build rows 2 to (1 + N)
$rowXmlSb = New-Object System.Text.StringBuilder
for ($i=0; $i -lt $questions.Count; $i++) {
    $rowNum = $i + 2
    $q = $questions[$i]

    $qId   = Get-OrAddString $q.QuestionText
    $tId   = Get-OrAddString $q.QuestionType
    $o1Id  = Get-OrAddString $q.Option1
    $o2Id  = Get-OrAddString $q.Option2
    $o3Id  = Get-OrAddString $q.Option3
    $expId = Get-OrAddString $q.Explanation

    [void]$rowXmlSb.Append("<row r=`"$rowNum`" spans=`"1:9`" ht=`"97.5`" customHeight=`"1`">")
    [void]$rowXmlSb.Append("<c r=`"A$rowNum`" t=`"s`"><v>$qId</v></c>")
    [void]$rowXmlSb.Append("<c r=`"B$rowNum`" t=`"s`"><v>$tId</v></c>")
    [void]$rowXmlSb.Append("<c r=`"C$rowNum`" t=`"s`"><v>$o1Id</v></c>")
    [void]$rowXmlSb.Append("<c r=`"D$rowNum`" t=`"s`"><v>$o2Id</v></c>")
    [void]$rowXmlSb.Append("<c r=`"E$rowNum`" t=`"s`"><v>$o3Id</v></c>")
    [void]$rowXmlSb.Append("<c r=`"F$rowNum`"><v>$($q.CorrectAnswer)</v></c>")
    [void]$rowXmlSb.Append("<c r=`"G$rowNum`"><v>$($q.TimeSeconds)</v></c>")
    [void]$rowXmlSb.Append("<c r=`"H$rowNum`"/>")
    [void]$rowXmlSb.Append("<c r=`"I$rowNum`" t=`"s`"><v>$expId</v></c>")
    [void]$rowXmlSb.Append("</row>")
}

# 6. Save updated xl/sharedStrings.xml
$ssXmlSb = New-Object System.Text.StringBuilder
[void]$ssXmlSb.Append('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>')
[void]$ssXmlSb.Append("<sst xmlns=`"http://schemas.openxmlformats.org/spreadsheetml/2006/main`" count=`"$($script:stringList.Count)`" uniqueCount=`"$($script:stringList.Count)`">")
foreach ($s in $script:stringList) {
    $esc = Escape-Xml $s
    [void]$ssXmlSb.Append("<si><t xml:space=`"preserve`">$esc</t></si>")
}
[void]$ssXmlSb.Append('</sst>')
[System.IO.File]::WriteAllText($ssPath, $ssXmlSb.ToString(), [System.Text.Encoding]::UTF8)

# 7. Update xl/worksheets/sheet1.xml
$sheetPath = Join-Path $extractDirNorm "xl\worksheets\sheet1.xml"
$rawSheetXml = [System.IO.File]::ReadAllText($sheetPath, [System.Text.Encoding]::UTF8)

$row1EndMatch = [System.Text.RegularExpressions.Regex]::Match($rawSheetXml, '<row\s+r="1"[\s\S]*?</row>')
if ($row1EndMatch.Success) {
    $beforeRows = $rawSheetXml.Substring(0, $row1EndMatch.Index + $row1EndMatch.Length)
} else {
    $sheetDataPos = $rawSheetXml.IndexOf('<sheetData>')
    if ($sheetDataPos -ge 0) {
        $beforeRows = $rawSheetXml.Substring(0, $sheetDataPos + '<sheetData>'.Length)
    } else {
        throw "Could not locate <sheetData> in sheet1.xml"
    }
}

$sheetDataEndPos = $rawSheetXml.IndexOf('</sheetData>')
if ($sheetDataEndPos -lt 0) {
    throw "Could not locate </sheetData> in sheet1.xml"
}
$afterRows = $rawSheetXml.Substring($sheetDataEndPos)

$lastRow = $questions.Count + 1
$beforeRows = $beforeRows -replace '<dimension ref="[^"]*"', "<dimension ref=`"A1:I$lastRow`""

$newSheetXml = $beforeRows + $rowXmlSb.ToString() + $afterRows
[System.IO.File]::WriteAllText($sheetPath, $newSheetXml, [System.Text.Encoding]::UTF8)

# 8. Re-pack cleanly into target .xlsx
$outDir = [System.IO.Path]::GetDirectoryName($OutputXlsx)
if (-not (Test-Path $outDir)) {
    [System.IO.Directory]::CreateDirectory($outDir) | Out-Null
}
if (Test-Path $OutputXlsx) { Remove-Item $OutputXlsx -Force }

$zip = [System.IO.Compression.ZipFile]::Open($OutputXlsx, [System.IO.Compression.ZipArchiveMode]::Create)
$allFiles = Get-ChildItem -Path $extractDirNorm -Recurse -File
foreach ($file in $allFiles) {
    $full = $file.FullName
    $rel = $full.Substring($extractDirNorm.Length).TrimStart('\', '/').Replace('\', '/')
    [System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile($zip, $full, $rel) | Out-Null
}
$zip.Dispose()

# Cleanup
Remove-Item $extractDirNorm -Recurse -Force

Write-Host "SUCCESS: Generated Quizizz Excel file -> $OutputXlsx" -ForegroundColor Green
