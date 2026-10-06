<#
.SYNOPSIS
    Converts Reveal.js or HTML presentations into a high-fidelity Landscape PDF using Microsoft Edge headless.
#>

[CmdletBinding()]
param (
    [Parameter(Mandatory = $true)]
    [string]$InputHtml,

    [Parameter(Mandatory = $false)]
    [string]$OutputPdf,

    [Parameter(Mandatory = $false)]
    [ValidateSet("16:10", "16:9", "A4")]
    [string]$Size = "16:10"
)

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8

# 1. Locate Edge executable
$edgeCandidates = @(
    "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    "$env:LOCALAPPDATA\Microsoft\Edge\Application\msedge.exe"
)

$edgePath = $edgeCandidates | Where-Object { Test-Path $_ } | Select-Object -First 1

if (-not $edgePath) {
    $edgeCmd = Get-Command "msedge" -ErrorAction SilentlyContinue
    if ($edgeCmd) {
        $edgePath = $edgeCmd.Source
    } else {
        throw "Microsoft Edge executable not found on system!"
    }
}

# 2. Resolve Input and Output Paths
$htmlFile = (Get-Item $InputHtml -ErrorAction Stop).FullName
if (-not $OutputPdf) {
    $OutputPdf = [System.IO.Path]::ChangeExtension($htmlFile, ".pdf")
} else {
    $OutputPdf = [System.IO.Path]::GetFullPath($OutputPdf)
}

$outDir = [System.IO.Path]::GetDirectoryName($OutputPdf)
if (-not (Test-Path $outDir)) {
    [System.IO.Directory]::CreateDirectory($outDir) | Out-Null
}

if (Test-Path $OutputPdf) {
    Remove-Item $OutputPdf -Force -ErrorAction SilentlyContinue
}

# 3. Try converting via Playwright (html_to_pdf.py) for highest fidelity & font loading
$pyScript = Join-Path $PSScriptRoot "html_to_pdf.py"
$pythonCmd = Get-Command "python" -ErrorAction SilentlyContinue

if ($pythonCmd -and (Test-Path $pyScript)) {
    Write-Host "Converting with Playwright Engine : $htmlFile" -ForegroundColor Cyan
    Write-Host "Target PDF                       : $OutputPdf" -ForegroundColor Gray
    Write-Host "Page Size                        : $Size" -ForegroundColor DarkCyan
    
    & $pythonCmd.Source $pyScript $htmlFile $OutputPdf --size $Size
    
    if (Test-Path $OutputPdf) {
        $item = Get-Item $OutputPdf
        $sizeMb = [Math]::Round($item.Length / 1MB, 2)
        Write-Host "SUCCESS: Generated Landscape PDF ($sizeMb MB) -> $OutputPdf" -ForegroundColor Green
        exit 0
    }
}

# 4. Fallback: Construct 100% compliant AbsoluteUri with ?print-pdf & use Edge Headless
$uriObj = New-Object System.Uri($htmlFile)
$encodedUri = $uriObj.AbsoluteUri + "?print-pdf"

$winW = 1280
$winH = 800
if ($Size -eq "16:9") {
    $winH = 720
} elseif ($Size -eq "A4") {
    $winH = 905
}

Write-Host "Converting via Edge Headless : $htmlFile" -ForegroundColor Cyan
Write-Host "URI                          : $encodedUri" -ForegroundColor DarkCyan
Write-Host "Target PDF                   : $OutputPdf" -ForegroundColor Gray
Write-Host "Using Edge                   : $edgePath" -ForegroundColor Gray
Write-Host "Viewport Scale               : ${winW}x${winH} (Scale 2x)" -ForegroundColor DarkCyan

$process = Start-Process -FilePath $edgePath -ArgumentList @(
    "--headless=new",
    "--disable-gpu",
    "--allow-file-access-from-files",
    "--disable-web-security",
    "--window-size=$winW,$winH",
    "--force-device-scale-factor=2",
    "--virtual-time-budget=10000",
    "--run-all-compositor-stages-before-draw",
    "--no-pdf-header-footer",
    "--print-to-pdf=$OutputPdf",
    $encodedUri
) -PassThru -Wait

if (Test-Path $OutputPdf) {
    $item = Get-Item $OutputPdf
    $sizeMb = [Math]::Round($item.Length / 1MB, 2)
    Write-Host "SUCCESS: Generated PDF ($sizeMb MB) -> $OutputPdf" -ForegroundColor Green
} else {
    throw "Failed to generate PDF. Exit code: $($process.ExitCode)"
}
