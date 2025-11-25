<#
.SYNOPSIS
    Automatically distribute Agent Factory agents to all repositories in the workspace.

.DESCRIPTION
    This script discovers all Git repositories in the parent workspace directory and 
    copies agents from the Agent Factory Warehouse to each repository's .github/agents/ 
    directory. It automatically excludes the agent-factory-warehouse itself.

.PARAMETER WorkspaceRoot
    Path to the workspace root containing multiple repositories. 
    Defaults to the parent directory of agent-factory-warehouse.

.PARAMETER Categories
    Array of category names to distribute (e.g., @("Debugging", "Testing")).
    If not specified, distributes all categories.

.PARAMETER Force
    Overwrite existing agents in target repositories.

.PARAMETER DryRun
    Show what would be copied without actually copying files.

.PARAMETER Exclude
    Array of repository names to exclude from distribution.

.PARAMETER IncludeNonGit
    Include directories that are not Git repositories.

.EXAMPLE
    .\DistributeAgents.ps1
    Discover and distribute all agents to all repositories in workspace.

.EXAMPLE
    .\DistributeAgents.ps1 -Categories @("Debugging", "Testing") -Force
    Distribute only Debugging and Testing agents, overwriting existing ones.

.EXAMPLE
    .\DistributeAgents.ps1 -DryRun
    Show what would be distributed without actually copying files.

.EXAMPLE
    .\DistributeAgents.ps1 -Exclude @("private-repo", "experimental") -Force
    Distribute to all repos except specified ones.
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $false)]
    [string]$WorkspaceRoot,

    [Parameter(Mandatory = $false)]
    [string[]]$Categories,

    [Parameter(Mandatory = $false)]
    [switch]$Force,

    [Parameter(Mandatory = $false)]
    [switch]$DryRun,

    [Parameter(Mandatory = $false)]
    [string[]]$Exclude = @(),

    [Parameter(Mandatory = $false)]
    [switch]$IncludeNonGit
)

# Get script directory and determine workspace root
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$AgentFactoryRoot = Split-Path -Parent $ScriptDir
$AgentsSourceDir = Join-Path $AgentFactoryRoot "agents"

# Default workspace root to parent of agent-factory-warehouse
if (-not $WorkspaceRoot) {
    $WorkspaceRoot = Split-Path -Parent $AgentFactoryRoot
}

# Available categories
$AvailableCategories = @(
    "Planning",
    "Debugging", 
    "Testing",
    "Validation",
    "GitSync",
    "BuildAutomation"
)

function Test-IsGitRepository {
    param([string]$Path)
    return Test-Path (Join-Path $Path ".git")
}

function Get-RepositoryInfo {
    param([string]$Path)
    
    $repoName = Split-Path -Leaf $Path
    $isGit = Test-IsGitRepository -Path $Path
    $hasAgentsDir = Test-Path (Join-Path $Path ".github\agents")
    $agentCount = 0
    
    if ($hasAgentsDir) {
        $agentFiles = Get-ChildItem -Path (Join-Path $Path ".github\agents") -Filter "*.agent.md" -ErrorAction SilentlyContinue
        $agentCount = $agentFiles.Count
    }
    
    return @{
        Name = $repoName
        Path = $Path
        IsGit = $isGit
        HasAgentsDir = $hasAgentsDir
        CurrentAgentCount = $agentCount
    }
}

function Get-AgentsByCategory {
    param([string]$Category)
    
    $categoryPath = Join-Path $AgentsSourceDir $Category
    if (Test-Path $categoryPath) {
        return Get-ChildItem -Path $categoryPath -Filter "*.agent.md"
    }
    return @()
}

function Get-AllAgents {
    param([string[]]$CategoriesToInclude)
    
    $allAgents = @()
    
    if (-not $CategoriesToInclude) {
        $CategoriesToInclude = $AvailableCategories
    }
    
    foreach ($category in $CategoriesToInclude) {
        $agents = Get-AgentsByCategory -Category $category
        foreach ($agent in $agents) {
            $allAgents += @{
                Category = $category
                Name = $agent.Name
                Path = $agent.FullName
            }
        }
    }
    
    return $allAgents
}

function Copy-AgentsToRepository {
    param(
        [hashtable]$RepoInfo,
        [array]$Agents,
        [bool]$Overwrite,
        [bool]$DryRunMode
    )
    
    $targetAgentsDir = Join-Path $RepoInfo.Path ".github\agents"
    $installedCount = 0
    $skippedCount = 0
    $errorCount = 0
    
    # Create .github/agents directory if needed
    if (-not $DryRunMode -and -not (Test-Path $targetAgentsDir)) {
        Write-Host "      [DIR] Creating directory: .github\agents" -ForegroundColor Cyan
        try {
            New-Item -ItemType Directory -Path $targetAgentsDir -Force | Out-Null
        }
        catch {
            Write-Error "      ❌ Failed to create directory: $_"
            return @{
                Installed = 0
                Skipped = 0
                Errors = 1
            }
        }
    }
    
    foreach ($agent in $Agents) {
        $targetPath = Join-Path $targetAgentsDir $agent.Name
        $action = ""
        
        # Check if agent already exists
        if ((Test-Path $targetPath) -and -not $Overwrite) {
            Write-Host "      [SKIP] Skip: $($agent.Name) (exists)" -ForegroundColor Gray
            $skippedCount++
            continue
        }
        
        if (Test-Path $targetPath) {
            $action = "[UPD] Update"
        } else {
            $action = "[ADD] Add"
        }
        
        if ($DryRunMode) {
            Write-Host "      [DRY RUN] $action`: $($agent.Name)" -ForegroundColor Yellow
        } else {
            try {
                Copy-Item -Path $agent.Path -Destination $targetPath -Force
                Write-Host "      $action`: $($agent.Name)" -ForegroundColor Green
                $installedCount++
            }
            catch {
                Write-Error "      [ERR] Failed: $($agent.Name) - $_"
                $errorCount++
            }
        }
    }
    
    return @{
        Installed = $installedCount
        Skipped = $skippedCount  
        Errors = $errorCount
    }
}

# Main script execution

Write-Host "Agent Factory Warehouse - Automatic Distribution`n" -ForegroundColor Cyan

# Validate source directory
if (-not (Test-Path $AgentsSourceDir)) {
    Write-Error "Agents source directory not found: $AgentsSourceDir"
    exit 1
}

# Validate workspace root
if (-not (Test-Path $WorkspaceRoot)) {
    Write-Error "Workspace root not found: $WorkspaceRoot"
    exit 1
}

Write-Host "Workspace Root: $WorkspaceRoot" -ForegroundColor Cyan
Write-Host "Source Directory: $AgentsSourceDir`n" -ForegroundColor Cyan

# Get all agents to distribute
$agentsToDistribute = Get-AllAgents -CategoriesToInclude $Categories

if ($agentsToDistribute.Count -eq 0) {
    Write-Warning "No agents found to distribute."
    exit 0
}

# Group agents by category for display
$agentsByCategory = $agentsToDistribute | Group-Object Category
Write-Host "Agents to distribute:" -ForegroundColor Yellow
foreach ($categoryGroup in $agentsByCategory) {
    Write-Host "   • $($categoryGroup.Name): $($categoryGroup.Count) agent$(if($categoryGroup.Count -ne 1){'s'})" -ForegroundColor Green
}
Write-Host ""

# Discover repositories
Write-Host "Discovering repositories..." -ForegroundColor Cyan

$allDirectories = Get-ChildItem -Path $WorkspaceRoot -Directory
$repositories = @()
$skippedDirs = @()

foreach ($dir in $allDirectories) {
    $dirName = $dir.Name
    
    # Skip agent-factory-warehouse itself
    if ($dirName -eq "agent-factory-warehouse") {
        continue
    }
    
    # Skip excluded directories
    if ($Exclude -contains $dirName) {
        $skippedDirs += $dirName
        continue
    }
    
    $repoInfo = Get-RepositoryInfo -Path $dir.FullName
    
    # Skip non-Git directories unless explicitly included
    if (-not $repoInfo.IsGit -and -not $IncludeNonGit) {
        $skippedDirs += "$dirName (not a Git repo)"
        continue
    }
    
    $repositories += $repoInfo
}

if ($repositories.Count -eq 0) {
    Write-Warning "No repositories found to distribute agents to."
    if ($skippedDirs.Count -gt 0) {
        Write-Host "`nSkipped directories:" -ForegroundColor Yellow
        foreach ($skipped in $skippedDirs) {
            Write-Host "   • $skipped" -ForegroundColor Gray
        }
    }
    exit 0
}

# Display discovered repositories
Write-Host "Discovered $($repositories.Count) repositor$(if($repositories.Count -ne 1){'ies'}):" -ForegroundColor Green
foreach ($repo in $repositories) {
    $gitIndicator = if ($repo.IsGit) { "[GIT]" } else { "[DIR]" }
    $agentIndicator = if ($repo.HasAgentsDir) { " ($($repo.CurrentAgentCount) agents)" } else { "" }
    Write-Host "   $gitIndicator $($repo.Name)$agentIndicator" -ForegroundColor White
}

if ($skippedDirs.Count -gt 0) {
    Write-Host "`nSkipped directories:" -ForegroundColor Yellow
    foreach ($skipped in $skippedDirs) {
        Write-Host "   • $skipped" -ForegroundColor Gray
    }
}

Write-Host ""

# Confirmation prompt (unless Force or DryRun)
if (-not $Force -and -not $DryRun) {
    Write-Host "Proceed with distribution? (Y/N): " -NoNewline -ForegroundColor Yellow
    $confirm = Read-Host
    if ($confirm -ine 'Y') {
        Write-Host "Distribution cancelled." -ForegroundColor Yellow
        exit 0
    }
    Write-Host ""
}

if ($DryRun) {
    Write-Host "DRY RUN MODE - No files will be copied`n" -ForegroundColor Yellow
}

# Distribute agents to each repository
$totalInstalled = 0
$totalSkipped = 0
$totalErrors = 0

foreach ($repo in $repositories) {
    Write-Host "Processing: $($repo.Name)" -ForegroundColor Cyan
    
    $result = Copy-AgentsToRepository -RepoInfo $repo -Agents $agentsToDistribute -Overwrite $Force.IsPresent -DryRunMode $DryRun.IsPresent
    
    $totalInstalled += $result.Installed
    $totalSkipped += $result.Skipped
    $totalErrors += $result.Errors
    
    if (-not $DryRun) {
        Write-Host "      [STATS] $($result.Installed) installed, $($result.Skipped) skipped, $($result.Errors) errors" -ForegroundColor White
    }
    Write-Host ""
}

# Final summary
$separator = "=" * 70
Write-Host $separator -ForegroundColor Cyan
Write-Host "Distribution Summary" -ForegroundColor Cyan  
Write-Host $separator -ForegroundColor Cyan

if ($DryRun) {
    Write-Host "DRY RUN - No actual changes made" -ForegroundColor Yellow
}

Write-Host "Repositories processed: $($repositories.Count)" -ForegroundColor White
Write-Host "Total agents: $($agentsToDistribute.Count)" -ForegroundColor White

if (-not $DryRun) {
    Write-Host "[OK] Installed/Updated: $totalInstalled" -ForegroundColor Green
    Write-Host "[SKIP] Skipped: $totalSkipped" -ForegroundColor Gray
    Write-Host "[ERR] Errors: $totalErrors" -ForegroundColor Red
}

if ($totalInstalled -gt 0 -and -not $DryRun) {
    Write-Host "`nNext Steps:" -ForegroundColor Yellow
    Write-Host "   1. Reload VSCode windows for affected repositories"
    Write-Host "   2. Open Copilot Chat to see the new agents"
    Write-Host "   3. Test agents with sample prompts"
}

if ($DryRun) {
    Write-Host "`nTo actually distribute agents, run:" -ForegroundColor Yellow
    $command = ".\DistributeAgents.ps1"
    if ($Categories) {
        $categoriesStr = ($Categories | ForEach-Object { "'$_'" }) -join ", "
        $command += " -Categories @($categoriesStr)"
    }
    if ($Force) {
        $command += " -Force"
    }
    Write-Host "   $command" -ForegroundColor Cyan
}

Write-Host ""