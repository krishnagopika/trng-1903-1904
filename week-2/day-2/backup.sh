function backup_files(){
    BACKUP_DIR="archives"

    echo $(-e $BACKUP_DIR)

    BACKUP_DATE=`date +%Y-%m-%d_%H-%M-%S`

    read -p "Enter file name: " FILE_NAME

    echo "$BACKUP_DATE"

    BACKUP_FILE="$BACKUP_DIR/${FILE_NAME}_${BACKUP_DATE}.tar.gz"

    tar -czf $BACKUP_FILE $FILE_NAME

}

backup_files




