n=$1
[ -n "$n" ] || n=1


l=$2

[ -n "$l" ] || l=8


for p in `seq 1 $n`
do
    password=`openssl rand -base64 ${l}`

    echo "$password" >> passwords.txt
done