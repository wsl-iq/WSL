Write-Host "Starting to remove all WSL distributions..."
wsl --list --all | ForEach-Object {
    $line = $_.Trim()
    if ($line -notmatch 'NAME|STATE|VERSION' -and $line -ne '') {
        $name = $line -replace '\s+.*$', ''
        Write-Host "Removing distribution: $name"
        wsl --unregister $name
    }
}

Write-Host "Disabling WSL features..."
Disable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux -NoRestart
Disable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform -NoRestart

Write-Host "Removing WSL virtual network interfaces..."
Get-NetAdapter | Where-Object { $_.Name -like "*WSL*" } | ForEach-Object { 
    Write-Host "Removing network interface: $($_.Name)"
    Remove-NetAdapter -Name $_.Name -Confirm:$false 
}

Write-Host "Cleaning up WSL files from AppData for user: $env:USERNAME..."
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\Packages\*Ubuntu*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\Packages\*Canonical*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\Packages\*Debian*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\Packages\*SUSE*" -ErrorAction SilentlyContinue

Write-Host "Cleaning WSL related system files..."
Remove-Item -Recurse -Force "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\WSL*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "C:\Users\$env:USERNAME\AppData\Local\lxss" -ErrorAction SilentlyContinue

Write-Host "Restarting your system to finalize the uninstallation..."
Restart-Computer -Force
