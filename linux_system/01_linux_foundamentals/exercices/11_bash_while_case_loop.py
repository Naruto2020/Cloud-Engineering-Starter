
=======================================================================

		🟦 BLOC 1 → 1.9 Bash — while loops

========================================================================


A for loop is useful when you have a collection of items:

for service in $services

A while loop is different: it keeps executing while a condition is true.

Basic structure

while [ condition ]
do
    commands
done


For example:

counter=1 

while [ "$counter" -le 3 ]
do
    echo "chcking server #$counter"
    counter=$((counter + 1))
done


====================================================================

		Next Bash concept: case

====================================================================

Bash case
1. What problem does case solve?

Imagine you have a variable:

action="start"

You could use if:

if [ "$action" = "start" ]; then
    echo "Starting service"
elif [ "$action" = "stop" ]; then
    echo "Stopping service"
elif [ "$action" = "status" ]; then
    echo "Checking service status"
else
    echo "Unknown action"
fi

This works.

But when you're checking one value against many possible values, case is cleaner.

That's exactly what case is designed for.

2. Basic structure

The general structure is:

case "$variable" in
    value1)
        commands
        ;;
    value2)
        commands
        ;;
    value3)
        commands
        ;;
    *)
        commands
        ;;
esac

Read it almost like English:

Case the value of $variable:

if it's value1, do this
if it's value2, do that
if it's value3, do something else
* means anything else

End case

That's why it starts with:

case

and ends with:

esac

esac is simply case backwards.

3. What does ;; mean?

Each case needs to finish with:

;;

It means:

"I'm finished with this case; don't continue into the next one."

For example:

case "$action" in
    start)
        echo "Starting service"
        ;;
    stop)
        echo "Stopping service"
        ;;
esac

If action="start", Bash executes:

Starting service

and then stops evaluating the case.

4. What is *?

This:

*)

means:

Anything that didn't match the previous cases.

For example:

action="restart"

If you only have start and stop, then restart doesn't match either.

So:

*)
    echo "Unknown action"
    ;;

will execute.

Why this matters in DevOps

You'll frequently have scripts where a user chooses an operation:

start
stop
restart
status

Instead of writing a huge chain of if/elif, case makes this very readable.

For example:

case "$action" in
    start)
        # start something
        ;;
    stop)
        # stop something
        ;;
    restart)
        # restart something
        ;;
    status)
        # check something
        ;;
    *)
        # invalid action
        ;;
esac

That's the concept.



Before moving further, let's practice another common Bash pattern used in Cloud/DevOps scripts: case, useful when you need to handle several possible values such as start, stop, restart, status.

I'll give you one exercise at a time, as usual.

Write a script that starts with:

action="status"

Then use case so that:

start → prints Starting service
stop → prints Stopping service
status → prints Checking service status
anything else → prints Unknown action


The important syntax to remember
case "$variable" in
    value1)
        commands
        ;;
    value2)
        commands
        ;;
    *)
        fallback
        ;;
esac

case is particularly useful in DevOps scripts for commands like:

./service.sh start
./service.sh stop
./service.sh status
./service.sh restart


======================================================================

		Bash Script Arguments

======================================================================


So far, our script has been using a value written inside the script:

action="status"

The problem is that if you want another action, you have to edit the script.

For example:

action="start"

then run it.

Then change it to:

action="stop"

then run it again.

That's not very useful for automation.

1. Passing information to a script

Bash lets you give information to a script when you execute it.

For example:

./service.sh start

Here:

./service.sh    → the script
start           → information given to the script

Bash makes that information available through positional parameters.

$1

The first argument is:

$1

So:

./service.sh start

inside the script:

$1

contains:

start
2. Multiple arguments

Suppose we execute:

./service.sh start nginx

There are now two arguments:

$1 → start
$2 → nginx

If we execute:

./service.sh restart nginx production

then:

$1 → restart
$2 → nginx
$3 → production

The position determines the variable.

3. $0

There is also:

$0

which represents the name/path used to invoke the script.

For example:

./service.sh start

roughly gives:

$0 → ./service.sh
$1 → start

So:

Variable	Meaning
$0	Script name/path
$1	First argument
$2	Second argument
$3	Third argument
4. Why is this useful for DevOps?

Now we can turn our previous script into an actual command.

Instead of:

action="status"

we can make the user choose the action:

./service.sh start

or:

./service.sh stop

or:

./service.sh status

The script doesn't need to be modified.

Conceptually:

User
  │
  │ ./service.sh start
  ▼
service.sh
  │
  │ $1 = "start"
  ▼
case "$1"
  │
  └── start → Starting service

This is the beginning of building CLI-style automation scripts, which you'll use frequently in DevOps.

5. $@

There is one more important argument variable:

$@

It represents all the arguments passed to the script.

For example:

./script.sh start nginx production

Then:

$1 → start
$2 → nginx
$3 → production
$@ → start nginx production

We won't use $@ yet. We'll come back to it when we need it.

Now let's apply the concept

We want to modify our previous script.

Previously:

action="status"

Now the action should come from the command line.

So instead of:

./service.sh

we want:

./service.sh start

and $1 should contain start.
