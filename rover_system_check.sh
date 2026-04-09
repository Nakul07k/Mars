# Generate a random battery percentage between 0 and 100
BATTERY=$(( RANDOM % 101 ))
B=1  

echo "Current Battery Level: ${BATTERY}%"

# Check if battery level is less than 20%
if [ "$BATTERY" -lt 20 ]; then
    echo "Battery low! Return to base!"
    B=0  # Set flag B to 0
fi

# Check network connectivity by pinging google.com
if ping -c 1 -W 3 google.com > /dev/null 2>&1; then
    echo "Communication link established."
else
    echo "Communication failure!"
    B=0
fi

# Final system status check
if [ "$B" -eq 1 ]; then
    echo "All systems operational!"
fi