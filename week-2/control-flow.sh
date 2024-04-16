# Loops


# for loop

read -a names

for name in "${names[@]}"
do
    echo "$name"
    if [ "$name" = "stop" ]; then
        echo "Stopped"
    fi
done


# While loop

while read -p "enter name" name ; do

    echo "$name"
    if [ "$name" = "stop" ]; then
        echo "Stopped"
        break
    fi
done