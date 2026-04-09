# Create a new directory named 'rover_mission'
mkdir rover_mission 

# Move into the 'rover_mission' directory
cd rover_mission

# Create three empty text files
touch log1.txt log2.txt log3.txt

# Rename 'log1.txt' to 'mission_log.txt'
mv log1.txt mission_log.txt

echo "Find all files in the current directory that have a .log extension:"
# Find all files in the current directory with .log extension
find . -maxdepth 1 -name "*.log"
echo -e""

echo "Display the contents of mission_log.txt:"
# Display contents of the file
cat mission_log.txt
echo -e""

echo "Find and display all lines containing the word "ERROR" in mission_log.txt:"
# Search for lines containing "ERROR" in the file
grep "ERROR" mission_log.txt
echo -e""

echo "number of lines in mission_log.txt:"
# Count number of lines in the file
wc -l mission_log.txt
echo -e""

echo "system's current date and time:"
# Display current system date and time
date
echo -e""

echo "CPU usage of the system in real time:"
# Show real-time CPU usage
top 
echo -e""

# Schedule system shutdown after 10 minutes
shutdown +10