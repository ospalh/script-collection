# -*- coding: utf-8 ; mode: shell-script -*-
# © Copyright 2017 Roland Sieker <ospalh@gmail.com>
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
#
# Source this file. That is kind-of the point of it.

# Check if we have a socket and an ssh-agent
candidate_pid=$(pgrep -u $(whoami) -a ssh-agent | grep ~/.ssh/agent/socket | awk '{print $1}')
# N.B.: The ~ gets expanded, here and below.

if [ -n ${candidate_pid} ]
then
    echo Re-using agent with pid  ${candidate_pid}
    # There is an ssh-agent belonging to us running. Use that.
    export SSH_AGENT_PID=${candidate_pid}
    export SSH_AUTH_SOCK=~/.ssh/agent/socket
else
    echo Starting new agent
    # We may kill one started by KDE Plasma.
    eval $(/usr/bin/ssh-agent -s -k -a ~/.ssh/agent/socket)
    # Now add your identities
    ssh-add ~/.ssh/id_rsa
    # ssh-add ~/.ssh/my-second-private-key
fi
