@ECHO OFF
echo "Converting Mod..."
SET convert="%~dp0%ConvertData_Rebellion"
cd GameInfo
for %%a in (*.entity) do %convert% entity %%a %%a txt
cd ..
cd Mesh
for %%a in (*.mesh) do %convert% mesh %%a %%a txt
cd ..
cd Particle
for %%a in (*.particle) do %convert% particle %%a %%a txt
cd ..
cd Window
for %%a in (*.brushes) do %convert% brushes %%a %%a txt
cd ..
echo "Converted Sucessfully"
pause