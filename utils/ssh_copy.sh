#!/bin/bash

ssh $1 'cat >> ~/.ssh/authorized_keys' < $2
