# Program name: workWithFiles4.ps1
# Program description: Reads a list of dog names and appends to a list of cat names
# Programmer's name: Kelsey Gallo
# Date: 2-25-25
# Define variables containing paths to dognames.txt and catnames.txt
$dogFile = "C:\\cpt180stuff\\pets\\dogs\\dognames.txt"
$catFile = "C:\\cpt180stuff\\pets\\cats\\catnames.txt"
# Check to see if both files exist
$filesExist = (Test-Path -Path $dogFile) -AND (Test-Path -Path $catFile)
if ($filesExist -eq $True){
	 # Run the program if both files exist
	 $dogContent = Get-Content -Path $dogFile
     Write-Output -InputObject $dogContent # Display contents of dognames.txt
	 Write-Output ""
	 $catContent = Get-Content -Path $catFile
     Write-Output -InputObject $catContent # Display contents of catnames.txt
	 Write-Output ""
	 Add-Content -Path $catFile -Value "Hobbes", "Schrodinger" # Add two names to catnames.txt
	 $catContent2 = Get-Content -Path $catFile
     Write-Output -InputObject $catContent2 # Display contents of catnames.txt with added names
}
else{
	 # Print error message if one or both files are missing
	 Write-Output -InputObject "Unable to access one or more files"
}
<# A Powershell pipeline is a mechanism to combine commands in one expression. Each command is separated by the operator |, which sends the output of the
previous command to the following one. An example of this mechanism is when you want to print customized output using the Write-Host command. You can
specify the text of the output to print with the Write-Output command by typing Write-Output -InputOutput and your text, followed by the | operator and
the desired text and background color (by typing Write-Host -ForegroundColor [Color] -BackgroundColor [Color]). For instance, you can type the following:
Write-Output -InputObject "My favorite color is blue. | Write-Host -ForegroundColor DarkBlue -BackgroundColor Cyan
to produce dark blue text with a cyan background. #>