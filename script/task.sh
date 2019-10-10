#!/usr/bin sh

# only one task at a time
if [ $# != 1 ]; then
    echo "usage: $0 <task_name>"
fi

rundev() {
    source ./.env
    flask run
}

case $1 in
    "rundev")        rundev;;
esac