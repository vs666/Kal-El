#!/bin/bash
# Path
#   /$USER/calApp/

if [[ $1 == '-h' ]]
then
    echo "Calendar App"
    echo "_________________________________________________"
    echo "calel -h --> for help"
    echo "calel -s --> show events"
    echo "calel -a --> add event"
    echo "_________________________________________________"
    echo "                      Created by Varul Srivastava"
else
if [[ $1 == '-s' ]]
then
    python3 /home/$USER/calApp/show_events.py
else
if [[ $1 == '-a' ]]
then
    python3 /home/$USER/calApp/add_event.py
else
    echo "Invalid Command. Type calel -h for help."
fi
fi
fi

