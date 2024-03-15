#!/bin/bash

 if [[ $(uname -r | tr '[:upper:]' '[:lower:]') =~ "el6" ]] || [[ $(uname -r | tr '[:upper:]' '[:lower:]') =~ "amzn1" ]] || [[ $(uname -r | tr '[:upper:]' '[:lower:]') =~ "el7" ]] || [[ $(uname -r | tr '[:upper:]' '[:lower:]') =~ "amzn2" ]] ; then
    yum install -y wget unzip  jq
  elif [[ $(uname -a | tr '[:upper:]' '[:lower:]') =~ "ubuntu" ]] || [[ $(uname -a | tr '[:upper:]' '[:lower:]') =~ "debian" ]]; then
    apt-get install -y wget unzip jq
  fi
