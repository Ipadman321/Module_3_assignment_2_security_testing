#Retrieves the classname Win32 with the specific subfile called Operating System
#from your computer.
$OS_information = Get-CimInstance -ClassName Win32_OperatingSystem

#Grabs the username of the account that it is currently running on
#and prints it with the users OS information.
Write-Output "$env:USERNAME's Operating System Information:"
Write-Output "-----------------------------"

#Grabs the OS name
Write-Output "Name: $($OS_information.Caption)"

#Grabs the OS Version number
Write-Output "Version: $($osVersion)"

#Grabs the Architecture of the OS
Write-Output "Architecture: $($OS_information.OSArchitecture)"

#Grabs the manufacturer of the OS
Write-Output "Manufacturer: $($OS_information.Manufacturer)"

#Grabs the last recorded boot time of the OS
Write-Output "Last Boot Up Time: $($OS_information.LastBootUpTime)"
Write-Output ""

#Retrieves the classname Win32 with the specific subfile called Computer System
#from your computer.
$computer = Get-CimInstance -ClassName Win32_ComputerSystem

#Grabs the username of the account that it is currently running on
#and prints it with the users Computer System Information.
Write-Output "$env:USERNAME's Computer System Information:"
Write-Output "----------------------------"

#Grabs the Manufacturer of the computer system
Write-Output "Manufacturer: $($computer.Manufacturer)"

#Grabs the Manufacturer of the computer system
Write-Output "Model: $($computer.Model)"
Write-Output ""

#Retrieves the classname Win32 with the specific subfile called Processor
#from your computer.
$cpu = Get-CimInstance -ClassName Win32_Processor

#Grabs the username of the account that it is currently running on
#and prints it with the users Processor Information.
Write-Output "$env:USERNAME's Processor Information:"
Write-Output "----------------------"

#Grabs the name of the Processor
Write-Output "Name: $($cpu.Name)"

#Grabs the number of cores from the Processor
Write-Output "Number of Cores: $($cpu.NumberOfCores)"

#Grabs the number of logical processors from the Processor
Write-Output "Number of Logical Processors: $($cpu.NumberOfLogicalProcessors)"

#Grabs the L2 Cache of the Processor
Write-Output "L2 Cache: $($cpu.L2CacheSize) KB"

#Grabs the L2 Cache of the Processor
Write-Output "L3 Cache: $($cpu.L3CacheSize) KB"

#Grabs the Clockspeed of the Processor
Write-Output "Clockspeed: $($cpu.CurrentClockSpeed) MHz"
Write-Output ""

#Retrieves the classname Win32 with the specific subfile called Diskdrive
#from your computer.
$disks = Get-CimInstance -ClassName Win32_DiskDrive

#Grabs the username of the account that it is currently running on
#and prints it with the users Diskdrive Information.
Write-Output "$env:USERNAME's Disk Information:"
Write-Output "-----------------"

#Runs a for loop for each disk drive that the script detects
foreach ($disk in $disks) {

    #Grabs the model of the diskdrive
    Write-Output "Model: $($disk.Model)"

    #Grabs the size of the diskdrive and uses rounding to calculate the capacity in GBs
    Write-Output "Size: $([math]::round($disk.Size / 1GB, 2)) GB"
    Write-Output ""
}

#Retrieves the classname Win32 with the specific subfile called PhysicalMemory
#from your computer.
$rams = Get-CimInstance -ClassName Win32_PhysicalMemory

#Grabs the username of the account that it is currently running on
#and prints it with the users Diskdrive Information.
Write-Output "$env:USERNAME's RAM Information:"
Write-Output "----------------------"

#Runs a for loop for each physical ram stick that the script detects
foreach ($ram in $rams) {

    #Grabs the name of the ram stick
    Write-Output "Name: $($ram.Name)"

    #Grabs the manufacturer of the ram stick
    Write-Output "Manufacturer: $($ram.Manufacturer)"

    #Grabs the model number of the ram stick
    Write-Output "Model: $($ram.PartNumber)"

    #Grabs the size of the ram stick and uses rounding to calculate the capacity in GBs
    Write-Output "Capacity: $([math]::round($ram.Capacity / 1GB, 2)) GB"

    #Grabs the speed of the ram stick
    Write-Output "Speed: $($ram.Speed) MHz"
    Write-Output ""
}
