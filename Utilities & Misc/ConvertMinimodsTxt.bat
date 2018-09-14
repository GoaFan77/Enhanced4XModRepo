@ECHO OFF
echo "Converting Mod..."
SET convert="%~dp0%ConvertData_Rebellion"
for /d %%f in (*) do (
	cd %~dp0%%f%\GameInfo
	for %%a in (*.entity) do %convert% entity %%a %%a txt
	cd %~dp0%%f%\Mesh
	for %%a in (*.mesh) do %convert% mesh %%a %%a txt
	cd %~dp0%%f%\Particle
	for %%a in (*.particle) do %convert% particle %%a %%a txt
	cd %~dp0%%f%\Window
	for %%a in (*.brushes) do %convert% brushes %%a %%a txt
	echo %%f
)
echo "Converted Sucessfully"
pause