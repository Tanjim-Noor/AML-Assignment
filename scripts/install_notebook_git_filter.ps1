param(
    [switch]$VerboseOutput
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$pythonExe = Join-Path $repoRoot ".venv\Scripts\python.exe"

if (-not (Test-Path -LiteralPath $pythonExe)) {
    throw "Workspace Python not found at '$pythonExe'."
}

$relativePython = ".venv/Scripts/python.exe"
$cleanCommand = "$relativePython -m nbstripout --extra-keys metadata.kernelspec --unix-newlines"
$textconvCommand = "$cleanCommand -t"

git -C $repoRoot config --replace-all filter.nbstripout.clean $cleanCommand
git -C $repoRoot config --replace-all filter.nbstripout.smudge cat
git -C $repoRoot config --replace-all filter.nbstripout.required true
git -C $repoRoot config --replace-all filter.nbstripout.extrakeys metadata.kernelspec
git -C $repoRoot config --replace-all diff.ipynb.textconv $textconvCommand

if ($VerboseOutput) {
    git -C $repoRoot config --get-regexp "^filter\.nbstripout\.|^diff\.ipynb\."
}

Write-Host "Configured nbstripout git filter for assignment notebooks."
