<#
.SYNOPSIS
    Install Agent Factory agents into a target repository.

.DESCRIPTION
    This script copies agent files from the Agent Factory Warehouse to a target repository's
    .github/agents/ directory. Supports installing all agents, specific categories, or 
    individual agents.

.PARAMETER TargetRepo
    Path to the target repository where agents should be installed.

.PARAMETER Categories
    Array of category names to install (e.g., @("Debugging", "Testing", "GitSync")).
    If not specified with -InstallAll, prompts user to select categories.

.PARAMETER InstallAll
    Install all agents from all categories.

.PARAMETER Force
    Overwrite existing agents in the target repository.

.PARAMETER List
    List available agents and categories without installing.

.EXAMPLE
    .\InstallAgents.ps1 -TargetRepo "C:\projects\my-app" -InstallAll
    Install all agents to the target repository.

.EXAMPLE
    .\InstallAgents.ps1 -TargetRepo "C:\projects\my-app" -Categories @("Debugging", "Testing")
    Install only Debugging and Testing agents.

.EXAMPLE
    .\InstallAgents.ps1 -List
    List all available agents and categories.

.EXAMPLE
    .\InstallAgents.ps1 -TargetRepo "C:\projects\my-app" -InstallAll -Force
    Install all agents, overwriting any existing agents.
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $false)]
    [string]$TargetRepo,

    [Parameter(Mandatory = $false)]
    [string[]]$Categories,

    [Parameter(Mandatory = $false)]
    [switch]$InstallAll,

    [Parameter(Mandatory = $false)]
    [switch]$Force,

    [Parameter(Mandatory = $false)]
    [switch]$List
)

# Get script directory (agent-factory-warehouse/scripts/)
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoRoot = Split-Path -Parent $ScriptDir
$AgentsDir = Join-Path $RepoRoot "agents"

# Available categories
$AvailableCategories = @(
    "Planning",
    "Debugging",
    "Testing",
    "Validation",
    "GitSync",
    "BuildAutomation",
    "SmartContracts"
)

function Show-AgentList {
    Write-Host "`n🏭 Agent Factory Warehouse - Available Agents`n" -ForegroundColor Cyan
    
    foreach ($category in $AvailableCategories) {
        $categoryPath = Join-Path $AgentsDir $category
        if (Test-Path $categoryPath) {
            Write-Host "📁 $category" -ForegroundColor Yellow
            
            $agents = Get-ChildItem -Path $categoryPath -Filter "*.agent.md"
            foreach ($agent in $agents) {
                $agentName = $agent.BaseName
                Write-Host "   └─ $agentName" -ForegroundColor Green
            }
            Write-Host ""
        }
    }
}

function Get-AgentsByCategory {
    param([string]$Category)
    
    $categoryPath = Join-Path $AgentsDir $Category
    if (Test-Path $categoryPath) {
        return Get-ChildItem -Path $categoryPath -Filter "*.agent.md"
    }
    return @()
}

function Install-Agents {
    param(
        [string]$Target,
        [string[]]$CategoriesToInstall,
        [bool]$Overwrite
    )
    
    # Validate target directory
    if (-not (Test-Path $Target)) {
        Write-Error "Target repository does not exist: $Target"
        return
    }
    
    # Create .github/agents directory
    $targetAgentsDir = Join-Path $Target ".github\agents"
    if (-not (Test-Path $targetAgentsDir)) {
        Write-Host "Creating directory: $targetAgentsDir" -ForegroundColor Cyan
        New-Item -ItemType Directory -Path $targetAgentsDir -Force | Out-Null
    }
    
    $installedCount = 0
    $skippedCount = 0
    $errorCount = 0
    
    foreach ($category in $CategoriesToInstall) {
        Write-Host "`n📦 Installing agents from category: $category" -ForegroundColor Yellow
        
        $agents = Get-AgentsByCategory -Category $category
        
        if ($agents.Count -eq 0) {
            Write-Warning "No agents found in category: $category"
            continue
        }
        
        foreach ($agent in $agents) {
            $targetPath = Join-Path $targetAgentsDir $agent.Name
            
            # Check if agent already exists
            if ((Test-Path $targetPath) -and -not $Overwrite) {
                Write-Host "   ⏭️  Skipped: $($agent.Name) (already exists, use -Force to overwrite)" -ForegroundColor Gray
                $skippedCount++
                continue
            }
            
            try {
                Copy-Item -Path $agent.FullName -Destination $targetPath -Force
                if ($Overwrite -and (Test-Path $targetPath)) {
                    Write-Host "   ♻️  Updated: $($agent.Name)" -ForegroundColor Green
                } else {
                    Write-Host "   ✅ Installed: $($agent.Name)" -ForegroundColor Green
                }
                $installedCount++
            }
            catch {
                Write-Error "   ❌ Failed to install: $($agent.Name) - $_"
                $errorCount++
            }
        }
    }
    
    # Summary
    Write-Host "`n" + ("=" * 60) -ForegroundColor Cyan
    Write-Host "📊 Installation Summary" -ForegroundColor Cyan
    Write-Host ("=" * 60) -ForegroundColor Cyan
    Write-Host "✅ Installed/Updated: $installedCount" -ForegroundColor Green
    Write-Host "⏭️  Skipped: $skippedCount" -ForegroundColor Gray
    Write-Host "❌ Errors: $errorCount" -ForegroundColor Red
    Write-Host "`n📍 Target: $targetAgentsDir" -ForegroundColor Cyan
    
    if ($installedCount -gt 0) {
        Write-Host "`n💡 Next Steps:" -ForegroundColor Yellow
        Write-Host "   1. Reload VSCode window (Ctrl+Shift+P → 'Developer: Reload Window')"
        Write-Host "   2. Open Copilot Chat"
        Write-Host "   3. Click the agent dropdown to see your new agents"
    }
}

# Main script logic

if ($List) {
    Show-AgentList
    exit 0
}

# Validate TargetRepo is provided when not listing
if (-not $TargetRepo) {
    Write-Error "TargetRepo parameter is required. Use -List to see available agents."
    Write-Host "`nUsage examples:" -ForegroundColor Yellow
    Write-Host "   .\InstallAgents.ps1 -List"
    Write-Host "   .\InstallAgents.ps1 -TargetRepo 'C:\projects\my-app' -InstallAll"
    Write-Host "   .\InstallAgents.ps1 -TargetRepo 'C:\projects\my-app' -Categories @('Debugging', 'Testing')"
    exit 1
}

# Determine which categories to install
$categoriesToInstall = @()

if ($InstallAll) {
    $categoriesToInstall = $AvailableCategories
    Write-Host "📦 Installing ALL agent categories..." -ForegroundColor Cyan
}
elseif ($Categories -and $Categories.Count -gt 0) {
    # Validate provided categories
    foreach ($cat in $Categories) {
        if ($AvailableCategories -contains $cat) {
            $categoriesToInstall += $cat
        }
        else {
            Write-Warning "Unknown category: $cat (will be skipped)"
        }
    }
}
else {
    # Interactive category selection
    Write-Host "`n🏭 Agent Factory Warehouse - Category Selection`n" -ForegroundColor Cyan
    Write-Host "Available categories:" -ForegroundColor Yellow
    
    for ($i = 0; $i -lt $AvailableCategories.Count; $i++) {
        $category = $AvailableCategories[$i]
        $agents = Get-AgentsByCategory -Category $category
        Write-Host "   [$($i + 1)] $category ($($agents.Count) agent$(if($agents.Count -ne 1){'s'}))"
    }
    Write-Host "   [A] All categories"
    Write-Host "   [Q] Quit"
    
    Write-Host "`nEnter category numbers separated by commas (e.g., 1,2,3) or 'A' for all: " -NoNewline -ForegroundColor Cyan
    $selection = Read-Host
    
    if ($selection -ieq 'Q') {
        Write-Host "Installation cancelled." -ForegroundColor Yellow
        exit 0
    }
    elseif ($selection -ieq 'A') {
        $categoriesToInstall = $AvailableCategories
    }
    else {
        $indices = $selection -split ',' | ForEach-Object { $_.Trim() }
        foreach ($index in $indices) {
            if ($index -match '^\d+$') {
                $idx = [int]$index - 1
                if ($idx -ge 0 -and $idx -lt $AvailableCategories.Count) {
                    $categoriesToInstall += $AvailableCategories[$idx]
                }
            }
        }
    }
}

if ($categoriesToInstall.Count -eq 0) {
    Write-Warning "No categories selected. Nothing to install."
    exit 0
}

# Confirm installation
Write-Host "`n📋 Categories to install:" -ForegroundColor Cyan
foreach ($cat in $categoriesToInstall) {
    $agents = Get-AgentsByCategory -Category $cat
    Write-Host "   • $cat ($($agents.Count) agent$(if($agents.Count -ne 1){'s'}))" -ForegroundColor Green
}

Write-Host "`n🎯 Target: $TargetRepo" -ForegroundColor Cyan

if (-not $Force) {
    Write-Host "`nProceed with installation? (Y/N): " -NoNewline -ForegroundColor Yellow
    $confirm = Read-Host
    if ($confirm -ine 'Y') {
        Write-Host "Installation cancelled." -ForegroundColor Yellow
        exit 0
    }
}

# Install agents
Install-Agents -Target $TargetRepo -CategoriesToInstall $categoriesToInstall -Overwrite $Force.IsPresent
