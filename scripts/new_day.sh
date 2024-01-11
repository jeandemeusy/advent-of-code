# accept two arguments: -y (year) and -d (day)
# if year is not provided, use current year, if day is not provided, use current day

year=$(date +"%Y")
day=$(date +"%d")

while getopts y:d: flag
do
    case "${flag}" in
        y) year=${OPTARG};;
        d) day=${OPTARG};;
    esac
done

day=$(printf "%02d" ${day})

cp ./scripts/template.py ./py/${year}/day${day}.py
touch ./input/${year}/day${day}.txt
touch ./input/${year}/day${day}_sample.txt