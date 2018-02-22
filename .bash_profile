if [ -f /sw/bin/init.sh ]; then
    /sw/bin/init.sh
fi

[[ -s "$HOME/.rvm/scripts/rvm" ]] && source "$HOME/.rvm/scripts/rvm" # Load RVM into a shell session *as a function*

#spacer() { echo -e " ";}
export PS1="\n\e[96m\d \@ \e[33m\w\n🌀  \e[0m"
export PATH=$PATH:/usr/local/git/bin:/usr/local/sbin
export PATH=$PATH:/usr/local/bin/node:/usr/local/bin 
export CLICOLOR=1

alias camera='sudo killall VDCAssistant'
alias profile='sudo vim .bash_profile'
alias ip='curl ipecho.net/plain; echo'

# added by Anaconda 2.2.0 installer
export PATH="/Users/rt/anaconda/bin:$PATH"
export SPARK_HOME="/Users/rt/spark-1.3.1"
export PYTHONPATH=$PYTHONPATH:$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.8.2.1-src.zip
export GOPATH=$HOME/go
export PATH=$PATH:$GOPATH/bin
export PATH="$HOME/.node/bin:$PATH"
