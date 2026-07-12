param(
    [switch]$VerboseOutput,
    [string[]]$AdditionalPreserveRelativePaths = @()
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$pythonExe = Join-Path $repoRoot ".venv\Scripts\python.exe"

if (-not (Test-Path -LiteralPath $pythonExe)) {
    throw "Workspace Python not found at '$pythonExe'."
}

$targetDirs = @(
    "Learning Materials Application on Assigment",
    "Final Assignment",
    "Assignment Report"
) | ForEach-Object { Join-Path $repoRoot $_ }

$notebooks = foreach ($dir in $targetDirs) {
    if (Test-Path -LiteralPath $dir) {
        Get-ChildItem -LiteralPath $dir -Recurse -File -Filter "*.ipynb"
    }
}

$preserveOutputPaths = @(
    (Join-Path $repoRoot "Final Assignment\notebooks\05_essential_gpa_change_regression.ipynb"),
    (Join-Path $repoRoot "Final Assignment\notebooks\06_comprehensive_gpa_change_regression.ipynb"),
    (Join-Path $repoRoot "Final Assignment\Deep Learning Experiments\01_category_embedding_mlp.ipynb"),
    (Join-Path $repoRoot "Final Assignment\Deep Learning Experiments\02_ft_transformer.ipynb"),
    (Join-Path $repoRoot "Final Assignment\Deep Learning Experiments\03_tabm.ipynb")
)
$preserveOutputPaths += @(
    $AdditionalPreserveRelativePaths |
        ForEach-Object { Join-Path $repoRoot $_ }
)

$preservedNotebooks = @(
    $notebooks | Where-Object { $preserveOutputPaths -contains $_.FullName }
)

$notebooks = @(
    $notebooks | Where-Object { $preserveOutputPaths -notcontains $_.FullName }
)

if (-not $notebooks) {
    Write-Host "No notebooks found in assignment notebook scopes."
    exit 0
}

function Convert-ToUnixNewlines {
    param(
        [Parameter(Mandatory = $true)]
        [System.IO.FileInfo[]]$Files
    )

    $utf8Strict = [System.Text.UTF8Encoding]::new($false, $true)
    $utf8NoBom = [System.Text.UTF8Encoding]::new($false)

    foreach ($file in $Files) {
        $content = [System.IO.File]::ReadAllText($file.FullName, $utf8Strict)
        $normalized = $content.Replace("`r`n", "`n").Replace("`r", "`n")

        if ($normalized -ne $content) {
            [System.IO.File]::WriteAllText($file.FullName, $normalized, $utf8NoBom)
        }
    }
}

$nbstripoutArgs = @(
    "-m",
    "nbstripout",
    "--extra-keys",
    "metadata.kernelspec",
    "--unix-newlines"
) + ($notebooks | ForEach-Object { $_.FullName })

if ($VerboseOutput) {
    Write-Host "Running nbstripout on $($notebooks.Count) notebook(s)..."
}

& $pythonExe @nbstripoutArgs

Convert-ToUnixNewlines -Files $notebooks
if ($preservedNotebooks) {
    Convert-ToUnixNewlines -Files $preservedNotebooks
}

Write-Host "Stripped notebook metadata/output for $($notebooks.Count) notebook(s)."
if ($preservedNotebooks) {
    Write-Host "Preserved executed outputs for $($preservedNotebooks.Count) designated notebook(s)."
}
